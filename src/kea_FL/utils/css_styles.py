"""
css_styles.py
"""

def line_css_style() -> str:
    """
    Line coverage CSS style
    
    Returns:
        CSS string
    """
    return """<style>
    :root {
        --github-bg: #ffffff;
        --github-text: #24292f;
        --github-gray-50: #f9fafb;
        --github-gray-100: #f1f2f4;
        --github-gray-200: #e4e7eb;
        --github-gray-300: #d1d5db;
        --github-gray-400: #9ca3af;
        --github-gray-500: #6e7781;
        --github-gray-600: #4d5663;
        --github-gray-700: #374151;
        --github-gray-800: #272e3b;
        
        --line-number-bg: #f6f8fa;
        --line-number-text: #6e7781;
        --line-number-border: #eaecef;
        
        --correct-bg: rgb(218, 251, 225);
        --correct-border: rgb(172, 238, 187);
        --correct-line-number-bg: rgb(172, 238, 187); 
        --correct-line-number-text: #000000;
        
        --bug-bg: rgb(255, 235, 233); 
        --bug-border: rgb(255, 206, 203);           
        --bug-line-number-bg: rgb(255, 206, 203); 
        --bug-line-number-text: #000000;            
        
        --covered-bg: var(--correct-bg);
        --covered-border: var(--correct-border);
        --covered-line-number-bg: var(--correct-line-number-bg);
        --covered-line-number-text: var(--correct-line-number-text);
        
        --sidebar-width: 300px;
        --sidebar-collapsed-width: 0px;
        --border-radius: 6px;
        --transition: all 0.2s ease;
        --code-line-height: 1.5em;
        --line-number-width: 4.5rem;
        --header-height: 60px;
    }

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
        line-height: 1.5;
        color: var(--github-text);
        background-color: var(--github-gray-50);
        display: flex;
        height: 100vh;
        overflow: hidden;
        padding-top: var(--header-height);
    }

    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: var(--header-height);
        background-color: var(--github-bg);
        border-bottom: 1px solid var(--github-gray-200);
        padding: 0 1.5rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        z-index: 100;
    }

    h1 {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--github-gray-800);
        margin-bottom: 0;
    }

    h2 {
        font-size: 1.25rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid var(--github-gray-200);
    }

    p {
        color: var(--github-gray-600);
        margin-bottom: 1rem;
    }

    .sidebar-toggle-btn {
        background-color: var(--github-bg);
        border: 1px solid var(--github-gray-200);
        border-radius: var(--border-radius);
        color: var(--github-gray-700);
        cursor: pointer;
        padding: 0.375rem 0.75rem;
        font-size: 0.875rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        transition: var(--transition);
    }

    .sidebar-toggle-btn:hover {
        background-color: var(--github-gray-50);
        border-color: var(--github-gray-300);
        color: var(--github-gray-800);
    }

    .sidebar {
        width: var(--sidebar-width);
        background-color: var(--github-bg);
        border-right: 1px solid var(--github-gray-200);
        display: flex;
        flex-direction: column;
        height: 100vh;
        transition: var(--transition);
        overflow: hidden;
        z-index: 10;
        position: fixed;
        left: 0;
        top: var(--header-height);
        height: calc(100vh - var(--header-height));
    }

    .sidebar.collapsed {
        width: var(--sidebar-collapsed-width);
        border-right: none;
        opacity: 0;
        visibility: hidden;
        pointer-events: none;
    }

    .sidebar-resizer {
        display: none;
    }

    .sidebar-toggle {
        display: none;
    }

    .file-list-title {
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.75rem 1rem;
        color: var(--github-gray-500);
        text-transform: uppercase;
        letter-spacing: 0.5px;
        border-bottom: 1px solid var(--github-gray-200);
        background-color: var(--github-gray-50);
    }

    .dir-tree {
        list-style: none;
        overflow-y: auto;
        flex: 1;
        padding: 0.5rem 0;
    }

    .dir-item {
        position: relative;
    }

    .dir-header {
        display: flex;
        align-items: center;
        padding: 0.25rem 1rem;
        color: var(--github-gray-700);
        cursor: pointer;
        font-size: 0.875rem;
        transition: var(--transition);
    }

    .dir-header:hover {
        background-color: var(--github-gray-50);
    }

    .dir-toggle {
        width: 1rem;
        height: 1rem;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 0.75rem;
        color: var(--github-gray-500);
        margin-right: 0.5rem;
    }

    .dir-content {
        list-style: none;
        padding-left: 1.5rem;
    }

    .file-item {
        padding: 0;
    }

    .file-link {
        display: flex;
        align-items: center;
        padding: 0.25rem 1rem;
        color: var(--github-gray-700);
        text-decoration: none;
        font-size: 0.875rem;
        transition: var(--transition);
    }

    .file-link::before {
        content: "📄";
        font-size: 0.75rem;
        margin-right: 0.5rem;
        opacity: 0.7;
    }

    .file-link:hover {
        background-color: var(--github-gray-50);
        color: #0969da;
    }

    .file-link.active {
        color: #0969da;
        font-weight: 500;
    }

    .main-content {
        flex: 1;
        overflow-y: auto;
        padding: 1.5rem;
        transition: var(--transition);
        margin-left: var(--sidebar-width);
        height: 100vh;
        background-color: var(--github-gray-50);
        padding-top: 1rem;
    }

    .sidebar.collapsed + .main-content {
        margin-left: var(--sidebar-collapsed-width) !important;
    }

    .file-header {
        background-color: var(--github-bg);
        border: 1px solid var(--github-gray-200);
        border-radius: var(--border-radius);
        padding: 0.75rem 1rem;
        margin-bottom: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        scroll-margin-top: calc(var(--header-height) + 1rem);
    }

    .file-header a {
        color: #0969da;
        text-decoration: none;
        font-size: 0.875rem;
        display: flex;
        align-items: center;
        gap: 0.25rem;
    }

    .file-header a:hover {
        text-decoration: underline;
    }

    .diff-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin-bottom: 2rem;
        min-height: 0;
    }

    @media (max-width: 1024px) {
        .diff-container {
            grid-template-columns: 1fr;
        }
    }

    .diff-panel {
        background-color: var(--github-bg);
        border: 1px solid var(--github-gray-200);
        border-radius: var(--border-radius);
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }

    .panel-header {
        background-color: var(--github-gray-50);
        border-bottom: 1px solid var(--github-gray-200);
        padding: 0.5rem 1rem;
        font-size: 0.875rem;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .panel-header::before {
        content: "";
        width: 0.75rem;
        height: 0.75rem;
        border-radius: 50%;
    }

    .diff-container > .diff-panel:first-child .panel-header::before {
        background-color: var(--bug-border);
    }

    .diff-container > .diff-panel:last-child .panel-header::before {
        background-color: var(--correct-border);
    }

    .code-container {
        font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;
        font-size: 12px;
        line-height: var(--code-line-height);
        overflow-y: auto;
        overflow-x: hidden;
        max-height: 600px;
        flex: 1;
        width: 100%;
        background-color: var(--github-bg);
    }

    .code-line {
        display: grid;
        grid-template-columns: var(--line-number-width) 1fr;
        width: 100%;
        transition: background-color 0.2s ease;
        border-left: 3px solid transparent;
        min-height: var(--code-line-height);
    }

    .line-number {
        width: var(--line-number-width);
        padding: 0 0.75rem;
        text-align: right;
        color: var(--line-number-text);
        user-select: none;
        background-color: var(--line-number-bg);
        border-right: 1px solid var(--line-number-border);
        min-height: var(--code-line-height);
        display: flex;
        align-items: center;
        justify-content: flex-end;
        flex-shrink: 0;
        font-variant-numeric: tabular-nums;
    }

    .correct-line .line-number {
        background-color: var(--correct-line-number-bg);
        color: var(--correct-line-number-text);
        border-right-color: var(--correct-border);
        font-weight: 100;
    }

    .bug-line .line-number {
        background-color: var(--bug-line-number-bg);
        color: var(--bug-line-number-text);
        border-right-color: var(--bug-border);
        font-weight: 100;
    }

    .covered-line .line-number {
        background-color: var(--correct-line-number-bg);
        color: var(--correct-line-number-text);
        border-right-color: var(--correct-border);
        font-weight: 600;
    }

    .code-content {
        flex: 1;
        padding: 0 0.75rem;
        white-space: pre-wrap;
        word-wrap: break-word;
        word-break: break-all;
        min-height: var(--code-line-height);
        display: flex;
        align-items: flex-start;
        padding-top: calc((var(--code-line-height) - 1em) / 2);
        width: 100%;
        color: var(--github-text);
    }

    .correct-line {
        background-color: var(--correct-bg);
        border-left-color: var(--correct-border);
    }

    .bug-line {
        background-color: var(--bug-bg);
        border-left-color: var(--bug-border);
    }

    .covered-line {
        background-color: var(--correct-bg);
        border-left-color: var(--correct-border);
    }

    .context-line .code-content:empty::before {
        content: " ";
    }

    .separator-line {
        background-color: var(--github-gray-50);
        color: var(--github-gray-500);
        text-align: center;
        padding: 0.5rem 0;
        font-style: italic;
        border-top: 1px dashed var(--github-gray-300);
        border-bottom: 1px dashed var(--github-gray-300);
        grid-column: 1 / -1;
    }

    .separator-line .line-number,
    .separator-line .code-content {
        height: auto;
        line-height: 1.5;
    }

    ::-webkit-scrollbar {
        width: 12px;
        height: 12px;
    }

    ::-webkit-scrollbar-track {
        background: transparent;
    }

    ::-webkit-scrollbar-thumb {
        background-color: var(--github-gray-300);
        border-radius: 6px;
        border: 3px solid transparent;
        background-clip: content-box;
    }

    ::-webkit-scrollbar-thumb:hover {
        background-color: var(--github-gray-400);
    }

    @media (max-width: 768px) {
        .sidebar {
            position: fixed;
            z-index: 100;
        }
        
        .main-content {
            margin-left: 0 !important;
            padding: 1rem;
        }
    }

    .context-line {
        background-color: var(--github-bg);
    }
</style>"""


