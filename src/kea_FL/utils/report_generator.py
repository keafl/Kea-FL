"""
report_generator.py
"""

import os
from datetime import datetime
from typing import List, Set
import html 

from kea_FL.core.parser import format_line_coverage_data, format_branch_coverage_data
from kea_FL.core.calculator import format_line_coverage_increment_data, format_branch_coverage_increment_data
from kea_FL.core.differ import format_line_diff_result, format_branch_diff_result
from kea_FL.utils.data_types import LineCoverageData, BranchCoverageData, LineCoverageDiff, BranchCoverageDiff, PairAnalysisResult, FullAnalysisResult, HAPPY_PREFIX, BUG_PREFIX
from kea_FL.utils.logger import get_logger
from kea_FL.utils.css_styles import line_css_style, branch_css_style, index_css_style


class ReportGenerator:
    LINE_REPORT_SUFFIX = "_line_diff_report.html"
    BRANCH_REPORT_SUFFIX = "_branch_diff_report.html"
    CODE_CONTAINER_CLASS = "code-container"
    BRANCH_CODE_CONTAINER_CLASS = "branch-code-container"
    
    def __init__(self, source_code_base_path: str = "", context_lines: int = 5):
        """
        initialize report generator
        
        Args:
            source_code_base_path: Source code base path, used to read source code files
            context_lines: Context lines to show before and after the diff
        """
        self.source_code_base_path = source_code_base_path
        self.context_lines = context_lines
        self.logger = get_logger("report_generator")


    def generate_line_coverage_data(self, coverage_data: LineCoverageData, case_name: str, output_dir: str):
        """
        generate line coverage data from raw XML file
        
        Args:
            coverage_data: Line coverage data
            case_name: Test case name
            output_dir: Output directory
        """
        line_coverage_data_path = os.path.join(output_dir, f"{case_name}_line_coverage.md")
        with open(line_coverage_data_path, "w", encoding='utf-8') as f:
            f.write("\n".join(format_line_coverage_data(coverage_data)))
        self.logger.info(f"generate line coverage data: {line_coverage_data_path}")


    def generate_branch_coverage_data(self, coverage_data: BranchCoverageData, case_name: str, output_dir: str):
        """
        generate branch coverage data from raw XML file
        
        Args:
            coverage_data: Branch coverage data
            case_name: Test case name
            output_dir: Output directory
        """
        branch_coverage_data_path = os.path.join(output_dir, f"{case_name}_branch_coverage.md")
        with open(branch_coverage_data_path, "w", encoding='utf-8') as f:
            f.write("\n".join(format_branch_coverage_data(coverage_data)))
        self.logger.info(f"generate branch coverage data: {branch_coverage_data_path}")


    def generate_incremental_data(self, result: PairAnalysisResult, output_dir: str):
        """
        generate incremental coverage data from coverage data
        
        Args:
            result: Coverage comparison result
            output_dir: Output directory
        """
        bug_line_incremental_data_path = os.path.join(output_dir, f"{BUG_PREFIX}{result.case_name}_line_incremental_data.md")
        bug_branch_incremental_data_path = os.path.join(output_dir, f"{BUG_PREFIX}{result.case_name}_branch_incremental_data.md")
        with open(bug_line_incremental_data_path, "w", encoding='utf-8') as f:
            f.write("\n".join(format_line_coverage_increment_data(result.bug_incremental_coverage["line_coverage_incremental"])))
        self.logger.info(f"generate bug line coverage increment data: {bug_line_incremental_data_path}")
        with open(bug_branch_incremental_data_path, "w", encoding='utf-8') as f:
            f.write("\n".join(format_branch_coverage_increment_data(result.bug_incremental_coverage["branch_coverage_incremental"])))
        self.logger.info(f"generate bug branch coverage increment data: {bug_branch_incremental_data_path}")

        correct_line_incremental_data_path = os.path.join(output_dir, f"{HAPPY_PREFIX}{result.case_name}_line_incremental_data.md")
        correct_branch_incremental_data_path = os.path.join(output_dir, f"{HAPPY_PREFIX}{result.case_name}_branch_incremental_data.md")
        with open(correct_line_incremental_data_path, "w", encoding='utf-8') as f:
            f.write("\n".join(format_line_coverage_increment_data(result.correct_incremental_coverage["line_coverage_incremental"])))
        self.logger.info(f"generate correct line coverage increment data: {correct_line_incremental_data_path}")
        with open(correct_branch_incremental_data_path, "w", encoding='utf-8') as f:
            f.write("\n".join(format_branch_coverage_increment_data(result.correct_incremental_coverage["branch_coverage_incremental"])))
        self.logger.info(f"generate correct branch coverage increment data: {correct_branch_incremental_data_path}")


    def generate_diff_data(self, result: PairAnalysisResult, output_dir: str):
        """
        generate diff data from coverage data
        
        Args:
            output_dir: Output directory
            result: Coverage comparison result
        """
        line_diff_data_path = os.path.join(output_dir, f"line_diff_data.md")
        branch_diff_data_path = os.path.join(output_dir, f"branch_diff_data.md")
        with open(line_diff_data_path, "w", encoding='utf-8') as f:
            f.write("\n".join(format_line_diff_result(result.diff_result.line_coverage_diff)))
        self.logger.info(f"generate line diff data: {line_diff_data_path}")
        with open(branch_diff_data_path, "w", encoding='utf-8') as f:
            f.write("\n".join(format_branch_diff_result(result.diff_result.branch_coverage_diff)))
        self.logger.info(f"generate branch diff data: {branch_diff_data_path}")


    def generate_compared_data(self, result: PairAnalysisResult, output_dir: str):
        """
        generate all data from coverage data
        
        Args:
            output_dir: Output directory
            result: Coverage comparison result
        """
        self.generate_incremental_data(result, output_dir)
        self.generate_diff_data(result, output_dir)


    def _get_current_time(self) -> str:
        """
        get current time string
        
        Returns:
            Formatted time string
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def _read_source_file(self, file_path: str) -> List[str]:
        """
        read source file content
        
        Args:
            file_path: Source file path
            
        Returns:
            File content lines list
        """
        encodings = ['utf-8', 'gbk', 'gb2312', 'latin-1']
        
        full_path = os.path.join(self.source_code_base_path, file_path.replace('/', os.sep))
        
        for encoding in encodings:
            try:
                with open(full_path, 'r', encoding=encoding) as f:
                    lines = f.readlines()
                self.logger.info(f"Successfully read source file: {full_path} encoding: {encoding}")
                return lines
            except UnicodeDecodeError:
                continue
            except FileNotFoundError:
                self.logger.error(f"Source file not found: {full_path}")
                # return empty list if file not found
                return [f"// Source file not found: {full_path}"]
        
        # return error list if all encodings failed
        self.logger.error(f"Failed to read source file: {full_path} all encodings tried")
        return [f"// Failed to read source file: {full_path}"]


    def _get_extended_line_range(self, line_numbers: Set[int], max_lines: int, context_lines: int = 5) -> List[tuple]:
        """
        get extended line range, including context lines, and mark separators
        
        Args:
            line_numbers: Line numbers to highlight set
            max_lines: Total lines in the file
            context_lines: Context lines to include
            
        Returns:
            List of line numbers with separator flag
        """
        if not line_numbers:
            return []

        extended_ranges = []
        sorted_lines = sorted(list(line_numbers))
        
        for line_num in sorted_lines:
            # Add context lines to the extended range
            start = max(1, line_num - context_lines)
            end = min(max_lines, line_num + context_lines)
            extended_ranges.append((start, end))
        
        # Merge overlapping ranges
        merged_ranges = []
        if extended_ranges:
            current_start, current_end = extended_ranges[0]
            
            for start, end in extended_ranges[1:]:
                # If ranges overlap or adjacent, merge them
                if start <= current_end + 1:
                    current_end = max(current_end, end)
                else:
                    # Add current range
                    merged_ranges.append((current_start, current_end))
                    current_start, current_end = start, end
            
            # Add last range
            merged_ranges.append((current_start, current_end))
        
        # Generate actual line numbers list, including separators
        result_lines = []
        for i, (start, end) in enumerate(merged_ranges):
            # Add all lines in the range
            for line_num in range(start, end + 1):
                result_lines.append((line_num, False))  # (line number, False)
            
            # If not last range, add separator
            if i < len(merged_ranges) - 1:
                result_lines.append((-1, True))  # (-1, True)
        
        return result_lines


    def _generate_html_header(self, title: str, css_styles: str) -> List[str]:
        """
        generate HTML header content
        
        Args:
            title: Page title
            css_styles: CSS styles
            
        Returns:
            HTML header content lines list
        """
        return [
            '<!DOCTYPE html>',
            '<html>',
            '<head>',
            '<meta charset="UTF-8">',
            f'<title>{title}</title>',
            css_styles,
            '<link rel="preconnect" href="https://fonts.googleapis.com">',
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
            '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Roboto+Mono:wght@400;500&display=swap" rel="stylesheet">',
            '<script>',
            '// Global sidebar toggle function',
            'function toggleSidebar() {',
            '    const sidebar = document.querySelector(".sidebar");',
            '    sidebar.classList.toggle("collapsed");',
            '}',
            '',
            '// Directory expand/collapse function',
            'function toggleDir(dirHeader) {',
            '    const toggle = dirHeader.querySelector(".dir-toggle");',
            '    const content = dirHeader.nextElementSibling;',
            '    ',
            '    if (content.style.display === "none" || content.style.display === "") {',
            '        content.style.display = "block";',
            '        toggle.textContent = "−";',
            '    } else {',
            '        content.style.display = "none";',
            '        toggle.textContent = "+";',
            '    }',
            '}',
            '',
            '// File link click event handler',
            'document.addEventListener(\'DOMContentLoaded\', () => {',
            '    const fileLinks = document.querySelectorAll(\'.file-link\');',
            '    ',
            '    fileLinks.forEach(link => {',
            '        link.addEventListener(\'click\', (e) => {',
            '            e.preventDefault();',
            '            ',
            '            fileLinks.forEach(l => l.classList.remove(\'active\'));',
            '            link.classList.add(\'active\');',
            '            ',
            '            const targetId = link.getAttribute(\'href\');',
            '            const targetElement = document.querySelector(targetId);',
            '            if (targetElement) {',
            '                targetElement.scrollIntoView({',
            '                    behavior: \'smooth\',',
            '                    block: \'start\'',
            '                });',
            '            }',
            '        });',
            '    });',
            '    ',
            '    if (fileLinks.length > 0) {',
            '        fileLinks[0].classList.add(\'active\');',
            '    }',
            '});',
            '</script>',
            '</head>',
            '<body>'
        ]


    def _generate_html_footer(self) -> List[str]:
        """
        generate HTML footer content
        
        Returns:
            HTML footer content lines list
        """
        return [
            '</body>',
            '</html>'
        ]


    def _generate_file_list_html(self, file_paths: List[str]) -> List[str]:
        """
        generate file list HTML content (as sidebar)
        
        Args:
            file_paths: File paths list
            
        Returns:
            File list HTML content lines list
        """
        html_content = []
        if not file_paths:
            return html_content
        
        # build directory tree structure
        dir_tree = {}
        for i, file_path in enumerate(file_paths):
            # split file path by "/"
            parts = file_path.split('/')
            current = dir_tree
            # create directory structure
            for part in parts[:-1]:
                if part not in current:
                    current[part] = {}
                current = current[part]
            # add file name
            current[parts[-1]] = {'__file__': True, 'anchor_id': f"file-{i}"}
        
        # recursive merge consecutive empty directories
        def merge_empty_dirs(tree, path_parts=[]):
            merged_tree = {}
            for name, content in tree.items():
                if isinstance(content, dict) and '__file__' not in content:
                    if len(content) == 1 and '__file__' not in list(content.values())[0]:
                        subname, subcontent = list(content.items())[0]
                        new_name = name + '/' + subname
                        new_content = merge_empty_dirs(subcontent, path_parts + [name, subname])
                        merged_tree[new_name] = new_content
                    else:
                        merged_tree[name] = merge_empty_dirs(content, path_parts + [name])
                else:
                    merged_tree[name] = content
            return merged_tree
        
        # merge consecutive empty directories
        merged_dir_tree = merge_empty_dirs(dir_tree)
        
        # generate directory tree
        def generate_tree_html(tree, prefix=''):
            tree_html = []
            for name, content in sorted(tree.items()):
                if name == '__file__':
                    continue
                    
                if isinstance(content, dict) and '__file__' in content:
                    # handle file
                    tree_html.append(f'<li class="file-item">')
                    tree_html.append(f'  <a href="#{content["anchor_id"]}" class="file-link"><span>{name}</span></a>')
                    tree_html.append('</li>')
                else:
                    # handle directory
                    tree_html.append(f'<li class="dir-item">')
                    tree_html.append(f'  <div class="dir-header" onclick="toggleDir(this)">')
                    tree_html.append(f'    <span class="dir-toggle">−</span>')
                    tree_html.append(f'    <span class="dir-name">{name}</span>')
                    tree_html.append(f'  </div>')
                    tree_html.append(f'  <ul class="dir-content" style="display: block;">')
                    tree_html.extend(generate_tree_html(content, prefix + name + '/'))
                    tree_html.append(f'  </ul>')
                    tree_html.append(f'</li>')
            return tree_html
        
        # generate sidebar HTML content
        html_content.append('<div class="sidebar" id="sidebar">')

        html_content.append('<h3 class="file-list-title">File List</h3>')
        html_content.append('<ul class="dir-tree">')
        html_content.extend(generate_tree_html(merged_dir_tree))
        html_content.append('</ul>')
        html_content.append('</div>')
        return html_content


    def _generate_html_line_diff_content(self, 
                                    file_path: str,
                                    source_lines: List[str],
                                    diff_data: LineCoverageDiff,
                                    anchor_id: str) -> str:
        """
        generate HTML line coverage diff content for a file
        
        Args:
            file_path: File path
            source_lines: Source lines list
            diff_data: Line coverage diff data for a file
            anchor_id: Anchor ID
            
        Returns:
            HTML content lines list
        """
        html_lines = []

        source_file_path = os.path.join(self.source_code_base_path, file_path.replace('/', os.sep))
        
        html_lines.append(f'<div class="file-header" id="{anchor_id}">')
        html_lines.append(f'    File: {file_path}')
        html_lines.append(f'    <a href="file:///{source_file_path}" target="_blank">')
        html_lines.append(f'        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">')
        html_lines.append(f'            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>')
        html_lines.append(f'            <polyline points="14 2 14 8 20 8"></polyline>')
        html_lines.append(f'            <line x1="16" y1="13" x2="8" y2="13"></line>')
        html_lines.append(f'            <line x1="16" y1="17" x2="8" y2="17"></line>')
        html_lines.append(f'            <polyline points="10 9 9 9 8 9"></polyline>')
        html_lines.append(f'        </svg>')
        html_lines.append(f'        Open Source Code')
        html_lines.append(f'    </a>')
        html_lines.append(f'</div>')
        
        html_lines.append('<div class="diff-container">')
        
        # left panel - only in first dataset lines (Bug execution)
        html_lines.append('<div class="diff-panel">')
        html_lines.append('<div class="panel-header">Bug Execution Lines</div>')
        html_lines.append('<div class="code-container">')
        
        if diff_data.only_in_first:
            only_first_lines = set(diff_data.only_in_first.keys())
            extended_lines = self._get_extended_line_range(only_first_lines, len(source_lines), self.context_lines)
            
            for line_num, is_separator in extended_lines:
                if is_separator:
                    html_lines.append('<div class="code-line separator-line"><span class="line-number"></span><span class="code-content">⋮</span></div>')
                else:
                    if 1 <= line_num <= len(source_lines):
                        line_content = html.escape(source_lines[line_num - 1].rstrip('\n\r'))
                        if line_num in only_first_lines:
                            html_lines.append(f'<div class="code-line bug-line"><span class="line-number">{line_num}</span><span class="code-content">{line_content}</span></div>')
                        else:
                            html_lines.append(f'<div class="code-line context-line"><span class="line-number">{line_num}</span><span class="code-content">{line_content}</span></div>')
                    else:
                        html_lines.append(f'<div class="code-line context-line"><span class="line-number">{line_num}</span><span class="code-content">// Line number out of range</span></div>')
        else:
            html_lines.append('<div class="code-line context-line"><span class="line-number"></span><span class="code-content">// No line difference</span></div>')
            
        html_lines.append('</div>')
        html_lines.append('</div>')
        
        # right panel - only in second dataset lines (Correct execution)
        html_lines.append('<div class="diff-panel">')
        html_lines.append('<div class="panel-header">Correct Execution Lines</div>')
        html_lines.append('<div class="code-container">')
        
        if diff_data.only_in_second:
            only_second_lines = set(diff_data.only_in_second.keys())
            extended_lines = self._get_extended_line_range(only_second_lines, len(source_lines), self.context_lines)
            
            for line_num, is_separator in extended_lines:
                if is_separator:
                    html_lines.append('<div class="code-line separator-line"><span class="line-number"></span><span class="code-content">⋮</span></div>')
                else:
                    if 1 <= line_num <= len(source_lines):
                        line_content = html.escape(source_lines[line_num - 1].rstrip('\n\r'))
                        if line_num in only_second_lines:
                            html_lines.append(f'<div class="code-line correct-line"><span class="line-number">{line_num}</span><span class="code-content">{line_content}</span></div>')
                        else:
                            html_lines.append(f'<div class="code-line context-line"><span class="line-number">{line_num}</span><span class="code-content">{line_content}</span></div>')
                    else:
                        html_lines.append(f'<div class="code-line context-line"><span class="line-number">{line_num}</span><span class="code-content">// Line number out of range</span></div>')
        else:
            html_lines.append('<div class="code-line context-line"><span class="line-number"></span><span class="code-content">// No line difference</span></div>')
            
        html_lines.append('</div>')
        html_lines.append('</div>')     
        html_lines.append('</div>')

        return '\n'.join(html_lines)


    def _generate_html_branch_diff_content(self, 
                                    file_path: str,
                                    source_lines: List[str],
                                    diff_data: BranchCoverageDiff,
                                    anchor_id: str) -> str:
        """
        generate HTML content for branch coverage diff
        
        Args:
            file_path: file path
            source_lines: source code lines
            diff_data: branch coverage diff data
            anchor_id: anchor id
            
        Returns:
            HTML content
        """
        html_lines = []
        
        source_file_path = os.path.join(self.source_code_base_path, file_path.replace('/', os.sep))
        
        html_lines.append(f'<div class="file-header" id="{anchor_id}">')
        html_lines.append(f'    File: {file_path}')
        html_lines.append(f'    <a href="file:///{source_file_path}" target="_blank">')
        html_lines.append(f'        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">')
        html_lines.append(f'            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>')
        html_lines.append(f'            <polyline points="14 2 14 8 20 8"></polyline>')
        html_lines.append(f'            <line x1="16" y1="13" x2="8" y2="13"></line>')
        html_lines.append(f'            <line x1="16" y1="17" x2="8" y2="17"></line>')
        html_lines.append(f'            <polyline points="10 9 9 9 8 9"></polyline>')
        html_lines.append(f'        </svg>')
        html_lines.append(f'        Open Source Code')
        html_lines.append(f'    </a>')
        html_lines.append(f'</div>')
        
        html_lines.append('<div class="diff-container">')
        
        # left panel - only in first dataset lines (Bug execution)
        html_lines.append('<div class="diff-panel">')
        html_lines.append('<div class="panel-header">Bug Execution Lines</div>')
        html_lines.append('<div class="code-container">')
        
        if diff_data.only_in_first:
            only_first_lines = set(diff_data.only_in_first.keys())
            extended_lines = self._get_extended_line_range(only_first_lines, len(source_lines), self.context_lines)
            
            for line_num, is_separator in extended_lines:
                if is_separator:
                    html_lines.append('<div class="code-line separator-line"><span class="line-number"></span><span class="code-content">⋮</span></div>')
                else:
                    if 1 <= line_num <= len(source_lines):
                        line_content = html.escape(source_lines[line_num - 1].rstrip('\n\r'))
                        if line_num in only_first_lines:
                            covered, total = diff_data.only_in_first[line_num]
                            full_content = f'{line_content} // Branch: Covered {covered}/{total}'
                            html_lines.append(f'<div class="code-line bug-line"><span class="line-number">{line_num}</span><span class="code-content">{full_content}</span></div>')
                        else:
                            html_lines.append(f'<div class="code-line context-line"><span class="line-number">{line_num}</span><span class="code-content">{line_content}</span></div>')
                    else:
                        html_lines.append(f'<div class="code-line context-line"><span class="line-number">{line_num}</span><span class="code-content">// Line number out of range</span></div>')
        else:
            html_lines.append('<div class="code-line context-line"><span class="line-number"></span><span class="code-content">// No line difference</span></div>')
            
        html_lines.append('</div>')
        html_lines.append('</div>')
        
        # right panel - only in second dataset lines (Correct execution)
        html_lines.append('<div class="diff-panel">')
        html_lines.append('<div class="panel-header">Correct Execution Lines</div>')
        html_lines.append('<div class="code-container">')
        
        if diff_data.only_in_second:
            only_second_lines = set(diff_data.only_in_second.keys())
            extended_lines = self._get_extended_line_range(only_second_lines, len(source_lines), self.context_lines)
            
            for line_num, is_separator in extended_lines:
                if is_separator:
                    html_lines.append('<div class="code-line separator-line"><span class="line-number"></span><span class="code-content">⋮</span></div>')
                else:
                    if 1 <= line_num <= len(source_lines):
                        line_content = html.escape(source_lines[line_num - 1].rstrip('\n\r'))
                        if line_num in only_second_lines:
                            covered, total = diff_data.only_in_second[line_num]
                            full_content = f'{line_content} // Branch: Covered {covered}/{total}'
                            html_lines.append(f'<div class="code-line correct-line"><span class="line-number">{line_num}</span><span class="code-content">{full_content}</span></div>')
                        else:
                            html_lines.append(f'<div class="code-line context-line"><span class="line-number">{line_num}</span><span class="code-content">{line_content}</span></div>')
                    else:
                        html_lines.append(f'<div class="code-line context-line"><span class="line-number">{line_num}</span><span class="code-content">// Line number out of range</span></div>')
        else:
            html_lines.append('<div class="code-line context-line"><span class="line-number"></span><span class="code-content">// No line difference</span></div>')
            
        html_lines.append('</div>')
        html_lines.append('</div>')
        html_lines.append('</div>')
        
        return '\n'.join(html_lines)


    def generate_line_diff_report(self, result: PairAnalysisResult, output_dir: str) -> str:
        """
        generate line coverage diff report
        
        Args:
            result: Coverage comparison result
            output_dir: Output directory for the report
        
        Returns:
            str: Path to the generated HTML report file
        """
        html_report_path = os.path.join(output_dir, f"{result.case_name}{self.LINE_REPORT_SUFFIX}")
        
        file_paths = []
        if result.diff_result.line_coverage_diff:
            file_paths = list(result.diff_result.line_coverage_diff.keys())
        
        html_content = self._generate_html_header(
            f"{result.case_name} Line Coverage Diff Report",
            line_css_style()
        )
        
        html_content.append('<!-- Fixed Navigation Bar -->')
        html_content.append('<div class="fixed-header">')
        html_content.append(f'    <h1>{result.case_name} Line Coverage Diff Report</h1>')
        html_content.append('    <button class="sidebar-toggle-btn" onclick="toggleSidebar()">')
        html_content.append('        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">')
        html_content.append('            <line x1="3" y1="12" x2="21" y2="12"></line>')
        html_content.append('            <line x1="3" y1="6" x2="21" y2="6"></line>')
        html_content.append('            <line x1="3" y1="18" x2="21" y2="18"></line>')
        html_content.append('        </svg>')
        html_content.append('        File List')
        html_content.append('    </button>')
        html_content.append('</div>')
        
        html_content.extend(self._generate_file_list_html(file_paths))
        
        html_content.append('<div class="main-content">')
        html_content.append(f'<p>Generated Time: {self._get_current_time()}</p>')
        
        if result.diff_result.line_coverage_diff:
            html_content.append('<h2>Line Coverage Diff</h2>')
            
            for i, (file_path, diff_data) in enumerate(result.diff_result.line_coverage_diff.items()):
                source_lines = self._read_source_file(file_path)
                
                anchor_id = f"file-{i}"
                file_diff_html = self._generate_html_line_diff_content(file_path, source_lines, diff_data, anchor_id)
                html_content.append(file_diff_html)
        
        html_content.append('</div>')
        html_content.extend(self._generate_html_footer())
        
        with open(html_report_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(html_content))
        
        self.logger.info(f"Line Coverage Diff Report Generated: {html_report_path}")
        return html_report_path


    def generate_branch_diff_report(self, result: PairAnalysisResult, output_dir: str) -> str:
        """
        generate branch coverage diff report
        
        Args:
            result: Coverage comparison result
            output_dir: Output directory for the report
        
        Returns:
            str: Path to the generated HTML report file
        """
        html_report_path = os.path.join(output_dir, f"{result.case_name}{self.BRANCH_REPORT_SUFFIX}")
        
        file_paths = []
        if result.diff_result.branch_coverage_diff:
            file_paths = list(result.diff_result.branch_coverage_diff.keys())
        
        html_content = self._generate_html_header(
            f"{result.case_name} Branch Coverage Diff Report",
            branch_css_style()
        )
        html_content.append('<!-- Fixed Navigation Bar -->')
        html_content.append('<div class="fixed-header">')
        html_content.append(f'    <h1>{result.case_name} Branch Coverage Diff Report</h1>')
        html_content.append('    <button class="sidebar-toggle-btn" onclick="toggleSidebar()">')
        html_content.append('        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">')
        html_content.append('            <line x1="3" y1="12" x2="21" y2="12"></line>')
        html_content.append('            <line x1="3" y1="6" x2="21" y2="6"></line>')
        html_content.append('            <line x1="3" y1="18" x2="21" y2="18"></line>')
        html_content.append('        </svg>')
        html_content.append('        File List')
        html_content.append('    </button>')
        html_content.append('</div>')
        
        html_content.extend(self._generate_file_list_html(file_paths))
        
        html_content.append('<div class="main-content">')
        html_content.append(f'<p>Generated Time: {self._get_current_time()}</p>')

        if result.diff_result.branch_coverage_diff:
            html_content.append('<h2>Branch Coverage Diff</h2>')
            
            for i, (file_path, diff_data) in enumerate(result.diff_result.branch_coverage_diff.items()):
                source_lines = self._read_source_file(file_path)
                
                anchor_id = f"file-{i}"
                file_diff_html = self._generate_html_branch_diff_content(file_path, source_lines, diff_data, anchor_id)
                html_content.append(file_diff_html)
        
        html_content.append('</div>')
        html_content.extend(self._generate_html_footer())
        
        with open(html_report_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(html_content))
        
        self.logger.info(f"Branch Coverage Diff Report Generated: {html_report_path}")
        return html_report_path


    def generate_diff_report(self, result: PairAnalysisResult, output_dir: str) -> tuple[str, str]:
        """
        generate diff report
        
        Args:
            result: Coverage comparison result
            output_dir: Output directory for the report
            
        Returns:
            tuple[str, str]: Line coverage diff report path, branch coverage diff report path
        """
        # generate line coverage diff report
        line_report_path = self.generate_line_diff_report(result, output_dir)
        # generate branch coverage diff report
        branch_report_path = self.generate_branch_diff_report(result, output_dir)
        return line_report_path, branch_report_path


    def generate_comprehensive_report(self, full_result: FullAnalysisResult, reproducer_data: dict, output_dir: str) -> None:
        """
        generate comprehensive report
        
        Args:
            full_result: Full analysis result
            reproducer_data: Reproducer data
            output_dir: Output directory for the report
        """
        report_path = os.path.join(output_dir, "index.html")
        
        css_styles = index_css_style()
        html_content = self._generate_html_header("Comprehensive Coverage Diff Report Generated", css_styles)
        
        html_content.append('<div class="container">')
        html_content.append('<header class="report-header">')
        html_content.append('<h1>Comprehensive Coverage Diff Report Generated</h1>')
        html_content.append(f'<p class="report-time">Generated Time: {self._get_current_time()}</p>')
        html_content.append('</header>')
        
        html_content.append('<section class="overview-section">')
        html_content.append('<h2>Analysis Overview</h2>')
        html_content.append(f'<div class="overview-card">')
        html_content.append(f'<p>Total Analyzed <strong>{len(full_result.pair_results)}</strong> Test Cases</p>')
        html_content.append('</div>')
        html_content.append('</section>')
        
        html_content.append('<section class="test-cases-section">')
        html_content.append('<h2>Test Cases List</h2>')
        
        for pair_result in full_result.pair_results:
            case_name = pair_result.case_name
            bug_result_data = reproducer_data[f"{BUG_PREFIX}{case_name}"]
            correct_result_data = reproducer_data[f"{HAPPY_PREFIX}{case_name}"]
            line_diff_report_path = pair_result.line_diff_report_path
            branch_diff_report_path = pair_result.branch_diff_report_path
            
            html_content.append(f'<div class="test-case-card">')
            html_content.append(f'<h3>{pair_result.case_name}</h3>')
            
            html_content.append('<div class="test-result-group">')
            html_content.append('<h4>Bug Test Case: Precondition Execution Result</h4>')
            html_content.append(f'<p>Status: <span class="status {bug_result_data.precondition_result.status.value.lower()}">{bug_result_data.precondition_result.status.value}</span></p>')
            html_content.append(f'<p>Execution Time: {bug_result_data.precondition_result.execution_time:.2f} seconds</p>')
            html_content.append(f'<p>Timestamp: {bug_result_data.precondition_result.timestamp}</p>')
            if bug_result_data.precondition_result.error_message:
                html_content.append(f'<p class="error-message">Error Message: {bug_result_data.precondition_result.error_message}</p>')
            html_content.append('</div>')

            html_content.append('<div class="test-result-group">')
            html_content.append('<h4>Bug Test Case: Property Execution Result</h4>')
            html_content.append(f'<p>Status: <span class="status {bug_result_data.property_result.status.value.lower()}">{bug_result_data.property_result.status.value}</span></p>')
            html_content.append(f'<p>Execution Time: {bug_result_data.property_result.execution_time:.2f} seconds</p>')
            html_content.append(f'<p>Timestamp: {bug_result_data.property_result.timestamp}</p>')
            if bug_result_data.property_result.error_message:
                html_content.append(f'<p class="error-message">Error Message: {bug_result_data.property_result.error_message}</p>')
            html_content.append('</div>')
            

            html_content.append('<div class="test-result-group">')
            html_content.append('<h4>Correct Test Case: Precondition Execution Result</h4>')
            html_content.append(f'<p>Status: <span class="status {correct_result_data.precondition_result.status.value.lower()}">{correct_result_data.precondition_result.status.value}</span></p>')
            html_content.append(f'<p>Execution Time: {correct_result_data.precondition_result.execution_time:.2f} seconds</p>')
            html_content.append(f'<p>Timestamp: {correct_result_data.precondition_result.timestamp}</p>')
            if correct_result_data.precondition_result.error_message:
                html_content.append(f'<p class="error-message">Error Message: {correct_result_data.precondition_result.error_message}</p>')
            html_content.append('</div>')

            html_content.append('<div class="test-result-group">')
            html_content.append('<h4>Correct Test Case: Property Execution Result</h4>')
            html_content.append(f'<p>Status: <span class="status {correct_result_data.property_result.status.value.lower()}">{correct_result_data.property_result.status.value}</span></p>')
            html_content.append(f'<p>Execution Time: {correct_result_data.property_result.execution_time:.2f} seconds</p>')
            html_content.append(f'<p>Timestamp: {correct_result_data.property_result.timestamp}</p>')
            if correct_result_data.property_result.error_message:
                html_content.append(f'<p class="error-message">Error Message: {correct_result_data.property_result.error_message}</p>')
            html_content.append('</div>')
            
            html_content.append('<div class="report-links">')
            html_content.append(f'<a href="{os.path.relpath(line_diff_report_path, output_dir)}" target="_blank" class="report-link">Line Coverage Difference Report</a>')
            html_content.append(f'<a href="{os.path.relpath(branch_diff_report_path, output_dir)}" target="_blank" class="report-link">Branch Coverage Difference Report</a>')
            html_content.append('</div>')
            
            html_content.append('</div>')
        
        html_content.append('</section>')
        html_content.append('</div>')
        
        html_content.extend(self._generate_html_footer())
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(html_content))
        
        self.logger.info(f"Generated comprehensive analysis report: {report_path}")
