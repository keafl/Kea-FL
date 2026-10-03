"""
runner.py
"""

import os
import time
from typing import List, Tuple, Callable

from .config import Config
from ..utils.llm import LLM
from ..utils.adb_wrapper import AdbWrapper
from ..utils.data_types import *
from ..utils.reproducer import Reproducer
from ..utils.logger import configure_logger, get_logger
from ..core.parser import parse_jacoco_line_coverage, parse_jacoco_branch_coverage
from ..core.differ import compare_line_diff, compare_branch_diff
from ..core.calculator import calculate_line_coverage_increment, calculate_branch_coverage_increment
from ..utils.report_generator import ReportGenerator

class WorkflowRunner:
    """Workflow runner class, coordinate the coverage difference analysis process"""
    def __init__(self, config: Config, init_operation: Callable = lambda: None, ec_file_generator: Callable = lambda: None):
        """
        Initialize WorkflowRunner class
        
        Args:
            config: Config object
            init_operation: Initialize operation function
            ec_file_generator: Coverage file generator function
        """
        self.config = config
        self.init_operation = init_operation
        self.ec_file_generator = ec_file_generator
        self.reproducer = Reproducer(AdbWrapper(config.adb_path), config.app_package, config.apk_path, config.device_serial)
        self.report_generator = ReportGenerator(self.config.app_source_dir)
        if self.config.llm_api_key and self.config.llm_model and self.config.llm_base_url:
            self.llm = LLM(self.config.llm_api_key, self.config.llm_model, self.config.llm_base_url)
        else:
            self.llm = None
        configure_logger(self.config.report_output_dir, "workflow.log")
        self.logger = get_logger("runner")


    def run_full_analysis(self, pair_test_cases: List[PairTestCase]) -> FullAnalysisResult:
        """
        Run full coverage difference analysis process
        
        Args:
            pair_test_cases: List of pair test cases to analyze
            
        Returns:
            FullAnalysisResult object
        """
        if len(pair_test_cases) == 0:
            raise ValueError("Pair test cases list is empty")
        
        self.logger.info("Start running full coverage difference analysis...")
        
        pair_results = []
        
        for i, pair_case in enumerate(pair_test_cases):
            self.logger.info(f"Processing pair test case [{i+1}]: {pair_case.happy_path.name} <-> {pair_case.bug_path.name}")
            
            case_output_dir = os.path.join(
                self.config.report_output_dir, 
                pair_case.case_name
            )
            os.makedirs(case_output_dir, exist_ok=True)
            
            pair_result = self._run_pair_analysis(
                pair_case, self.init_operation, self.ec_file_generator, case_output_dir
            )
            pair_results.append(pair_result)
        
        full_result = FullAnalysisResult(
            pair_results=pair_results,
        )
        
        reproducer_data = self.reproducer.data
        output_dir = self.config.report_output_dir
        self.report_generator.generate_comprehensive_report(full_result, reproducer_data, output_dir)
        self.logger.info(f"Full coverage difference analysis completed, processed {len(pair_test_cases)} pair test cases, results saved to: {output_dir}")
        return full_result


    def _run_pair_analysis(self, 
                        pair_case: PairTestCase,
                        init_operation: Callable, 
                        ec_file_generator: Callable,
                        output_dir: str
    ) -> PairAnalysisResult:
        """
        Run pair test case analysis process
        
        Args:
            pair_case: Pair test case
            output_dir: Output directory
            
        Returns:
            PairAnalysisResult object
        """
        self.logger.info(f"Running pair test case analysis: {pair_case.happy_path.name} <-> {pair_case.bug_path.name}")
        self.logger.info("Running property-satisfying path...")
        correct_precondition_xml, correct_property_xml = self._run_single_flow(
            pair_case.happy_path, init_operation, ec_file_generator, output_dir
        )

        self.logger.info("Running property-violating path path...")
        bug_precondition_xml, bug_property_xml = self._run_single_flow(
            pair_case.bug_path, init_operation, ec_file_generator, output_dir
        )

        self.logger.info("Parsing coverage data...")
        data_dir = os.path.join(output_dir, "data")
        os.makedirs(data_dir, exist_ok=True)

        bug_case_pre = BUG_PREFIX + pair_case.case_name + PRECONDITION_SUFFIX
        bug_case_prop = BUG_PREFIX + pair_case.case_name + PROPERTY_SUFFIX
        bug_precondition_line_cov = parse_jacoco_line_coverage(bug_precondition_xml)
        self.report_generator.generate_line_coverage_data(bug_precondition_line_cov, bug_case_pre, data_dir)
        bug_precondition_branch_cov = parse_jacoco_branch_coverage(bug_precondition_xml)
        self.report_generator.generate_branch_coverage_data(bug_precondition_branch_cov, bug_case_pre, data_dir)
        bug_property_line_cov = parse_jacoco_line_coverage(bug_property_xml)
        self.report_generator.generate_line_coverage_data(bug_property_line_cov, bug_case_prop, data_dir)
        bug_property_branch_cov = parse_jacoco_branch_coverage(bug_property_xml)
        self.report_generator.generate_branch_coverage_data(bug_property_branch_cov, bug_case_prop, data_dir)

        happy_case_pre = HAPPY_PREFIX + pair_case.case_name + PRECONDITION_SUFFIX
        happy_case_prop = HAPPY_PREFIX + pair_case.case_name + PROPERTY_SUFFIX
        correct_precondition_line_cov = parse_jacoco_line_coverage(correct_precondition_xml)
        self.report_generator.generate_line_coverage_data(correct_precondition_line_cov, happy_case_pre, data_dir)
        correct_precondition_branch_cov = parse_jacoco_branch_coverage(correct_precondition_xml)
        self.report_generator.generate_branch_coverage_data(correct_precondition_branch_cov, happy_case_pre, data_dir)
        correct_property_line_cov = parse_jacoco_line_coverage(correct_property_xml)
        self.report_generator.generate_line_coverage_data(correct_property_line_cov, happy_case_prop, data_dir)
        correct_property_branch_cov = parse_jacoco_branch_coverage(correct_property_xml)
        self.report_generator.generate_branch_coverage_data(correct_property_branch_cov, happy_case_prop, data_dir)
        
        self.logger.info("Calculating incremental coverage...")
        bug_incremental = self._calculate_incremental_coverage(
            bug_precondition_line_cov, bug_precondition_branch_cov,
            bug_property_line_cov, bug_property_branch_cov
        )

        correct_incremental = self._calculate_incremental_coverage(
            correct_precondition_line_cov, correct_precondition_branch_cov,
            correct_property_line_cov, correct_property_branch_cov
        )

        self.logger.info("Performing incremental coverage analysis...")
        diff_result = self._perform_diff_analysis(
            bug_incremental["line_coverage_incremental"],
            bug_incremental["branch_coverage_incremental"],
            correct_incremental["line_coverage_incremental"],
            correct_incremental["branch_coverage_incremental"]
        )
        
        self.logger.info("Generating pair test case report...")
        result = PairAnalysisResult(
            case_name=pair_case.case_name,
            diff_result=diff_result,
            bug_precondition_xml=bug_precondition_xml,
            bug_property_xml=bug_property_xml,
            correct_precondition_xml=correct_precondition_xml,
            correct_property_xml=correct_property_xml,
            bug_incremental_coverage=bug_incremental,
            correct_incremental_coverage=correct_incremental,
            line_diff_report_path="",
            branch_diff_report_path="",
            ranking=[]
        )
        
        self.logger.info("Saving intermediate data...")
        os.makedirs(data_dir, exist_ok=True)
        self.report_generator.generate_compared_data(result, data_dir)

        self.logger.info("Generating diff report...")
        line_diff_report_path, branch_diff_report_path = self.report_generator.generate_diff_report(result, output_dir)
        result.line_diff_report_path = line_diff_report_path
        result.branch_diff_report_path = branch_diff_report_path

        if self.llm:
            prompt = self.llm.auto_generate_prompt(
                test_case_name=result.case_name,
                coverage_diff_data=result.diff_result,
                steps_log_path=self.step_log_path,
            )
            ranking = self.llm.run_ranking(prompt)
            result.ranking = ranking
            # Save ranking to file
            self.logger.info(f"Saving ranking to {os.path.join(output_dir, 'ranking.txt')}")    
            with open(os.path.join(output_dir, "ranking.txt"), "w") as f:
                f.write("\n".join(ranking))

        return result


    def _run_single_flow(self, test_case: TestCase, init_operation: Callable, ec_file_generator: Callable, output_dir: str) -> Tuple[str, str]:
        """
        Execute single test case flow and collect coverage data before and after the test case
        
        Args:
            test_case: Test case object
            init_operation: Initialization operation function
            ec_file_generator: Coverage data file generator function
            output_dir: Output directory
            
        Returns:
            Tuple of precondition and property XML file paths, (precondition_xml_path, property_xml_path) 
        """
        data = self.reproducer.reproduce_test_case(test_case,
                                                    output_dir,
                                                    ec_file_generator,
                                                    self.config.ec_file_path,
                                                    self.config.jacococli_jar_path, 
                                                    self.config.app_classfiles_dir, 
                                                    self.config.app_source_dir,
                                                    init_operation)

        precondition_xml_path = data.precondition_coverage_data.xml_path
        property_xml_path = data.property_coverage_data.xml_path

        return precondition_xml_path, property_xml_path


    def _calculate_incremental_coverage(self, 
                                    precondition_line_cov: LineCoverageData,
                                    precondition_branch_cov: BranchCoverageData,
                                    property_line_cov: LineCoverageData,
                                    property_branch_cov: BranchCoverageData
    ) -> dict:
        """
        Calculate incremental coverage between precondition and property coverage data
        
        Returns:
            Dictionary containing line coverage and branch coverage incremental data
        """
        line_incremental = calculate_line_coverage_increment(precondition_line_cov, property_line_cov)
        branch_incremental = calculate_branch_coverage_increment(precondition_branch_cov, property_branch_cov)
        
        return {
            "line_coverage_incremental": line_incremental,
            "branch_coverage_incremental": branch_incremental
        }


    def _perform_diff_analysis(self, 
                            first_line_cov_inc: LineCoverageData,
                            first_branch_cov_inc: BranchCoverageData,
                            second_line_cov_inc: LineCoverageData, 
                            second_branch_cov_inc: BranchCoverageData
    ) -> CoverageDiffResult:
        """
        Perform incremental coverage difference analysis between two sets of line coverage and branch coverage data
        
        Returns:
            Coverage difference result object
        """
        line_diff = compare_line_diff(first_line_cov_inc, second_line_cov_inc)
        branch_diff = compare_branch_diff(first_branch_cov_inc, second_branch_cov_inc)
        
        return CoverageDiffResult(line_diff, branch_diff)


    def build_pair_test_cases(self, step_log_path: str, fastbot_log_path: str) -> List[PairTestCase]:
        """
        Build pair test cases from step log and fastbot log files
        """
        self.step_log_path = step_log_path
        self.logger.info("Building pair test cases...")
        return self.reproducer.build_pair_test_cases(step_log_path, fastbot_log_path)
