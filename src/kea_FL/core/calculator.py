"""
calculator.py
"""

from typing import List
from ..utils.data_types import LineCoverageData, BranchCoverageData


def calculate_line_coverage_increment(
    baseline_coverage: LineCoverageData, 
    current_coverage: LineCoverageData, 
) -> LineCoverageData:
    """
    Compare two line coverage data and output the difference to a file
    Only output the lines that are added in current_coverage
    
    Args:
        baseline_coverage: Baseline version coverage data {file_path: {line_number: coverage_count}}
        
        current_coverage: Current version coverage data {file_path: {line_number: coverage_count}}
    
    Returns:
        Incremental line coverage data {file_path: {line_number: coverage_count}}
    """
    # get the union of all file paths
    all_file_paths = set(baseline_coverage.keys()).union(set(current_coverage.keys()))
    incremental_coverage_data: LineCoverageData = {}
    
    # iterate over each file path
    for file_path in sorted(all_file_paths):
        baseline_lines = baseline_coverage.get(file_path, {})
        current_lines = current_coverage.get(file_path, {})
        
        # find the lines that are added or improved in current_coverage
        added_or_improved_lines = {}
        for line_number, coverage_count in current_lines.items():
            if line_number not in baseline_lines:
                added_or_improved_lines[line_number] = coverage_count
            elif baseline_lines[line_number] == 0 and coverage_count > 0:
                added_or_improved_lines[line_number] = coverage_count
        
        if added_or_improved_lines:
            incremental_coverage_data[file_path] = added_or_improved_lines
    
    return incremental_coverage_data


def format_line_coverage_increment_data(
    increment_data: LineCoverageData
) -> List[str]:
    """
    Format line coverage increment data to a list of strings
    
    Args:
        increment_data: Incremental line coverage data {file_path: {line_number: coverage_count}}
        
    Returns:
        Formatted list of strings, suitable for writing to a file
    """
    lines = []
    
    for file in sorted(increment_data.keys()):
        lines.append(f"===== File: {file} =====\n")
        file_data = increment_data[file]
        # 按行号排序输出
        for line_num in sorted(file_data.keys()):
            lines.append(f"Line {line_num}: Covered {file_data[line_num]} times")
        lines.append("\n")
    
    return lines


def calculate_branch_coverage_increment(
    baseline_coverage: BranchCoverageData, 
    current_coverage: BranchCoverageData, 
) -> BranchCoverageData:
    """
    Compare two branch coverage data and output the difference to a file
    Only output the branches that are added or improved in current_coverage
    
    Args:
        baseline_coverage: Baseline version branch coverage data {file_path: {line_number: (covered_count, total_count)}}
        current_coverage: Current version branch coverage data {file_path: {line_number: (covered_count, total_count)}}
    
    Returns:
        Incremental branch coverage data {file_path: {line_number: (covered_count, total_count)}}
    """
    # get the union of all file paths
    all_file_paths = set(baseline_coverage.keys()).union(set(current_coverage.keys()))
    incremental_branch_data: BranchCoverageData = {}

    # iterate over each file path
    for file_path in sorted(all_file_paths):
        baseline_branches = baseline_coverage.get(file_path, {})
        current_branches = current_coverage.get(file_path, {})
        
        # find the branches that are added or improved in current_coverage
        added_or_improved_branches = {}
        for line_number, (current_covered_count, current_total_count) in current_branches.items():
            if line_number not in baseline_branches:
                # branch is added in current_coverage
                added_or_improved_branches[line_number] = (current_covered_count, current_total_count)
            else:
                baseline_covered_count, baseline_total_count = baseline_branches[line_number]
                # branch is improved in current_coverage
                if baseline_total_count == current_total_count and current_covered_count > baseline_covered_count:
                    added_or_improved_branches[line_number] = (current_covered_count, current_total_count)
                # branch is added in current_coverage
                elif current_total_count > baseline_total_count and current_covered_count > 0:
                    added_or_improved_branches[line_number] = (current_covered_count, current_total_count)
        
        if added_or_improved_branches:
            incremental_branch_data[file_path] = added_or_improved_branches
    
    return incremental_branch_data


def format_branch_coverage_increment_data(
    increment_data: BranchCoverageData
) -> List[str]:
    """
    Format branch coverage increment data to a list of strings
    
    Args:
        increment_data: Incremental branch coverage data {file_path: {line_number: (covered_count, total_count)}}
        
    Returns:
        Formatted list of strings, suitable for writing to a file
    """
    lines = []
    
    for file in sorted(increment_data.keys()):
        lines.append(f"===== File: {file} =====\n")
        file_data = increment_data[file]
        for line_num in sorted(file_data.keys()):
            covered, total = file_data[line_num]
            lines.append(f"Line {line_num}: Covered {covered} times ({total} branches)")
        lines.append("\n")
    
    return lines