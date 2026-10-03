"""
log_parser.py
"""

import re
import os
import json
from typing import Optional

from .data_types import Touch, Action


class LogParser:
    TOUCH_PATTERN = re.compile(r":Sending Touch \((ACTION_\w+)\): \d+:\(([\d\.]+),([\d\.]+)\)") # touch action line pattern
    WAIT_PATTERN = re.compile(r"Wait Event for (\d+) milliseconds") # wait event line pattern
    ACTION_TYPE_PATTERN = re.compile(r"\[Fastbot\].*action type: (\w+)")  # action type pattern
    ACTION_END_PATTERN = re.compile(r"\[Fastbot\].*Finish monkey step")  # action end line pattern
    ACTION_OVER_PATTERN = re.compile(r"\[Fastbot\].*Monkey is over!")   # action over line pattern

    def parse_touch(self, log_line: str) -> Optional[Touch]:
        """解析触摸动作行，返回touch action type和coordinate"""
        match = self.TOUCH_PATTERN.search(log_line)
        if not match:
            return None

        touch_map = {"ACTION_DOWN": "down", "ACTION_MOVE": "move", "ACTION_UP": "up"}
        touch_type = touch_map.get(match.group(1))
        if not touch_type:
            return None

        x = float(match.group(2))
        y = float(match.group(3))
        return Touch(touch_type, x, y)

    def parse_action(self, segment_lines: list[str]) -> Optional[Action]:
        """
        parse action segment lines, return action object
        """
        action_type = None
        for line in segment_lines:
            type_match = self.ACTION_TYPE_PATTERN.search(line)
            if type_match:
                action_type = type_match.group(1)
                break
        if not action_type:
            return None

        touch_series = []
        wait_duration = 0.0
        for line in segment_lines:
            wait_match = self.WAIT_PATTERN.search(line)
            if wait_match:
                wait_duration = float(wait_match.group(1)) / 1000
                continue

            touch = self.parse_touch(line)
            if touch:
                touch.wait_duration = wait_duration
                touch_series.append(touch)
                wait_duration = 0.0  # reset wait duration after each touch

        return Action(action_type, touch_series)


    def split_actions(self, log_lines: list[str]) -> list[list[str]]:
        """分割多段日志，返回各段action的行列表"""
        segments = []
        current_segment = []
        in_action = False  # flag to track if we are in an action

        for line in log_lines:
            line = line.strip()
            if not line:
                continue

            # action start
            if self.ACTION_TYPE_PATTERN.search(line):
                in_action = True
                current_segment = [line]
                continue

            # action end
            if (self.ACTION_END_PATTERN.search(line) or self.ACTION_OVER_PATTERN.search(line)) and in_action:
                in_action = False
                segments.append(current_segment)
                current_segment = []
                continue

            # collect action lines within the current action segment
            if in_action:
                current_segment.append(line)

        return segments


    def parse_monkey_log(self, log_path: str) -> list[Action]:
        """
        parse monkey log file

        Args:
            log_path (str): monkey log file path
        Returns:
            list[Action]: list of action objects
        """
        if not os.path.exists(log_path):
            raise FileNotFoundError(f"Monkey log file not found: {log_path}")

        with open(log_path, "r", encoding="utf-8") as f:
            log_lines = f.readlines()

        action_segments = self.split_actions(log_lines)
        if not action_segments:
            return []

        actions = []
        for segment in action_segments:
            action = self.parse_action(segment)
            if action:  # action is not None, filter out empty actions
                actions.append(action)

        return actions


    def parse_step_log(self, step_log_path: str):
        """
        parse step.log file

        Args:
            step_log_path (str): step.log file path
        Returns:
            list[dict]: list of event objects
        """
        if not os.path.exists(step_log_path):
            raise FileNotFoundError(f"step.log file not found: {step_log_path}")
        
        EVENT_TYPE_MONKEY = "Monkey"
        EVENT_TYPE_SCRIPT = "Script"
        EVENT_TYPE_SCRIPT_INFO = "ScriptInfo"
        events= []
        log_lines = []

        with open(step_log_path, 'r', encoding='utf-8') as f:
            log_lines = [line.strip() for line in f if line.strip()]

        for line_num, line_stripped in enumerate(log_lines, 1):
            try:
                event: dict = json.loads(line_stripped)
                event_type = event.get("Type", "")
                step_count = event.get("MonkeyStepsCount", 0)

                if event_type == EVENT_TYPE_MONKEY:
                    info: dict = json.loads(event.get("Info", "{}"))
                    events.append({
                        "type": "monkey",
                        "action": info.get("act", ""),
                        "step_count": step_count,
                        "pos": info.get("pos", [])
                    })
                elif event_type == EVENT_TYPE_SCRIPT:
                    info = json.loads(event.get("Info", "{}"))
                    events.append({
                        "type": "script",
                        "method": info.get("method", ""),
                        "params": info.get("params", []),
                        "step_count": step_count
                    })
                elif event_type == EVENT_TYPE_SCRIPT_INFO:
                    info = json.loads(event.get("Info", "{}"))
                    events.append({
                        "type": "script_info",
                        "prop_name": info.get("propName", ""),
                        "state": info.get("state", ""),
                        "step_count": step_count
                    })
            except json.JSONDecodeError as e:
                raise RuntimeError(
                    f"Line {line_num} JSON parse error: {line_stripped} | Error details: {str(e)}"
                ) from e

        return events