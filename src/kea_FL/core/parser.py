"""
parser.py
"""

import xml.etree.ElementTree as ET
from typing import Dict, Tuple, List

from ..utils.data_types import LineCoverageData, BranchCoverageData
from ..utils.logger import get_logger

logger = get_logger("parser")

def parse_jacoco_line_coverage(xml_path: str) -> LineCoverageData:
    """
    Parse Jacoco XML file

    Args:
        xml_path: Path to the Jacoco XML file
    
    Returns:
        Returns line coverage data: {file_path: {line_number: cover_count}}
    """
    line_coverage: LineCoverageData = {}
    
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        for package_elem in root.iter('package'):
            package_name = package_elem.get('name', '')
            
            for source_elem in package_elem.findall('sourcefile'):
                source_file = source_elem.get('name')
                if not source_file:
                    continue
                
                # Build full path
                full_path = f"{package_name}/{source_file}" if package_name else source_file
                
                # Extract line number and cover count
                lines: Dict[int, int] = {}
                for line in source_elem.findall('line'):
                    line_nr = int(line.get('nr', 0))
                    covered_times = int(line.get('ci', 0))
                    if covered_times > 0:  # Only record lines that are covered
                        lines[line_nr] = covered_times
                
                if lines:
                    line_coverage[full_path] = lines
    
    except Exception as e:
        logger.error(f"Error parsing XML file ({xml_path}): {str(e)}")
        raise
    
    return line_coverage


def format_line_coverage_data(coverage_data: LineCoverageData) -> List[str]:
    """
    Format line coverage data to a list of strings
    
    Args:
        coverage_data: Line coverage data {file_path: {line_number: cover_count}}
        
    Returns:
        Formatted string of lines, ready for printing or writing to a file
    """
    formatted_lines = []
    
    for file_path in sorted(coverage_data.keys()):
        formatted_lines.append(f"===== File: {file_path} =====\n")
        file_coverage = coverage_data[file_path]
        # Sort lines by line number
        for line_number in sorted(file_coverage.keys()):
            formatted_lines.append(f"Line {line_number}: Covered {file_coverage[line_number]} times")
        formatted_lines.append("\n")
    
    return formatted_lines


def parse_jacoco_branch_coverage(xml_path: str) -> BranchCoverageData:
    """
    Parse Jacoco XML file
    
    Args:
        xml_path: Path to the Jacoco XML file
    
    Returns:
        Returns branch coverage data, formatted as: {file_path: {line_number: (covered_branches, total_branches)}}
    """
    branch_coverage: BranchCoverageData = {}
    
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for package_elem in root.iter('package'):
            package_name = package_elem.get('name', '')
            
            for source_elem in package_elem.findall('sourcefile'):
                source_file = source_elem.get('name')
                if not source_file:
                    continue
                    
                full_file_path = f"{package_name}/{source_file}" if package_name else source_file
                
                lines: Dict[int, Tuple[int, int]] = {}
                for line in source_elem.findall('line'):
                    line_num = int(line.get('nr', 0))  # Line number
                    mb = int(line.get('mb', 0))       # Uncovered branches count
                    cb = int(line.get('cb', 0))       # Covered branches count
                    total_branches = mb + cb
                    
                    if total_branches > 0:  # Only record lines that have branches that are covered
                        lines[line_num] = (cb, total_branches)
                
                if lines:
                    branch_coverage[full_file_path] = lines
                    
    except Exception as e:
        logger.error(f"Error parsing XML file ({xml_path}): {str(e)}")
        raise
    
    return branch_coverage


def format_branch_coverage_data(branch_coverage_data: BranchCoverageData) -> List[str]:
    """
    Format branch coverage data to a list of strings
    
    Args:
        branch_coverage_data: Branch coverage data {file_path: {line_number: (covered_branches, total_branches)}}
        
    Returns:
        Formatted string of lines, ready for printing or writing to a file
    """
    formatted_lines = []
    
    for file_path in sorted(branch_coverage_data.keys()):
        formatted_lines.append(f"===== File: {file_path} =====\n")
        file_branch_coverage = branch_coverage_data[file_path]
        # Sort lines by line number
        for line_number in sorted(file_branch_coverage.keys()):
            covered_count, total_count = file_branch_coverage[line_number]
            formatted_lines.append(f"Line {line_number}: Covered {covered_count} branches ({total_count} branches)")
        formatted_lines.append("\n")
    
    return formatted_lines