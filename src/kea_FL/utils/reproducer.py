"""
reproducer.py
"""

import os
import time
from typing import Optional, Callable

from .adb_wrapper import AdbWrapper, AdbError
from .logger import get_logger
from .data_types import TestCase, TestResult, TestStatus, TestData, CoverageData, PairTestCase
from .replayer import Replayer


class Reproducer:
    """Reproducer class"""
    
    def __init__(self, adb: AdbWrapper, app_package: str, apk_path: str, device_serial: Optional[str] = None):
        """
        Initialize Reproducer class
        
        Args:
            adb: AdbWrapper instance
            app_package: Application package name
            device_serial: Device serial number
        """
        self.adb = adb
        self.app_package = app_package
        self.apk_path = apk_path
        self.device_serial = device_serial
        self.data = dict[str, TestData]()  # store all test data, key is test case name
        self.replayer = Replayer(self.app_package, self.device_serial)
        self.logger = get_logger("reproducer")


    def add_test_case(self, test_case: TestCase) -> None:
        """
        Add test case to Reproducer class
        
        Args:
            test_case: TestCase object
        """
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.data[test_case.name] = TestData(test_case,
                                            TestResult(TestStatus.UNEXECUTED, None, 0.0, timestamp),
                                            TestResult(TestStatus.UNEXECUTED, None, 0.0, timestamp),
                                            CoverageData("", ""),
                                            CoverageData("", ""))


    def setup_test_environment(self, init_operation: Callable):
        """
        Set test environment
        """
        try:
            # uninstall app if it is installed on device
            list_installed_packages = self.adb.list_installed_packages(self.device_serial)
            if self.app_package in list_installed_packages:
                self.adb.clear_app_data(self.app_package, self.device_serial)
                self.adb.uninstall_app(self.app_package, self.device_serial)

            # install app on device
            self.adb.install_app(self.apk_path, self.device_serial)
            
            # launch app
            self.adb.launch_app(self.app_package, self.device_serial)
            
            # execute init operation after app launches
            self.logger.info("Execute init operation after app launches")
            init_operation()
            self.logger.info("Init operation executed")

            # wait for app to launch
            time.sleep(3)
            self.logger.info("Test environment setup completed")

            return True
        except AdbError as e:
            self.logger.error(f"Test environment setup failed: {e}")
            raise AdbError(f"Test environment setup failed: {e}")


    def reset_environment(self):
        """
        Reset test environment
        """
        try:
            # force stop app
            self.adb.shutdown_app(self.app_package, self.device_serial)
            
            # clear app data
            self.adb.clear_app_data(self.app_package, self.device_serial)

            self.logger.info("Test environment reset completed")
        except AdbError as e:
            self.logger.error(f"Test environment reset failed: {e}")
            raise AdbError(f"Test environment reset failed: {e}")


    def execute_test_case(self,
                        test_case: TestCase, 
                        output_dir: str,
                        ec_file_generator: Callable,
                        ec_file_path: str,
                        jacococli_jar_path: str, 
                        app_classfiles_path: str, 
                        app_source_path: str,
    ) -> None:
        """
        Execute single test case
        
        Args:
            test_case: TestCase object
            output_dir: Output directory
            ec_file_generator: Coverage data generator function
            ec_file_path: Coverage data file path
            jacococli_jar_path: JaCoCo CLI JAR path
            app_classfiles_path: app compiled class files path
            app_source_path: app source code path

        Returns:
            TestResult object
        """
        start_time = time.time()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        precondition_status = TestStatus.SUCCESS
        precondition_error_message = None

        property_status = TestStatus.SUCCESS
        property_error_message = None

        try:
            # execute preconditions
            self.logger.info(f"Start executing preconditions for test case: {test_case.name}")
            self.replayer.execute_events(test_case.preconditions)
            self.logger.info(f"Preconditions executed for test case: {test_case.name}")

        except Exception as e:
            precondition_status = TestStatus.ERROR
            precondition_error_message = str(e)
        finally:
            # collect coverage data for preconditions
            self.logger.info(f"Start collecting coverage data for preconditions of test case: {test_case.name}")
            precondition_output_dir = os.path.join(output_dir, f"{test_case.name}_precondition")
            os.makedirs(precondition_output_dir, exist_ok=True)
            precondition_coverage_data =  self.collect_coverage_data(ec_file_generator,
                                                                    ec_file_path,
                                                                    precondition_output_dir,
                                                                    jacococli_jar_path, 
                                                                    app_classfiles_path, 
                                                                    app_source_path,
                                                                    test_case.name)
            self.data[test_case.name].precondition_coverage_data = precondition_coverage_data
            # record preconditions execution result
            precondition_result = TestResult(
                status=precondition_status,
                error_message=precondition_error_message if precondition_status == TestStatus.ERROR else None,
                execution_time=time.time() - start_time,
                timestamp=timestamp
            )
            self.data[test_case.name].precondition_result = precondition_result

        try:
            # execute property
            self.logger.info(f"Start executing property for test case: {test_case.name}")
            self.replayer.execute_events(test_case.property)
            self.logger.info(f"Property executed for test case: {test_case.name}")
        except Exception as e:
            property_status = TestStatus.ERROR
            property_error_message = str(e)
        finally:
            # collect coverage data for property
            self.logger.info(f"Start collecting coverage data for property of test case: {test_case.name}")
            property_output_dir = os.path.join(output_dir, f"{test_case.name}_property")
            os.makedirs(property_output_dir, exist_ok=True)
            property_coverage_data =  self.collect_coverage_data(ec_file_generator,
                                                                ec_file_path,
                                                                property_output_dir,
                                                                jacococli_jar_path, 
                                                                app_classfiles_path, 
                                                                app_source_path,
                                                                test_case.name)
            self.data[test_case.name].property_coverage_data = property_coverage_data
            # record property execution result
            property_result = TestResult(
                status=property_status,
                error_message=property_error_message if property_status == TestStatus.ERROR else None,
                execution_time=time.time() - start_time,
                timestamp=timestamp
            )
            self.data[test_case.name].property_result = property_result


    def collect_coverage_data(self,
                            ec_file_generator: Callable,
                            ec_file_path: str,
                            output_dir: str,
                            jacococli_jar_path: str, 
                            app_classfiles_path: str, 
                            app_source_path: str,
                            test_case_name: str,
    ) -> CoverageData:
        """
        Collect JaCoCo coverage data
        
        Args:
            ec_file_generator: Coverage data generator function
            ec_file_path: Coverage file path on device
            output_dir: Output directory for coverage data
            jacococli_jar_path: JaCoCo CLI JAR path
            app_classfiles_path: app compiled class files path
            app_source_path: app source code path
            test_case_name: Test case name
            
        Returns:
            Coverage data object
        """
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        ec_file_type = ec_file_path.split(".")[-1]
        output_file_path = f"{output_dir}/{test_case_name}.{ec_file_type}"
        
        try:
            # generate coverage file
            self.logger.info(f"Start generating coverage file operation")
            ec_file_generator()
            self.logger.info(f"Complete generating coverage file operation")

            # pull coverage file from device
            self.adb.pull_file(ec_file_path, output_file_path, self.device_serial)

            # convert .ec file to XML format
            self.convert_ec_to_xml(output_file_path, output_file_path.replace(f".{ec_file_type}", ".xml"),
                                jacococli_jar_path, app_classfiles_path, app_source_path)
            
            coverage_data = CoverageData(
                xml_path=output_file_path.replace(f".{ec_file_type}", ".xml"),
                timestamp=timestamp
            )
            
            self.logger.info(f"Coverage data collected: {coverage_data.xml_path}")
            return coverage_data
            
        except AdbError as e:
            self.logger.error(f"Failed to collect coverage data for test case: {test_case_name} with error: {e}")
            raise


    def convert_ec_to_xml(self, ec_file_path: str, 
                        xml_path: str, 
                        jacococli_jar_path: str, 
                        app_classfiles_path: str, 
                        app_source_path: str
    ) -> None:
        """
        Convert JaCoCo coverage file to XML format
        
        Args:
            ec_file_path: .ec file path
            xml_path: Output XML file path
            jacococli_jar_path: JaCoCo CLI JAR path
            app_classfiles_path: app compiled class files path
            app_source_path: app source code path
        """
        import shutil
        import subprocess

        if not os.path.exists(ec_file_path):
            raise FileNotFoundError(f"Input file not found: {ec_file_path}")

        if not shutil.which("java"):
            raise EnvironmentError("Java environment not found, please ensure Java is installed and PATH is configured")
        
        output_dir = os.path.dirname(xml_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        cmd = [
            "java", "-jar", jacococli_jar_path, "report", ec_file_path,
            "--classfiles", app_classfiles_path,
            "--sourcefiles", app_source_path,
            "--xml", xml_path
        ]
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode != 0:
                error_msg = f"JaCoCo conversion failed with error: {result.stderr}"
                self._create_placeholder_xml(xml_path, error_msg)
                raise RuntimeError(error_msg)
                
            self.logger.info(f"JaCoCo conversion command: {' '.join(cmd)}")
            self.logger.info(f"JaCoCo conversion output: {result.stdout}")
            self.logger.info(f"Coverage file converted successfully: {ec_file_path} -> {xml_path}")
            
        except subprocess.TimeoutExpired:
            raise RuntimeError("JaCoCo conversion timeout after 120 seconds")
        except Exception as e:
            self._create_placeholder_xml(xml_path, str(e))
            raise RuntimeError(f"JaCoCo conversion failed with error: {str(e)}")


    def _create_placeholder_xml(self, xml_path: str, error_message: str) -> None:
        """
        Create placeholder XML file for failed conversion
        
        Args:
            xml_path: XML file path
            error_message: Error message
        """
        try:
            with open(xml_path, 'w', encoding='utf-8') as f:
                f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
                f.write('<!DOCTYPE report PUBLIC "-//JACOCO//DTD Report 1.1//EN" "report.dtd">\n')
                f.write('<report name="Coverage Report">\n')
                f.write(f'  <sessioninfo id="placeholder-error" start="0" dump="0">\n')
                f.write(f'    <error>{error_message}</error>\n')
                f.write(f'  </sessioninfo>\n')
                f.write('</report>\n')
        except Exception:
            pass


    def reproduce_test_case(self, 
                        test_case: TestCase, 
                        output_dir: str,
                        ec_file_generator: Callable,
                        ec_file_path: str,
                        jacococli_jar_path: str, 
                        app_classfiles_path: str, 
                        app_source_path: str,
                        init_operation: Callable,
    ) -> TestData:
        """
        Reproduce specific test case and collect coverage data
        
        Args:
            test_case: Test case
            
        Returns:
            Test result
        """
        self.logger.info(f"Start reproducing test case: {test_case.name}")
        self.replayer.connect_device()
        
        if not self.setup_test_environment(init_operation):
            raise Exception("Failed to setup test environment")
        
        try:
            self.add_test_case(test_case)
            self.execute_test_case(test_case,
                                    output_dir,
                                    ec_file_generator,
                                    ec_file_path,
                                    jacococli_jar_path, 
                                    app_classfiles_path, 
                                    app_source_path)

            return self.data[test_case.name]
            
        finally:
            self.reset_environment()


    def build_pair_test_cases(self, step_log_path: str, fastbot_log_path: str) -> list[PairTestCase]:
        """
        Build pair test cases from step log and fastbot log files
        """
        pair_test_cases: list[PairTestCase] = []

        events = self.replayer.get_events(fastbot_log_path, step_log_path)

        test_case_names = self.replayer.get_prop_name(events)
        self.logger.info(f"Extract {len(test_case_names)} pairs test cases")

        for prop_name in test_case_names:
            pair_test_case = self.replayer.cut_events_by_prop_name(prop_name, events)
            if pair_test_case is None:
                continue
            pair_test_cases.append(pair_test_case)

        self.logger.info(f"Build {len(pair_test_cases)} pairs test cases")
        for i, pair_test_case in enumerate(pair_test_cases):
            self.logger.info(f"Test case [{i+1}]: {pair_test_case.case_name}")
            self.logger.info(f"    -happy_path: [preconditions]: {len(pair_test_case.happy_path.preconditions)}, [property]: {len(pair_test_case.happy_path.property)}")
            self.logger.info(f"    -bug_path: [preconditions]: {len(pair_test_case.bug_path.preconditions)}, [property]: {len(pair_test_case.bug_path.property)}")

        return pair_test_cases