def branch_css_style() -> str:
    """
    branch coverage CSS style
    
    Returns:
        CSS style string
    """
    return """<style>
    :root {
        --github-bg: #ffffff;
        --github-text: #24292f;
        --github-gray-50: #f9fafb;
        --github-gray-100: #f1f2f4;
        --github-gray-200: #e4e7eb;
        --github-gray-300: #d1d5db;
        --github-gray-400: #9ca3af;
        --github-gray-500: #6e7781;
        --github-gray-600: #4d5663;
        --github-gray-700: #374151;
        --github-gray-800: #272e3b;
        
        --line-number-bg: #f6f8fa;
        --line-number-text: #6e7781;
        --line-number-border: #eaecef;
        
        --correct-bg: rgb(218, 251, 225);           
        --correct-border: rgb(172, 238, 187);       
        --correct-line-number-bg: rgb(172, 238, 187); 
        --correct-line-number-text: #000000; 
        
        --bug-bg: rgb(255, 235, 233);               
        --bug-border: rgb(255, 206, 203);           
        --bug-line-number-bg: rgb(255, 206, 203);   
        --bug-line-number-text: #000000; 
        
        --covered-bg: var(--correct-bg);
        --covered-border: var(--correct-border);
        --covered-line-number-bg: var(--correct-line-number-bg);
        --covered-line-number-text: var(--correct-line-number-text);
        
        --sidebar-width: 300px;
        --sidebar-collapsed-width: 0px;
        --border-radius: 6px;
        --transition: all 0.2s ease;
        --code-line-height: 1.5em;
        --line-number-width: 4.5rem;
        --header-height: 60px;
    }

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
        line-height: 1.5;
        color: var(--github-text);
        background-color: var(--github-gray-50);
        display: flex;
        height: 100vh;
        overflow: hidden;
        padding-top: var(--header-height);
    }

    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: var(--header-height);
        background-color: var(--github-bg);
        border-bottom: 1px solid var(--github-gray-200);
        padding: 0 1.5rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        z-index: 100;
    }

    h1 {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--github-gray-800);
        margin-bottom: 0;
    }

    h2 {
        font-size: 1.25rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid var(--github-gray-200);
    }

    p {
        color: var(--github-gray-600);
        margin-bottom: 1rem;
    }

    .sidebar-toggle-btn {
        background-color: var(--github-bg);
        border: 1px solid var(--github-gray-200);
        border-radius: var(--border-radius);
        color: var(--github-gray-700);
        cursor: pointer;
        padding: 0.375rem 0.75rem;
        font-size: 0.875rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        transition: var(--transition);
    }

    .sidebar-toggle-btn:hover {
        background-color: var(--github-gray-50);
        border-color: var(--github-gray-300);
        color: var(--github-gray-800);
    }

    .sidebar {
        width: var(--sidebar-width);
        background-color: var(--github-bg);
        border-right: 1px solid var(--github-gray-200);
        display: flex;
        flex-direction: column;
        height: 100vh;
        transition: var(--transition);
        overflow: hidden;
        z-index: 10;
        position: fixed;
        left: 0;
        top: var(--header-height);
        height: calc(100vh - var(--header-height));
    }

    .sidebar.collapsed {
        width: var(--sidebar-collapsed-width);
        border-right: none;
        opacity: 0;
        visibility: hidden;
        pointer-events: none;
    }

    .sidebar-resizer {
        display: none;
    }


    .sidebar-toggle {
        display: none;
    }

    .file-list-title {
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.75rem 1rem;
        color: var(--github-gray-500);
        text-transform: uppercase;
        letter-spacing: 0.5px;
        border-bottom: 1px solid var(--github-gray-200);
        background-color: var(--github-gray-50);
    }

    .dir-tree {
        list-style: none;
        overflow-y: auto;
        flex: 1;
        padding: 0.5rem 0;
    }

    .dir-item {
        position: relative;
    }

    .dir-header {
        display: flex;
        align-items: center;
        padding: 0.25rem 1rem;
        color: var(--github-gray-700);
        cursor: pointer;
        font-size: 0.875rem;
        transition: var(--transition);
    }

    .dir-header:hover {
        background-color: var(--github-gray-50);
    }

    .dir-toggle {
        width: 1rem;
        height: 1rem;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 0.75rem;
        color: var(--github-gray-500);
        margin-right: 0.5rem;
    }

    .dir-content {
        list-style: none;
        padding-left: 1.5rem;
    }

    .file-item {
        padding: 0;
    }

    .file-link {
        display: flex;
        align-items: center;
        padding: 0.25rem 1rem;
        color: var(--github-gray-700);
        text-decoration: none;
        font-size: 0.875rem;
        transition: var(--transition);
    }

    .file-link::before {
        content: "📄";
        font-size: 0.75rem;
        margin-right: 0.5rem;
        opacity: 0.7;
    }

    .file-link:hover {
        background-color: var(--github-gray-50);
        color: #0969da;
    }

    .file-link.active {
        color: #0969da;
        font-weight: 500;
    }

    .main-content {
        flex: 1;
        overflow-y: auto;
        padding: 1.5rem;
        transition: var(--transition);
        margin-left: var(--sidebar-width);
        height: 100vh;
        background-color: var(--github-gray-50);
        padding-top: 1rem;
    }

    .sidebar.collapsed + .main-content {
        margin-left: var(--sidebar-collapsed-width) !important;
    }

    .file-header {
        background-color: var(--github-bg);
        border: 1px solid var(--github-gray-200);
        border-radius: var(--border-radius);
        padding: 0.75rem 1rem;
        margin-bottom: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        scroll-margin-top: calc(var(--header-height) + 1rem);
    }

    .file-header a {
        color: #0969da;
        text-decoration: none;
        font-size: 0.875rem;
        display: flex;
        align-items: center;
        gap: 0.25rem;
    }

    .file-header a:hover {
        text-decoration: underline;
    }

    .diff-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin-bottom: 2rem;
        min-height: 0;
    }

    @media (max-width: 1024px) {
        .diff-container {
            grid-template-columns: 1fr;
        }
    }

    .diff-panel {
        background-color: var(--github-bg);
        border: 1px solid var(--github-gray-200);
        border-radius: var(--border-radius);
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }

    .panel-header {
        background-color: var(--github-gray-50);
        border-bottom: 1px solid var(--github-gray-200);
        padding: 0.5rem 1rem;
        font-size: 0.875rem;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .panel-header::before {
        content: "";
        width: 0.75rem;
        height: 0.75rem;
        border-radius: 50%;
    }

    .diff-container > .diff-panel:first-child .panel-header::before {
        background-color: var(--bug-border);
    }

    .diff-container > .diff-panel:last-child .panel-header::before {
        background-color: var(--correct-border);
    }

    .code-container {
        font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;
        font-size: 12px;
        line-height: var(--code-line-height);
        overflow-y: auto;
        overflow-x: hidden;
        max-height: 600px;
        flex: 1;
        width: 100%;
        background-color: var(--github-bg);
    }

    .code-line {
        display: grid;
        grid-template-columns: var(--line-number-width) 1fr;
        width: 100%;
        transition: background-color 0.2s ease;
        border-left: 3px solid transparent;
        min-height: var(--code-line-height);
    }

    .line-number {
        width: var(--line-number-width);
        padding: 0 0.75rem;
        text-align: right;
        color: var(--line-number-text);
        user-select: none;
        background-color: var(--line-number-bg);
        border-right: 1px solid var(--line-number-border);
        min-height: var(--code-line-height);
        display: flex;
        align-items: center;
        justify-content: flex-end;
        flex-shrink: 0;
        font-variant-numeric: tabular-nums;
    }

    .correct-line .line-number {
        background-color: var(--correct-line-number-bg);
        color: var(--correct-line-number-text);
        border-right-color: var(--correct-border);
        font-weight: 100;
    }

    .bug-line .line-number {
        background-color: var(--bug-line-number-bg);
        color: var(--bug-line-number-text);
        border-right-color: var(--bug-border);
        font-weight: 100;
    }

    .covered-line .line-number {
        background-color: var(--correct-line-number-bg);
        color: var(--correct-line-number-text);
        border-right-color: var(--correct-border);
        font-weight: 600;
    }

    .code-content {
        flex: 1;
        padding: 0 0.75rem;
        white-space: pre-wrap;
        word-wrap: break-word;
        word-break: break-all;
        min-height: var(--code-line-height);
        display: flex;
        align-items: flex-start;
        padding-top: calc((var(--code-line-height) - 1em) / 2);
        width: 100%;
        color: var(--github-text);
    }

    .correct-line {
        background-color: var(--correct-bg);
        border-left-color: var(--correct-border);
    }

    .bug-line {
        background-color: var(--bug-bg);
        border-left-color: var(--bug-border);
    }

    .covered-line {
        background-color: var(--correct-bg);
        border-left-color: var(--correct-border);
    }

    .context-line .code-content:empty::before {
        content: " ";
    }

    .separator-line {
        background-color: var(--github-gray-50);
        color: var(--github-gray-500);
        text-align: center;
        padding: 0.5rem 0;
        font-style: italic;
        border-top: 1px dashed var(--github-gray-300);
        border-bottom: 1px dashed var(--github-gray-300);
        grid-column: 1 / -1;
    }

    .separator-line .line-number,
    .separator-line .code-content {
        height: auto;
        line-height: 1.5;
    }

    ::-webkit-scrollbar {
        width: 12px;
        height: 12px;
    }

    ::-webkit-scrollbar-track {
        background: transparent;
    }

    ::-webkit-scrollbar-thumb {
        background-color: var(--github-gray-300);
        border-radius: 6px;
        border: 3px solid transparent;
        background-clip: content-box;
    }

    ::-webkit-scrollbar-thumb:hover {
        background-color: var(--github-gray-400);
    }

    @media (max-width: 768px) {
        .sidebar {
            position: fixed;
            z-index: 100;
        }
        
        .main-content {
            margin-left: 0 !important;
            padding: 1rem;
        }
    }

    .context-line {
        background-color: var(--github-bg);
    }
</style>"""

