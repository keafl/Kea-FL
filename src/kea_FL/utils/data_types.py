"""
data_types.py
"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional, List

# line code coverage data type
# data format: {file_path: {line_number: cover_count}}
LineCoverageData = dict[str, dict[int, int]]

# branch code coverage data type
# data format: {file_path: {line_number: (covered_branches, total_branches)}}
BranchCoverageData = dict[str, dict[int, tuple[int, int]]]


@dataclass
class LineCoverageDiff:
    """line code coverage difference data structure"""
    # lines only in first data set {line_number: cover_count}
    only_in_first: dict[int, int]
    # lines only in second data set {line_number: cover_count}
    only_in_second: dict[int, int]


@dataclass
class BranchCoverageDiff:
    """branch code coverage difference data structure"""
    # branches only in first data set {line_number: (covered_branches, total_branches)}
    only_in_first: dict[int, tuple[int, int]]
    # branches only in second data set {line_number: (covered_branches, total_branches)}
    only_in_second: dict[int, tuple[int, int]]


@dataclass
class CoverageDiffResult:
    """coverage difference result data structure"""
    # file level difference {file_path: diff_details}
    line_coverage_diff: dict[str, LineCoverageDiff]
    branch_coverage_diff: dict[str, BranchCoverageDiff]


class TestStatus(Enum):
    """test status enum"""
    SUCCESS = "success"
    UNEXECUTED = "unexecuted"
    ERROR = "error"


@dataclass
class TestCase:
    """test case data class"""
    name: str
    preconditions: list[dict]  # test case precondition event sequence
    property: list[dict]  # test case property event sequence


@dataclass
class TestResult:
    """test result data class"""
    status: TestStatus
    error_message: Optional[str]
    execution_time: float
    timestamp: str


@dataclass
class CoverageData:
    """coverage data class"""
    xml_path: str
    timestamp: str


@dataclass
class TestData:
    """test data class"""   
    test_case: TestCase
    precondition_result: TestResult
    property_result: TestResult
    precondition_coverage_data: CoverageData
    property_coverage_data: CoverageData


@dataclass
class PairTestCase:
    """pair test case data class"""
    case_name: str
    happy_path: TestCase
    bug_path: TestCase


@dataclass
class PairAnalysisResult:
    """pair test case analysis result data class"""
    case_name: str
    diff_result: CoverageDiffResult
    bug_precondition_xml: str  # xml path
    bug_property_xml: str 
    correct_precondition_xml: str 
    correct_property_xml: str 
    bug_incremental_coverage: dict  # include line_coverage_incremental and branch_coverage_incremental
    correct_incremental_coverage: dict
    line_diff_report_path: str   # line coverage report path
    branch_diff_report_path: str  # branch coverage report path
    ranking: list[str]  # ranking result


@dataclass
class FullAnalysisResult:
    """full analysis result data class"""
    pair_results: List[PairAnalysisResult]


HAPPY_PREFIX = "happy_"
BUG_PREFIX = "bug_"
PRECONDITION_SUFFIX = "_pre"
PROPERTY_SUFFIX = "_prop"


@dataclass
class Touch():
    touch_type: str  # touch action type: down, move, up
    x: float  # coordinate x
    y: float  # coordinate y
    wait_duration: float = 0.0  # wait duration ms, by default 0


@dataclass
class Action():
    action_type: str  # action type
    touch_series: list[Touch]  # touch action series: (touch_type, coordinate_x, coordinate_y, wait_duration_ms
