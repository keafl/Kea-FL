"""
differ.py
"""

from typing import Dict, Tuple, List
from ..utils.data_types import LineCoverageData, BranchCoverageData, LineCoverageDiff, BranchCoverageDiff



def _compare_line_diff_for_file(
    lines_in_first: Dict[int, int], 
    lines_in_second: Dict[int, int]
) -> LineCoverageDiff:
    """
    Compare line coverage data for a single file, returning the difference
    
    Args:
        lines_in_first: Line coverage data for the first dataset, {line_number: cover_count}
        lines_in_second: Line coverage data for the second dataset, {line_number: cover_count}
        
    Returns:
        LineCoverageDiff object
    """
    # Find lines that are only in the first dataset
    only_in_first = {line: lines_in_first[line] for line in lines_in_first if line not in lines_in_second}
    
    # Find lines that are only in the second dataset
    only_in_second = {line: lines_in_second[line] for line in lines_in_second if line not in lines_in_first}
    
    return LineCoverageDiff(only_in_first, only_in_second)


def _compare_branch_diff_for_file(
    branches_in_first: Dict[int, Tuple[int, int]], 
    branches_in_second: Dict[int, Tuple[int, int]]
) -> BranchCoverageDiff:
    """
    Compare branch coverage data for a single file, returning the difference
    
    Args:
        branches_in_first: Branch coverage data for the first dataset, {line_number: (covered_branch_count, total_branch_count)}
        branches_in_second: Branch coverage data for the second dataset, {line_number: (covered_branch_count, total_branch_count)}
        
    Returns:
        BranchCoverageDiff object
    """
    # Find branches that are only in the first dataset
    only_in_first = {line: branches_in_first[line] for line in branches_in_first if line not in branches_in_second}
    
    # Find branches that are only in the second dataset
    only_in_second = {line: branches_in_second[line] for line in branches_in_second if line not in branches_in_first}
    
    return BranchCoverageDiff(only_in_first, only_in_second)


def compare_line_diff(
    first: LineCoverageData, 
    second: LineCoverageData
) -> Dict[str, LineCoverageDiff]:
    """
    Compare two line coverage datasets, finding the difference
    
    Args:
        first: Line coverage data for the first dataset, {file_path: {line_number: cover_count}}
        second: Line coverage data for the second dataset, {file_path: {line_number: cover_count}}
        
    Returns:
        Line coverage difference for each file, {file_path: LineCoverageDiff}
    """
    all_files = set(first.keys()).union(set(second.keys()))
    
    diff_result = {}
    
    for file in sorted(all_files):
        lines_in_first = first.get(file, {})
        lines_in_second = second.get(file, {})
        
        # Compare line coverage data for the current file
        file_diff = _compare_line_diff_for_file(lines_in_first, lines_in_second)
        
        # Only add to result if there are differences
        if file_diff.only_in_first or file_diff.only_in_second:
            diff_result[file] = file_diff
    
    return diff_result


def compare_branch_diff(
    first: BranchCoverageData, 
    second: BranchCoverageData
) -> Dict[str, BranchCoverageDiff]:
    """
    Compare two branch coverage datasets, finding the difference
    
    Args:
        first: Branch coverage data for the first dataset, {file_path: {line_number: (covered_branch_count, total_branch_count)}}
        second: Branch coverage data for the second dataset, {file_path: {line_number: (covered_branch_count, total_branch_count)}}
        
    Returns:
        Branch coverage difference for each file, {file_path: BranchCoverageDiff}
    """
    all_files = set(first.keys()).union(set(second.keys()))

    diff_result = {}

    for file in sorted(all_files):
        branches_in_first = first.get(file, {})
        branches_in_second = second.get(file, {})
        
        # Compare branch coverage data for the current file
        file_diff = _compare_branch_diff_for_file(branches_in_first, branches_in_second)
        
        # Only add to result if there are differences
        if file_diff.only_in_first or file_diff.only_in_second:
            diff_result[file] = file_diff

    return diff_result


def format_line_diff_result(line_diff_result: Dict[str, LineCoverageDiff]) -> List[str]:
    """
    Format line coverage difference results as a list of strings
    
    Args:
        line_diff_result: Line coverage difference results, {file_path: LineCoverageDiff}
        
    Returns:
        Formatted string list, suitable for printing or writing to a file
    """
    formatted_lines = []
    
    # Format line coverage difference results
    if line_diff_result:
        formatted_lines.append("========== Line coverage difference ==========\n")
        for file_path in sorted(line_diff_result.keys()):
            line_diff = line_diff_result[file_path]
            formatted_lines.append(f"File: {file_path}\n")
            
            # Only in first dataset
            if line_diff.only_in_first:
                formatted_lines.append("  Only in first dataset::")
                for line_number in sorted(line_diff.only_in_first.keys()):
                    formatted_lines.append(f"    Line {line_number}: Covered {line_diff.only_in_first[line_number]}")
            
            # Only in second dataset
            if line_diff.only_in_second:
                formatted_lines.append("  Only in second dataset::")
                for line_number in sorted(line_diff.only_in_second.keys()):
                    formatted_lines.append(f"    Line {line_number}: Covered {line_diff.only_in_second[line_number]}")
            formatted_lines.append("\n")
    
    return formatted_lines


def format_branch_diff_result(branch_diff_result: Dict[str, BranchCoverageDiff]) -> List[str]:
    """
    Format branch coverage difference results as a list of strings
    
    Args:
        branch_diff_result: Branch coverage difference results, {file_path: BranchCoverageDiff}
        
    Returns:
        Formatted string list, suitable for printing or writing to a file
    """
    formatted_lines = []
    
    # Format branch coverage difference results
    if branch_diff_result:
        formatted_lines.append("========== Branch coverage difference ==========\n")
        for file_path in sorted(branch_diff_result.keys()):
            branch_diff = branch_diff_result[file_path]
            formatted_lines.append(f"File: {file_path}\n")
            
            # Only in first dataset
            if branch_diff.only_in_first:
                formatted_lines.append("  Only in first dataset::")
                for line_number in sorted(branch_diff.only_in_first.keys()):
                    covered_count, total_count = branch_diff.only_in_first[line_number]
                    formatted_lines.append(f"    Line {line_number}: Covered {covered_count} ({total_count})")
            
            # Only in second dataset
            if branch_diff.only_in_second:
                formatted_lines.append("  Only in second dataset::")
                for line_number in sorted(branch_diff.only_in_second.keys()):
                    covered_count, total_count = branch_diff.only_in_second[line_number]
                    formatted_lines.append(f"    Line {line_number}: Covered {covered_count} ({total_count})")
            formatted_lines.append("\n")
    
    return formatted_lines