def index_css_style() -> str:
    """
    css style for index.html
    
    Returns:
        css style string
    """
    return """<style>
    :root {
        --primary-color: #4361ee;
        --secondary-color: #3f37c9;
        --success-color: #4cc9f0;
        --warning-color: #f72585;
        --danger-color: #e63946;
        --light-color: #f8f9fa;
        --dark-color: #212529;
        --gray-color: #6c757d;
        --border-color: #dee2e6;
        --card-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        --transition: all 0.3s ease;
    }
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f5f7fb;
    }
    
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    
    .report-header {
        text-align: center;
        margin-bottom: 30px;
        padding: 30px;
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        color: white;
        border-radius: 10px;
        box-shadow: var(--card-shadow);
    }
    
    .report-header h1 {
        font-size: 2.5rem;
        margin-bottom: 10px;
    }
    
    .report-time {
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    h2 {
        color: var(--secondary-color);
        margin: 30px 0 20px 0;
        padding-bottom: 10px;
        border-bottom: 2px solid var(--border-color);
    }
    
    .overview-section {
        margin-bottom: 30px;
    }
    
    .overview-card {
        background: white;
        padding: 25px;
        border-radius: 10px;
        box-shadow: var(--card-shadow);
        text-align: center;
    }
    
    .overview-card p {
        font-size: 1.2rem;
        margin: 10px 0;
    }
    
    .test-cases-section {
        margin-top: 30px;
    }
    
    .test-case-card {
        background: white;
        margin-bottom: 30px;
        padding: 25px;
        border-radius: 10px;
        box-shadow: var(--card-shadow);
        transition: var(--transition);
    }
    
    .test-case-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
    }
    
    .test-case-card h3 {
        color: var(--primary-color);
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 1px solid var(--border-color);
    }
    
    .test-result-group {
        margin-bottom: 20px;
        padding: 15px;
        border-radius: 8px;
        background-color: #f8f9fa;
    }
    
    .test-result-group h4 {
        color: var(--secondary-color);
        margin-bottom: 10px;
    }
    
    .test-result-group p {
        margin: 8px 0;
    }
    
    .status {
        padding: 5px 10px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.9rem;
    }
    
    .status.success {
        background-color: rgba(76, 201, 240, 0.2);
        color: #168aad;
    }
    
    .status.error {
        background-color: rgba(230, 57, 70, 0.2);
        color: #e63946;
    }
    
    .status.unexecuted {
        background-color: rgba(108, 117, 125, 0.2);
        color: #6c757d;
    }
    
    .error-message {
        color: var(--danger-color);
        font-weight: 500;
    }
    
    .report-links {
        display: flex;
        gap: 15px;
        flex-wrap: wrap;
        margin-top: 15px;
    }
    
    .report-link {
        display: inline-block;
        padding: 10px 20px;
        background-color: var(--primary-color);
        color: white;
        text-decoration: none;
        border-radius: 5px;
        transition: var(--transition);
    }
    
    .report-link:hover {
        background-color: var(--secondary-color);
        transform: translateY(-2px);
    }
    
    .back-to-top {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        cursor: pointer;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        z-index: 1000;
        font-size: 1.5rem;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: var(--transition);
    }
    
    .back-to-top:hover {
        background-color: var(--secondary-color);
        transform: translateY(-3px);
    }
    
    @media (max-width: 768px) {
        .container {
            padding: 15px;
        }
        
        .report-header h1 {
            font-size: 2rem;
        }
        
        .report-links {
            flex-direction: column;
        }
        
        .report-link {
            width: 100%;
            text-align: center;
        }
    }
</style>"""