
import os
import time
from pathlib import Path

from src.kea_FL import Config
from src.kea_FL import WorkflowRunner as Runner

# Initialize Omni-Notes
def init():
    import time
    import uiautomator2 as u2
    d = u2.connect()
    d(resourceId="net.gsantner.markor_test:id/next", index=1).click()
    time.sleep(1)
    d(resourceId="net.gsantner.markor_test:id/next", index=1).click()
    time.sleep(1)
    d(resourceId="android:id/button1", index=1).click()
    time.sleep(1)
    d(resourceId="com.android.permissioncontroller:id/permission_allow_button", text="Allow").click()
    time.sleep(1)
    d(resourceId="net.gsantner.markor_test:id/next", index=1).click()
    time.sleep(1)
    d(resourceId="net.gsantner.markor_test:id/next", index=1).click()
    time.sleep(1)
    d(resourceId="net.gsantner.markor_test:id/next", index=1).click()
    time.sleep(1)
    d(resourceId="net.gsantner.markor_test:id/done", index=1).click()
    print("init done")
    time.sleep(5)

# Generate EC file
def gen_ec():
    import subprocess
    cmd = "adb shell am broadcast -a net.gsantner.markor.GENERATE_COVERAGE -n net.gsantner.markor_test/net.gsantner.markor.JacocoCoverageReceiver -e extra_file_name \"my_coverage\""
    subprocess.run(cmd, shell=True, check=True)


def set_up_runner():
    # Set up the API key
    api_key = None

    # Set up the report output directory
    report_output_dir = os.path.join(r".\report", f"report_{time.strftime('%Y%m%d_%H%M%S')}")

    # Set up the configuration
    app_project_base_dir = r"study\app_src\markor-1\app"
    config = Config(
        app_package="net.gsantner.markor_test",
        apk_path=os.path.join(app_project_base_dir, r"build\outputs\apk\flavorAtest\debug\net.gsantner.markor-v130-2.8.6-flavorAtest-debug.apk"),
        app_source_dir=os.path.join(app_project_base_dir, r"src\main\java"),
        app_classfiles_dir=os.path.join(app_project_base_dir, r"build\intermediates\javac\flavorAtestDebug\classes"),
        ec_file_path=r"/sdcard/Android/data/net.gsantner.markor_test/files/my_coverage.ec",
        report_output_dir=report_output_dir,
        llm_api_key=api_key,
    )
    runner = Runner(config, init, gen_ec)
    return runner

if __name__ == "__main__":
    # 1652
    fastbot_log_path = r"study\kea2_reports\markor1652\fastbot_2026040918_0649628167.log"
    step_log_path = r"study\kea2_reports\markor1652\output_2026040918_0649628167\steps.log"

    # Run the analysis
    runner = set_up_runner()
    pair_test_cases = runner.build_pair_test_cases(step_log_path, fastbot_log_path)
    runner.run_full_analysis(pair_test_cases)