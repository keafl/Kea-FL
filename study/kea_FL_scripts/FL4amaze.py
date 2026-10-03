import os
import time
from pathlib import Path

from src.kea_FL import Config
from src.kea_FL import WorkflowRunner as Runner

# Initialize Omni-Notes
def init_app():
    import time 
    import uiautomator2 as u2

    d = u2.connect()
    d(resourceId="com.android.permissioncontroller:id/permission_allow_button", text="Allow").click()

# Generate EC file
def gen_ec_file():
    import subprocess
    cmd = "adb shell am broadcast -a com.amaze.filemanager.GENERATE_COVERAGE -n com.amaze.filemanager.debug/com.amaze.filemanager.CoverageReceiver"
    subprocess.run(cmd, shell=True, check=True)

def set_up_runner():
    # Set up the API key
    api_key = None

    # Set up the report output directory
    report_output_dir = os.path.join(r".\report", f"report_{time.strftime('%Y%m%d_%H%M%S')}")
    
    # Set up the configuration
    app_project_base_dir = r"study\app_src\AmazeFileManager\app"
    config = Config(
        app_package="com.amaze.filemanager.debug",
        apk_path=os.path.join(app_project_base_dir, r"build\outputs\apk\fdroid\debug\app-fdroid-debug.apk"),
        app_source_dir=os.path.join(app_project_base_dir, r"src\main\java"),
        app_classfiles_dir=os.path.join(app_project_base_dir, r"build\intermediates\javac\fdroidDebug\classes"),
        ec_file_path=r"/storage/emulated/0/Android/data/com.amaze.filemanager.debug/files/jacoco_coverage.ec",
        report_output_dir=report_output_dir,
        llm_api_key=api_key,
    )
    runner = Runner(config, init_app, gen_ec_file)
    return runner

if __name__ == "__main__":
    fastbot_log_path = r"study\kea2_reports\amaze3991\fastbot_2026040917_1955562784.log"
    step_log_path = r"study\kea2_reports\amaze3991\output_2026040917_1955562784\steps.log"

    # Run the analysis
    runner = set_up_runner()
    pair_test_cases = runner.build_pair_test_cases(step_log_path, fastbot_log_path)
    runner.run_full_analysis(pair_test_cases)