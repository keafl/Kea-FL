"""
llm.py
"""

import os
import json
import time
import re
from typing import List, Tuple

from openai import OpenAI

from ..utils.logger import get_logger
from ..utils.data_types import CoverageDiffResult


class LLM:
    """LLM class for file ranking"""

    def __init__(
            self,
            api_key: str,
            model: str = "deepseek-chat",
            base_url: str = "https://api.deepseek.com",
            temperature: float = 0.0,
            top_p: float = 0.1,
            frequency_penalty: float = 0.0,
            presence_penalty: float = 0.0
    ):
        """
        Initialize LLM class
        
        Args:
            api_key: API key for LLM
            model: Model name to use
            base_url: Base URL for LLM API
            temperature: Temperature for the model
            top_p: Top-p parameter for the model
            frequency_penalty: Frequency penalty for the model
            presence_penalty: Presence penalty for the model
        """
        self.api_key = api_key
        self.model = model
        self.base_url = base_url
        self.temperature = temperature
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.logger = get_logger("llm")

    def _auto_parse_coverage_diff(self, coverage_diff_data: CoverageDiffResult) -> str:
        """
        Format memory line coverage diff dict to human-readable text & extract diff file list

        Args:
            line_coverage_diff: key=source file path, value=line coverage diff object

        Returns:
            str: Formatted coverage diff text
        """
        line_coverage_diff = coverage_diff_data.line_coverage_diff
        coverage_text_lines: List[str] = []

        if not line_coverage_diff:
            self.logger.warning("line coverage diff dict is empty, no diff data")
            return "coverage diff data is empty"

        try:
            for file_path, diff_data in line_coverage_diff.items():
                coverage_text_lines.append(f"File: {file_path}")

                if diff_data.only_in_first:
                    coverage_text_lines.append(f"  Only in first dataset lines: {sorted(diff_data.only_in_first.keys())}")
                    for line_no, cnt in sorted(diff_data.only_in_first.items()):
                        coverage_text_lines.append(f"    Line {line_no}: hit count {cnt}")

                if diff_data.only_in_second:
                    coverage_text_lines.append(f"  Only in second dataset lines: {sorted(diff_data.only_in_second.keys())}")
                    for line_no, cnt in sorted(diff_data.only_in_second.items()):
                        coverage_text_lines.append(f"    Line {line_no}: hit count {cnt}")

                coverage_text_lines.append("-" * 40)

            full_text = "\n".join(coverage_text_lines)
            return full_text

        except Exception as e:
            self.logger.error(f"format coverage diff dict failed: {type(e).__name__}: {e}")
            return "parse failed"


    def _auto_parse_action_steps(self, test_case_name: str, steps_log_path: str) -> Tuple[str, str, str]:
        """
        Auto parse action steps file
        
        Args:
            test_case_name: Name of the test case
            steps_log_path: Path to action steps file
        
        Returns:
            Tuple[str, str, str]: Parsed action steps, first pass action steps, first fail action steps
        """

        if not os.path.exists(steps_log_path):
            self.logger.warning(f"action steps path does not exist: {steps_log_path}")
            return "action steps path does not exist", "no data", "no data"

        all_actions = []
        first_pass_idx = -1
        first_fail_idx = -1

        try:
            with open(steps_log_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for line in lines:
                line = line.strip()
                if not line:
                    continue

                try:
                    log_data = json.loads(line)
                    log_type = log_data.get("Type")
                    info = log_data.get("Info", "{}")
                    info_data = json.loads(info) if isinstance(info, str) else {}

                    if log_type == "Monkey":
                        act = info_data.get("act")
                        if act:
                            all_actions.append(f"Random operation: {act}")

                    elif log_type == "Script":
                        method = info_data.get("method")
                        params = info_data.get("params", [])

                        if method == "click":
                            widget = params[0] if params else ""
                            all_actions.append(f"Click: {widget[:50]}" if widget else "Click")

                        elif method == "setText":
                            text = params[1] if len(params) > 1 else ""
                            all_actions.append(f"Input: {text[:30]}")

                        elif method == "swipe":
                            all_actions.append("Swipe")

                        elif method == "pressKey" and params and params[0] == "back":
                            all_actions.append("Back")

                        elif method == "longClick":
                            all_actions.append("Long click")

                    elif log_type == "ScriptInfo":
                        prop_name = info_data.get("propName", "")
                        state = info_data.get("state")

                        if prop_name:
                            current_case = prop_name.split(".")[-1]

                            if state == "start":
                                all_actions.append(f"Start: {current_case}")

                            elif state == "pass":
                                all_actions.append(f"Pass: {current_case}")
                                if first_pass_idx == -1 and current_case == test_case_name:
                                    first_pass_idx = len(all_actions) - 1

                            elif state == "fail":
                                all_actions.append(f"Fail: {current_case}")
                                if first_fail_idx == -1 and current_case == test_case_name:
                                    first_fail_idx = len(all_actions) - 1

                except Exception:
                    continue

            # deduplicate
            dedup = []
            for i, a in enumerate(all_actions):
                if i == 0 or a != all_actions[i - 1]:
                    dedup.append(a)

            flow_pass = dedup[:first_pass_idx + 1] if first_pass_idx != -1 else []
            flow_fail = dedup[:first_fail_idx + 1] if first_fail_idx != -1 else []

            full_flow = " → ".join(dedup) if dedup else "No operation records"
            pass_flow = " → ".join(flow_pass) if flow_pass else "not found"
            fail_flow = " → ".join(flow_fail) if flow_fail else "not found"

            return full_flow, pass_flow, fail_flow

        except Exception as e:
            self.logger.error(f"parse action failed: {e}", exc_info=True)
            return "parse failed", "parse failed", "parse failed"


    def _generate_divergence_hint(self, correct_flow: str, error_flow: str) -> str:
        """
        Generate divergence hint for action steps
        
        Args:
            correct_flow: Correct action steps
            error_flow: Incorrect action steps
        
        Returns:
            str: Divergence hint
        """
        if "not found" in correct_flow or "not found" in error_flow:
            return "Unable to determine divergence point."

        pass_actions = [x.strip() for x in correct_flow.split("→")]
        fail_actions = [x.strip() for x in error_flow.split("→")]

        i = 0
        while i < len(pass_actions) and i < len(fail_actions):
            if pass_actions[i] != fail_actions[i]:
                break
            i += 1

        common = pass_actions[:i]
        pass_suffix = pass_actions[i:]
        fail_suffix = fail_actions[i:]

        out = []

        if common:
            out.append("Common prefix:\n" + " → ".join(common[-10:]))

        if pass_suffix:
            out.append("PASS continuation:\n" + " → ".join(pass_suffix))

        if fail_suffix:
            out.append("FAIL continuation:\n" + " → ".join(fail_suffix))

        return "\n\n".join(out)


    def _generate_file_summary(self, coverage_diff_data: CoverageDiffResult) -> str:
        """
        Generate file summary for coverage text
        
        Args:
            coverage_diff_data: Coverage diff data
        
        Returns:
            str: File summary
        """
        line_coverage_diff = coverage_diff_data.line_coverage_diff
        out = []

        for file, diff_lines in line_coverage_diff.items():
            line_counts = len(diff_lines.only_in_first.keys()) + len(diff_lines.only_in_second.keys())
            out.append(f"{file}\n  Differing lines: {line_counts}")

        return "\n\n".join(out)


    def auto_generate_prompt(self, test_case_name: str, coverage_diff_data: CoverageDiffResult, steps_log_path: str) -> str:
        """
        Generate prompt for LLM to find NCF bug

        Args:
            test_case_name: Name of the test case
            coverage_diff_path: path to the coverage diff file
            steps_log_path: path to the action steps log file
            test_script_path: path to the test script file
        
        Returns:
            str: Prompt for LLM
        """
        coverage_text = self._auto_parse_coverage_diff(coverage_diff_data)

        _, correct_flow, error_flow = self._auto_parse_action_steps(test_case_name, steps_log_path)

        divergence_hint = self._generate_divergence_hint(correct_flow, error_flow)

        file_summary = self._generate_file_summary(coverage_diff_data)

        prompt = f"""
## Question
You will read an event flow including page actions and code coverage differences between correct and error executions.
Then answer:
Which files most likely contain the non-crash functional (NCF) bug?

## Rules
(0) Infer functionality from failed test case name.
(1) Only NCF bugs.
(2) Compare execution flows and identify divergence point.
    (a) Focus on last shared action → first divergence.
    (b) Coverage is supporting evidence only.
(3) Consider state inconsistency issues.
(4) Ignore random exploratory actions unless directly relevant.
(5) Focus only on files relevant to failed scenario.
(6) Exclude test/mock/third-party code.
(7) Rank by contribution to divergence behavior.
(8) Prefer simplest explanation.

## Failed Test Case
{test_case_name}

## Code Coverage Summary
{coverage_text}

## Execution Divergence Hint
{divergence_hint}

## Correct Execution Path
{correct_flow}

## Error Execution Path
{error_flow}

## Files to Analyze
{file_summary}

## Output Format
Provide your answer with file paths only. Sort all the files by suspicion level (highest first). One file path per line. No numbering, no explanations, no additional text, no extra punctuation.

Output:
"""
        self.logger.info(f"Generated prompt: {prompt.strip()}")
        return prompt.strip()


    def run_ranking(self, prompt: str, max_retries: int = 2) -> list[str]:
        """
        Run LLM inference for NCF fault localization ranking task.
        
        Args:
            prompt: Prompt for LLM
            max_retries: Maximum number of retries for LLM call
        
        Returns:
            str: LLM inference result
        """
        last_error = None

        for attempt in range(max_retries + 1):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    stream=False,
                    temperature=self.temperature,
                    top_p=self.top_p,
                    frequency_penalty=self.frequency_penalty,
                    presence_penalty=self.presence_penalty
                )

                if not response:
                    raise ValueError("Empty response from LLM")

                if not response.choices:
                    raise ValueError("No choices in LLM response")

                content = response.choices[0].message.content

                if content is None or len(content.strip()) == 0:
                    raise ValueError("Empty content in LLM response")

                self.logger.info(f"LLM response: {content.strip()}")
                return [f.strip() for f in content.strip().splitlines()]

            except Exception as e:
                last_error = e
                self.logger.warning(
                    f"LLM call failed (attempt {attempt + 1}/{max_retries + 1}): {e}"
                )
                time.sleep(1.5 * (attempt + 1))  # exponential backoff

        # final fallback
        self.logger.error(f"LLM failed after retries: {last_error}")
        return []
