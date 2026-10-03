"""
adb_wrapper.py
"""

import subprocess
import os
from typing import List, Optional, Tuple


from .logger import get_logger


class DeviceInfo:
    """Device information class"""
    def __init__(self, serial: str, state: str):
        self.serial = serial
        self.state = state


    def __str__(self):
        return f"Device(serial={self.serial}, state={self.state})"


class AdbError(Exception):
    """ADB-related exception class"""
    pass


class AdbWrapper:
    """ADB wrapper class"""
    
    def __init__(self, adb_path: str = "adb"):
        """
        Initialize ADB wrapper
        
        Args:
            adb_path: ADB executable path, default is in system PATH
        """
        self.adb_path = adb_path
        self.logger = get_logger("adb_wrapper")


    def _run_adb_command(self, args: List[str], timeout: int = 30) -> Tuple[str, str, int]:
        """
        Execute ADB command
        
        Args:
            args: ADB command arguments
            timeout: Command timeout in seconds
            
        Returns:
            Tuple[stdout, stderr, return_code]
            
        Raises:
            AdbError: When ADB command execution fails
        """
        cmd = [self.adb_path] + args
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return result.stdout, result.stderr, result.returncode
        except subprocess.TimeoutExpired:
            raise AdbError(f"ADB command timed out: {' '.join(cmd)}")
        except Exception as e:
            raise AdbError(f"Failed to execute ADB command: {e}")


    def get_connected_devices(self) -> List[DeviceInfo]:
        """
        Get connected devices
        
        Returns:
            List of DeviceInfo objects
        """
        stdout, stderr, return_code = self._run_adb_command(["devices"])
        
        if return_code != 0:
            raise AdbError(f"Failed to get devices: {stderr}")
        
        devices = []
        lines = stdout.strip().split('\n')
        
        for line in lines[1:]:
            if line.strip():
                parts = line.split('\t')
                if len(parts) >= 2:
                    serial, state = parts[0], parts[1]
                    devices.append(DeviceInfo(serial, state))
        
        return devices
    

    def list_installed_packages(self, device_serial: Optional[str] = None) -> List[str]:
        """
        List installed packages on a device
        
        Args:
            device_serial: Device serial number (when multiple devices are connected)
            
        Returns:
            List of installed package names
        """
        args = []
        if device_serial:
            args.extend(["-s", device_serial])
        
        args.extend(["shell", "pm", "list", "packages"])
        
        stdout, stderr, return_code = self._run_adb_command(args)
        
        if return_code != 0:
            raise AdbError(f"Failed to list installed packages: {stderr}")
        
        packages = []
        for line in stdout.strip().split('\n'):
            if line.startswith("package:"):
                packages.append(line.split(":")[1].strip())
        
        return packages


    def push_file(self, local_path: str, device_path: str, device_serial: Optional[str] = None):
        """
        Push file to a device
        
        Args:
            local_path: Local file path
            device_path: Target path on the device
            device_serial: Device serial number (when multiple devices are connected)
        """
        if not os.path.exists(local_path):
            raise AdbError(f"Local file does not exist: {local_path}")
        
        args = []
        if device_serial:
            args.extend(["-s", device_serial])
        
        args.extend(["push", local_path, device_path])
        
        stdout, stderr, return_code = self._run_adb_command(args)
        
        if return_code != 0:
            self.logger.error(f"Failed to push file: {stderr}")
            raise AdbError(f"Failed to push file: {stderr}")

        self.logger.info(f"Successfully pushed file: {stdout}")


    def pull_file(self, device_path: str, local_path: str, device_serial: Optional[str] = None):
        """
        Pull file from a device
        
        Args:
            device_path: File path on the device
            local_path: Local target path
            device_serial: Device serial number (when multiple devices are connected)
        """
        local_dir = os.path.dirname(local_path)
        if local_dir:
            os.makedirs(local_dir, exist_ok=True)
        
        args = []
        if device_serial:
            args.extend(["-s", device_serial])
        
        args.extend(["pull", device_path, local_path])
        
        stdout, stderr, return_code = self._run_adb_command(args)
        
        if return_code != 0:
            self.logger.error(f"Failed to pull file: {stderr}")
            raise AdbError(f"Failed to pull file: {stderr}")

        self.logger.info(f"Successfully pulled file: {stdout}")


    def install_app(self, apk_path: str, device_serial: Optional[str] = None, reinstall: bool = True):
        """
        Install app
        
        Args:
            apk_path: APK file path
            device_serial: Device serial number (when multiple devices are connected)
            reinstall: Whether to reinstall the app
        """
        if not os.path.exists(apk_path):
            raise AdbError(f"APK file does not exist: {apk_path}")
        
        args = []
        if device_serial:
            args.extend(["-s", device_serial])
        
        args.append("install")
        if reinstall:
            args.append("-t")
            args.append("-r")
        args.append(apk_path)
        
        stdout, stderr, return_code = self._run_adb_command(args)
        
        if return_code != 0:
            self.logger.error(f"Failed to install app: {stderr}")
            raise AdbError(f"Failed to install app: {stderr}")

        self.logger.info(f"Successfully installed app: {stdout}")


    def uninstall_app(self, package_name: str, device_serial: Optional[str] = None):
        """
        Uninstall app
        
        Args:
            package_name: Package name
            device_serial: Device serial number (when multiple devices are connected)
        """
        args = []
        if device_serial:
            args.extend(["-s", device_serial])
        
        args.extend(["uninstall", package_name])
        
        stdout, stderr, return_code = self._run_adb_command(args)
        
        if return_code != 0:
            self.logger.error(f"Failed to uninstall app: {stderr}")
            raise AdbError(f"Failed to uninstall app: {stderr}")

        self.logger.info(f"Successfully uninstalled app: {stdout}")


    def launch_app(self, package_name: str, device_serial: Optional[str] = None):
        """
        Launch app
        
        Args:
            package_name: Package name
            device_serial: Device serial number (when multiple devices are connected)
        """
        args = []
        if device_serial:
            args.extend(["-s", device_serial])

        args.extend(["shell", "monkey", "-p", package_name, "-c", "android.intent.category.LAUNCHER", "1"])
        
        stdout, stderr, return_code = self._run_adb_command(args)
        
        if return_code != 0:
            self.logger.error(f"Failed to launch app: {stderr}")
            raise AdbError(f"Failed to launch app: {stderr}")

        self.logger.info(f"Successfully launched app: {stdout}")
    

    def shutdown_app(self, package_name: str, device_serial: Optional[str] = None):
        """
        Shutdown app
        
        Args:
            package_name: Package name
            device_serial: Device serial number (when multiple devices are connected)
        """
        args = []
        if device_serial:
            args.extend(["-s", device_serial])
        
        args.extend(["shell", "am", "force-stop", package_name])
        
        stdout, stderr, return_code = self._run_adb_command(args)
        
        if return_code != 0:
            self.logger.error(f"Failed to shutdown app: {stderr}")
            raise AdbError(f"Failed to shutdown app: {stderr}")

        self.logger.info(f"Successfully shutdown app: {stdout}")


    def clear_app_data(self, package_name: str, device_serial: Optional[str] = None):
        """
        Clear app data
        
        Args:
            package_name: Package name
            device_serial: Device serial number (when multiple devices are connected)
        """
        args = []
        if device_serial:
            args.extend(["-s", device_serial])
        
        args.extend(["shell", "pm", "clear", package_name])
        
        stdout, stderr, return_code = self._run_adb_command(args)
        
        if return_code != 0:
            self.logger.error(f"Failed to clear app data: {stderr}")
            raise AdbError(f"Failed to clear app data: {stderr}")

        self.logger.info(f"Successfully cleared app data: {stdout}")


    def execute_shell_command(self, command: str, device_serial: Optional[str] = None) -> str:
        """
        Execute shell command on device
        
        Args:
            command: Shell command to execute
            device_serial: Device serial number (when multiple devices are connected)
            
        Returns:
            Command execution result
        """
        args = []
        if device_serial:
            args.extend(["-s", device_serial])
        
        args.extend(["shell", command])
        
        stdout, stderr, return_code = self._run_adb_command(args)
        
        if return_code != 0:
            self.logger.error(f"Failed to execute shell command: {stderr}")
            raise AdbError(f"Failed to execute shell command: {stderr}")
        
        self.logger.info(f"Successfully executed shell command: {stdout}")
        return stdout


    def take_screenshot(self, local_path: str, device_serial: Optional[str] = None):
        """
        Take screenshot of device screen and save it to local
        
        Args:
            local_path: Local save path
            device_serial: Device serial number (when multiple devices are connected)
        """
        local_dir = os.path.dirname(local_path)
        if local_dir:
            os.makedirs(local_dir, exist_ok=True)
        
        temp_device_path = "/sdcard/screenshot_tmp.png"
        
        screenshot_cmd = f"screencap -p {temp_device_path}"
        self.execute_shell_command(screenshot_cmd, device_serial)
        
        success = self.pull_file(temp_device_path, local_path, device_serial)
        
        try:
            self.execute_shell_command(f"rm {temp_device_path}", device_serial)
            self.logger.info(f"Successfully deleted temp file: {temp_device_path}")
        except AdbError:
            self.logger.error(f"Failed to delete temp file: {temp_device_path}")
            pass


    def get_logcat(self, lines: int = 100, device_serial: Optional[str] = None) -> str:
        """
        Get logcat from device screen
        
        Args:
            lines: Number of lines to get from logcat
            device_serial: Device serial number (when multiple devices are connected)
            
        Returns:
            Logcat content
        """
        args = []
        if device_serial:
            args.extend(["-s", device_serial])
        
        args.extend(["logcat", "-d", "-t", str(lines)])
        
        stdout, stderr, return_code = self._run_adb_command(args)
        
        if return_code != 0:
            self.logger.error(f"Failed to get logcat: {stderr}")
            raise AdbError(f"Failed to get logcat: {stderr}")
        
        self.logger.info(f"Successfully got logcat: {stdout}")
        return stdout


    def check_device_connection(self, device_serial: Optional[str] = None) -> bool:
        """
        Check device connection status
        
        Args:
            device_serial: Device serial number (when multiple devices are connected)
            
        Returns:
            Device connection status
        """
        try:
            devices = self.get_connected_devices()
            if device_serial:
                return any(device.serial == device_serial and device.state == "device" for device in devices)
            else:
                return len([d for d in devices if d.state == "device"]) > 0
        except AdbError:
            return False

