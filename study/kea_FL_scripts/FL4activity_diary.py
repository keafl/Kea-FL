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


# Generate EC file
def gen_ec_file():
    import subprocess
    cmd = "adb shell am broadcast -a de.rampro.activitydiary.GENERATE_COVERAGE -n de.rampro.activitydiary.debug/de.rampro.activitydiary.CoverageReceiver"
    subprocess.run(cmd, shell=True, check=True)

def set_up_runner():
    # Set up the API key
    api_key = None

    # Set up the report output directory
    report_output_dir = os.path.join(r".\report", f"report_{time.strftime('%Y%m%d_%H%M%S')}")
    
    # Set up the configuration
    app_project_base_dir = r"study\app_src\ActivityDiary\app"
    config = Config(
        app_package="de.rampro.activitydiary.debug",
        apk_path=os.path.join(app_project_base_dir, r"build\outputs\apk\debug\ActivityDiary-1.2.3-dev-debug.apk"),
        app_source_dir=os.path.join(app_project_base_dir, r"src\main\java"),
        app_classfiles_dir=os.path.join(app_project_base_dir, r"build\intermediates\classes\debug"),
        ec_file_path=r"/storage/emulated/0/Android/data/de.rampro.activitydiary.debug/files/jacoco_coverage.ec",
        report_output_dir=report_output_dir,
        llm_api_key=api_key,
    )
    runner = Runner(config, init_app, gen_ec_file)
    return runner

if __name__ == "__main__":
    # 132
    fastbot_log_path = r"study\kea2_reports\diary132\fastbot_2026060109_4211898319.log"
    step_log_path = r"study\kea2_reports\diary132\output_2026060109_4211898319\steps.log"

    # 155
    fastbot_log_path = r"study\kea2_reports\diary155\fastbot_2026060223_4149037366.log"
    step_log_path = r"study\kea2_reports\diary155\output_2026060223_4149037366\steps.log"

    # Run the analysis
    runner = set_up_runner()
    pair_test_cases = runner.build_pair_test_cases(step_log_path, fastbot_log_path)
    runner.run_full_analysis(pair_test_cases)