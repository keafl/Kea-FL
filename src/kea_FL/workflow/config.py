"""
config.py
"""
import os
from typing import Optional

from kea_FL.utils.logger import get_logger


class Config:
    """Config class"""

    def __init__(self, app_package: str, 
            apk_path: str,
            app_source_dir: str, 
            app_classfiles_dir: str, 
            ec_file_path: str,
            report_output_dir: str,
            device_serial: Optional[str] = None, 
            adb_path: str = "adb",
            jacococli_jar_path: str = "",
            llm_api_key: Optional[str] = None,
            llm_model: Optional[str] = "deepseek-chat",
            llm_base_url: Optional[str] = "https://api.deepseek.com",
    ):
        """
        Initialize Config class
        
        Args:
            app_package: Application package name
            apk_path: apk file path
            app_source_dir: app source directory
            app_classfiles_dir: app class files directory
            ec_file_path: coverage data file path
            report_output_dir: report output directory
            device_serial: Device serial number
            adb_path: ADB path, default "adb"
            jacococli_jar_path: JaCoCo CLI JAR path, default "" will use default path
            llm_api_key: LLM API key
            llm_model: LLM model, default "deepseek-chat"
            llm_base_url: LLM base URL
        """
        self.app_package = app_package
        self.apk_path = apk_path
        self.app_source_dir = app_source_dir
        self.app_classfiles_dir = app_classfiles_dir
        self.ec_file_path = ec_file_path
        self.report_output_dir = report_output_dir
        self.device_serial = device_serial
        self.adb_path = adb_path
        self.jacococli_jar_path = jacococli_jar_path
        self.llm_api_key = llm_api_key
        self.llm_model = llm_model
        self.llm_base_url = llm_base_url
        self.logger = get_logger("config")

        os.makedirs(self.report_output_dir, exist_ok=True)

        if not self.adb_path:
            self.adb_path = "adb"

        if not self.jacococli_jar_path:
            self._default_jacococli_jar_path()

        self._check_config_validity()

        self.logger.info(f"Config initialized, app_package: {self.app_package}, \
                        APK path: {self.apk_path}, \
                        source directory: {self.app_source_dir}, \
                        class files directory: {self.app_classfiles_dir}, \
                        coverage data file path: {self.ec_file_path}, \
                        report output directory: {self.report_output_dir}, \
                        device serial number: {self.device_serial}, \
                        ADB path: {self.adb_path}, \
                        JaCoCo CLI JAR path: {self.jacococli_jar_path}".replace(" ", "").replace(",", "\n"))


    def _default_jacococli_jar_path(self):
        """
        Default JaCoCo CLI JAR path, use this project's jacococli.jar
        """
        current_file_abs_path = os.path.abspath(__file__)
        src_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file_abs_path)))
        project_root = os.path.dirname(src_root)
        jar_path = os.path.join(project_root, "jacococli.jar")
        if not os.path.exists(jar_path):
            raise FileNotFoundError(f"Jacoco CLI JAR path not found: {jar_path}, please check project root directory contains jacococli.jar")
        self.jacococli_jar_path = jar_path


    def _check_config_validity(self):
        """Check config validity, and paths exist"""
        if not all([self.app_package, self.apk_path, self.app_source_dir, self.app_classfiles_dir]):
            raise ValueError("Config is incomplete, please check app_package, apk_path, app_source_dir, app_classfiles_dir are not None")

        for path in [self.app_source_dir, self.app_classfiles_dir]:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Path not found: {path}")
