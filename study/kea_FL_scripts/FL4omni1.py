import os
import time
from pathlib import Path

from src.kea_FL import Config
from src.kea_FL import WorkflowRunner as Runner

# Initialize Omni-Notes
def init_omni_notes():
    pass

# Generate EC file
def gen_ec_file():
    import subprocess
    cmd = "adb shell am broadcast -a it.feio.android.omninotes.JACOCO -n it.feio.android.omninotes.alpha/it.feio.android.omninotes.JacocoCoverageReceiver"
    subprocess.run(cmd, shell=True, check=True)


def set_up_runner():
    # Set up the API key
    api_key = None

    # Set up the report output directory
    report_output_dir = os.path.join(r".\report", f"report_{time.strftime('%Y%m%d_%H%M%S')}")

    # Set up the configuration
    app_project_base_dir = r"study\app_src\Omni-Notes-1\omniNotes"
    config = Config(
        app_package="it.feio.android.omninotes.alpha",
        apk_path=os.path.join(app_project_base_dir, r"build\outputs\apk\alpha\debug\OmniNotes-alphaDebug-6.3.0.apk"),
        app_source_dir=os.path.join(app_project_base_dir, r"src\main\java"),
        app_classfiles_dir=os.path.join(app_project_base_dir, r"build\intermediates\javac\alphaDebug\classes"),
        ec_file_path=r"/storage/emulated/0/Android/data/it.feio.android.omninotes.alpha/files/jacoco_coverage.ec",
        report_output_dir=report_output_dir,
        llm_api_key=api_key,
    )
    # Set up the runner
    runner = Runner(config, init_omni_notes, gen_ec_file)
    return runner


if __name__ == "__main__":
    # 937
    fastbot_log_path = r"study\kea2_reports\omni937\fastbot_2026041117_0925042850.log"
    step_log_path = r"study\kea2_reports\omni937\output_2026041117_0925042850\steps.log"

    # Run the analysis
    runner = set_up_runner()
    pair_test_cases = runner.build_pair_test_cases(step_log_path, fastbot_log_path)
    runner.run_full_analysis(pair_test_cases)