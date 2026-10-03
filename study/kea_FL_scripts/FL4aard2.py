import os
import time
from pathlib import Path

from src.kea_FL import Config
from src.kea_FL import WorkflowRunner as Runner

# Initialize
def init_app():
    import time 
    import uiautomator2 as u2

    d = u2.connect()
    d(resourceId="itkach.aard2:id/dictionaries_empty_btn_scan", text="Add").click()
    time.sleep(1)
    d(resourceId="android:id/title", text="freedict-bre-fra-0.6.4 (1).slob").click()
    time.sleep(1)


# Generate EC file
def gen_ec_file():
    import subprocess
    cmd = "adb shell am broadcast -a itkach.aard2.GENERATE_COVERAGE -n itkach.aard2/itkach.aard2.CoverageReceiver"
    subprocess.run(cmd, shell=True, check=True)

def set_up_runner():
    # Set up the API key
    api_key = None

    # Set up the report output directory
    report_output_dir = os.path.join(r".\report", f"report_{time.strftime('%Y%m%d_%H%M%S')}")
    
    # Set up the configuration
    app_project_base_dir = r"study\app_src\aard2"
    config = Config(
        app_package="itkach.aard2",
        apk_path=os.path.join(app_project_base_dir, r"build\outputs\apk\debug\aard2-debug.apk"),
        app_source_dir=os.path.join(app_project_base_dir, r"src"),
        app_classfiles_dir=os.path.join(app_project_base_dir, r"build\intermediates\javac\debug\classes"),
        ec_file_path=r"/storage/emulated/0/Android/data/itkach.aard2/files/jacoco_coverage.ec",
        report_output_dir=report_output_dir,
        llm_api_key=api_key,
    )
    runner = Runner(config, init_app, gen_ec_file)
    return runner

if __name__ == "__main__":
    fastbot_log_path = r"study\kea2_reports\aard140\fastbot_2026053116_5032839382.log"
    step_log_path = r"study\kea2_reports\aard140\output_2026053116_5032839382\steps.log"

    # Run the analysis
    runner = set_up_runner()
    pair_test_cases = runner.build_pair_test_cases(step_log_path, fastbot_log_path)
    runner.run_full_analysis(pair_test_cases)