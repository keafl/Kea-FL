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
    d(resourceId="com.ichi2.anki.debug:id/get_started").click()
    time.sleep(1)

# Generate EC file
def gen_ec_file():
    import subprocess
    cmd = "adb shell am broadcast -a com.ichi2.anki.GENERATE_COVERAGE -n com.ichi2.anki.debug/com.ichi2.anki.CoverageReceiver"
    subprocess.run(cmd, shell=True, check=True)

def set_up_runner():
    # Set up the API key
    api_key = None

    # Set up the report output directory
    report_output_dir = os.path.join(r".\report", f"report_{time.strftime('%Y%m%d_%H%M%S')}")
    
    # Set up the configuration
    app_project_base_dir = r"study\app_src\AnkiDroid"
    config = Config(
        app_package="com.ichi2.anki.debug",
        apk_path=os.path.join(app_project_base_dir, r"build\outputs\apk\play\debug\AnkiDroid-play-arm64-v8a-debug.apk"),
        app_source_dir=os.path.join(app_project_base_dir, r"src\main\java"),
        app_classfiles_dir=os.path.join(app_project_base_dir, r"build\tmp\kotlin-classes\playDebug"),
        ec_file_path=r"/storage/emulated/0/Android/data/com.ichi2.anki.debug/files/jacoco_coverage.ec",
        report_output_dir=report_output_dir,
        llm_api_key=api_key,
    )
    runner = Runner(config, init_app, gen_ec_file)
    return runner

if __name__ == "__main__":
    fastbot_log_path = r"study\kea2_reports\anki20279\fastbot_2026053109_4507755884.log"
    step_log_path = r"study\kea2_reports\anki20279\output_2026053109_4507755884\steps.log"

    # Run the analysis
    runner = set_up_runner()
    pair_test_cases = runner.build_pair_test_cases(step_log_path, fastbot_log_path)
    runner.run_full_analysis(pair_test_cases)