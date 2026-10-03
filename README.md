# Kea-FL

Kea-FL is a automated tool used for analyzing differences in code coverage reports for Fault Localization (FL), designed to identify bug-related coverage changes and help developers more accurately locate Android app defects.

## Table of Contents

- [Related Project](#related-project)
- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Core Module Description](#core-module-description)
- [Usage](#usage)
  - [Prerequisites](#prerequisites)
  - [Running the Analysis](#running-the-analysis)
- [Configuration Parameters](#configuration-parameters)
- [LLM Integration (Optional)](#llm-integration-optional)
- [Study Data](#study-data)
- [License](#license)

## Related Project

**Kea2** is the upstream tool that detects property violations in Android apps and generates the bug reports under `study/kea2_reports/`. Kea-FL builds on these reports to analyze bug-related coverage differences.

- Repository: [https://github.com/ecnusse/Kea2](https://github.com/ecnusse/Kea2)

## Features

- Calculate coverage increments before and after execution
- Analyze coverage differences between paired test cases
- Generate detailed difference analysis reports
- Support line coverage and branch coverage analysis
- Integrate with LLM (Large Language Model) for intelligent file ranking

## Installation

### From Source

This project uses `uv` for package management. First, install `uv`:

```bash
# Install uv (Windows)
powershell -ExecutionPolicy ByPass -c "iwr https://astral.sh/uv/install.ps1 | iex"

# Install uv (Linux/Mac)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then follow these steps to install the project:

```bash
# Clone the project
git clone https://github.com/keafl/Kea-FL.git
cd Kea-FL

# Create virtual environment
uv venv kea_fl

# Activate virtual environment
uv activate kea_fl  # Linux/Mac
# or
kea_fl\Scripts\activate     # Windows

# Install the project
uv pip install -e .
```

### Development Mode Installation (Optional)
If you want to customize Kea-FL, you can install the project in development mode.

```bash
pip install -e ".[dev]"
```

## Project Structure

```
Kea-FL/
├── src/                    # Source code directory
│   └── kea_FL/             # Main source code package
│       ├── core/           # Core functionality modules
│       │   ├── __init__.py
│       │   ├── calculator.py       # Coverage calculation module
│       │   ├── differ.py           # Coverage difference analysis module
│       │   └── parser.py           # Coverage report parsing module
│       ├── utils/          # Utility modules
│       │   ├── __init__.py
│       │   ├── adb_wrapper.py      # ADB operation wrapper
│       │   ├── css_styles.py       # CSS style definitions
│       │   ├── data_types.py       # Data type definitions
│       │   ├── llm.py              # LLM integration for file ranking
│       │   ├── logger.py           # Logging utility
│       │   ├── log_parser.py       # Kea's log parsing module
│       │   ├── replayer.py         # Test case replay module
│       │   ├── report_generator.py # Report generation module
│       │   └── reproducer.py       # Reproduction module
│       ├── workflow/       # Workflow modules
│       │   ├── __init__.py
│       │   ├── config.py           # Configuration management
│       │   └── runner.py           # Workflow executor
│       └── __init__.py
├── study/                  # Experimental data and results
│   ├── app_src/            # Open-source app source code (instrumented with Jacoco)
│   │   └── *.7z            # Compressed source code archives (tracked by Git LFS)
│   ├── kea2_reports/       # Property violation reports detected by Kea2
│   │   └── */              # Bug-specific report directories
│   ├── kea_FL_reports/     # Kea-FL analysis results
│   │   ├── RQ1/            # Research Question 1 results
│   │   └── RQ3/            # Research Question 3 results
│   ├── kea_FL_scripts/     # Per-app run scripts (FL4*.py)
│   ├── LLM_Prompts/        # Per-bug LLM prompts (*.md)
│   ├── RQ1_Results/        # RQ1 aggregated result CSV files
│   ├── RQ2_Results/        # RQ2 per-baseline comparison result CSV files
│   ├── RQ3_results/        # RQ3 ablation experiment result CSV files
│   └── bug_cases.csv       # List of bugs analyzed
├── pyproject.toml          # Project build & dependency configuration
├── uv.lock                 # uv dependency lock file
├── jacococli.jar           # Jacoco CLI tool for parsing .ec files
├── .gitattributes          # Git LFS configuration (for *.7z)
├── .gitignore
├── LICENSE                 # MIT License
└── README.md               # Project documentation
```

## Core Module Description

- **core/calculator.py**: Responsible for calculating code coverage increment information, supporting both line coverage and branch coverage calculation
- **core/differ.py**: Analyzes code coverage differences between different test cases, identifying bug-related coverage changes
- **core/parser.py**: Parses various formats of coverage reports, extracting coverage data
- **utils/report_generator.py**: Generates detailed coverage difference analysis reports, including HTML format visualization reports
- **utils/llm.py**: Integrates with LLM for intelligent file ranking based on suspiciousness
- **workflow/runner.py**: Coordinates the workflow of various modules, providing complete analysis process execution
- **workflow/config.py**: Manages project configuration, including app information, path settings, etc.

## Usage

### Prerequisites

Before using Kea-FL, please ensure the following prerequisites are met:

1. Extract the app source code archives from `study/app_src/*.7z` to a working directory
2. Ensure your phone device (or Android emulator) has developer mode enabled and supports adb debugging
3. Ensure the computer running this project has the necessary environment to run adb commands
4. Place the Jacoco-instrumented APK file and coverage data (.ec) file in accessible locations

### Running the Analysis

You can use Kea-FL by creating a `Config` object with the required parameters and running the workflow. Here's a basic usage example:

```python
from kea_FL.workflow.config import Config
from kea_FL.workflow.runner import run_analysis

# Create configuration
config = Config(
    app_package="com.example.app",
    apk_path="path/to/app.apk",
    app_source_dir="path/to/source/code",
    app_classfiles_dir="path/to/class/files",
    ec_file_path="path/to/coverage.ec",
    report_output_dir="path/to/output"
)

# Run analysis
result = run_analysis(config)
```

After writing your script, use the following command to run the analysis. Remember to replace `file_name` with your actual file name (without the `.py` suffix). This command should be executed in the virtual environment where the project is installed.

```bash
python -m example.file_name
```

You can also check some examples in the `study\kea_FL_scripts\` directory.

## Configuration Parameters

When using Kea-FL as a library, you need to create a `Config` object with various parameters. Here's a comprehensive list of all configuration parameters:

| Parameter | Type | Default Value | Required | Description |
|-----------|------|---------------|----------|-------------|
| `app_package` | str | - | Yes | App package name |
| `apk_path` | str | - | Yes | Path to the APK file |
| `app_source_dir` | str | - | Yes | Path to the app source code directory |
| `app_classfiles_dir` | str | - | Yes | Path to the app class files directory |
| `ec_file_path` | str | - | Yes | Path to the coverage data file (.ec file) |
| `report_output_dir` | str | - | Yes | Directory where analysis reports will be saved |
| `device_serial` | str | None | No | Device serial number (for multiple connected devices) |
| `adb_path` | str | "adb" | No | Path to the ADB executable (default: system path "adb") |
| `jacococli_jar_path` | str | `""` | No | Path to the Jacoco CLI JAR file (default: project's `jacococli.jar`) |
| `llm_api_key` | str | None | No | API key for LLM integration (DeepSeek API) |
| `llm_model` | str | `"deepseek-chat"` | No | LLM model to use (only applicable if `llm_api_key` is provided) |

**Note:** The first six parameters are required and must be provided. The rest are optional with default values.

## LLM Integration (Optional)

Kea-FL integrates with Large Language Models (LLMs) to intelligently rank files based on their suspiciousness of containing bugs. This feature helps developers prioritize their debugging efforts by focusing on the most likely buggy files first.

- Automatically ranks files by suspiciousness after coverage difference analysis
- Uses DeepSeek API for intelligent file ranking
- Optional feature that can be enabled when needed

### Usage Instructions

1. **Obtain a DeepSeek API key** from the DeepSeek official website
2. **Provide LLM parameters** when creating a `Config` object:
   - `llm_api_key`: Your DeepSeek API key
   - `llm_model`: The model to use (default: `"deepseek-chat"`)
3. **Automatic ranking**: The LLM will automatically rank files after the coverage difference analysis

### Disabling LLM Feature

If you don't want to use the LLM feature, simply omit the `llm_api_key` and `llm_model` parameters when creating the `Config` object. The tool will continue to function normally without file ranking.

## Study Data

The `study` directory contains experimental data and results from the Kea-FL research:

### App Source Code
The `study/app_src/` directory contains compressed archives of open-source Android apps instrumented with Jacoco:
- `ActivityDiary.7z`
- `AmazeFileManager.7z`
- `Anki-Android.7z`
- `Omni-Notes-1.7z`, `Omni-Notes-2.7z`
- `aard2.7z`
- `markor-1.7z`, `markor-2.7z`
- `tasks.7z`

### Bug Reports
The `study/kea2_reports/` directory contains property violation reports detected by Kea2 for various bugs:
- `aard140/`, `amaze3991/`, `anki20279/`
- `diary132/`, `diary155/`
- `markor1652/`, `markor1668/`, `markor1695/`, `markor2153/`, `markor2199/`, `markor2250/`
- `omni937/`, `omni938/`, `omni939/`, `omni942/`, `omni945/`, `omni949/`, `omni950/`, `omni951/`, `omni954/`, `omni956/`, `omni981/`
-  `tasks3426/`

### Kea-FL Analysis Results
The `study/kea_FL_reports/` directory contains analysis results generated by Kea-FL, organized by research questions:
- `RQ1/`: Per-bug analysis results for Research Question 1
- `RQ3/`: Per-bug analysis results for Research Question 3

Each research-question directory contains one subdirectory per bug (23 bugs in total). Within each bug directory, results are grouped by the tested method (e.g., `test_search_activity/`, `test_check_recent_file/`), storing the buggy/happy precondition and property coverage data (`.ec`, `.xml`), difference data, and generated reports.

### Run Scripts
The `study/kea_FL_scripts/` directory contains the run scripts that drive the analysis for each app:
- `FL4aard2.py`
- `FL4activity_diary.py`
- `FL4amaze.py`
- `FL4ankiDroid.py`
- `FL4markor1.py`, `FL4markor2.py`
- `FL4omni1.py`, `FL4omni2.py`
- `FL4tasks.py`

### LLM Prompts
The `study/LLM_Prompts/` directory contains the prompt templates sent to the LLM for each bug, one Markdown file per bug (e.g., `aard140.md`, `markor1652.md`, `tasks3426.md`).

### RQ1 Results
The `study/RQ1_Results/` directory contains the aggregated RQ1 results:
- `RQ1_Results.csv`: per-bug file ranking with hit@1 / hit@5 / hit@10 and EXAM metrics
- `running_time.csv`: running time per bug

### RQ2 Results
The `study/RQ2_Results/` directory contains the comparison results against baseline fault-localization methods:
- `BugLocator.csv`
- `Lucene.csv`
- `MopenHands.csv`
- `Ochiai.csv`
- `SentenceBERT.csv`
- `UniXCoder.csv`

### RQ3 Results
The `study/RQ3_results/` directory contains the RQ3 ablation experiment results:
- `RQ3_Without_Coverage_Information_Results.csv`
- `RQ3_Without_Incrementa_Coverage_Results.csv`
- `RQ3_Without_LLM_Ranking_Results.csv`

### Bug Cases
The `study/bug_cases.csv` file contains a list of all bugs analyzed in the study.

## License

This project is licensed under the MIT License. For details, please refer to the [LICENSE](LICENSE) file.