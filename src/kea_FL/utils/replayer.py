"""
replayer.py
"""

import time
import subprocess
import re
from typing import Optional

import uiautomator2 as u2

from .data_types import TestCase, PairTestCase, Action, Touch, HAPPY_PREFIX, BUG_PREFIX
from .log_parser import LogParser
from .logger import get_logger


class Replayer:
    CLICK_ACTION = "CLICK"
    LONG_CLICK_ACTION = "LONG_CLICK"
    BACK_ACTION = "BACK"
    SCROLL_ACTIONS = {"SCROLL_TOP_DOWN", "SCROLL_BOTTOM_UP", "SCROLL_LEFT_RIGHT", "SCROLL_RIGHT_LEFT"}
    KNOWN_ACTIONS = {CLICK_ACTION, LONG_CLICK_ACTION, BACK_ACTION, *SCROLL_ACTIONS}

    def __init__(self, package_name: str, device_serial: Optional[str] = None):
        self.package_name = package_name
        self.device_serial = device_serial
        self.log_parser = LogParser()
        self.logger = get_logger("replayer")


    def connect_device(self):
        """Connect to device"""
        try:
            if self.device_serial is None:
                self.d = u2.connect()
                self.device_serial = self.d.serial
            else:
                self.d = u2.connect(self.device_serial)
            self.logger.info(f"Connected to device: {self.device_serial}")
        except Exception as e:
            raise RuntimeError(f"Connection failed: {str(e)}")
    
    def is_top_package(self, target_package: str):
        """
        Check if the target package is the top package on the device
        Args:
            target_package: Package name to check
        Returns:
            bool: True if the package is the top package, False otherwise
        """
        cmd = r'adb shell dumpsys activity activities | findstr /i "packageName="'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        top_package = None
        
        if result.returncode == 0 and result.stdout.strip():
            top_line = result.stdout.splitlines()[0].strip()
            pattern = r'packageName=([a-zA-Z0-9_\.]+)'
            match = re.search(pattern, top_line)
            if match:
                top_package = match.group(1)

        return top_package == target_package


    def map_monkey_to_event(self, events: list[dict], monkey_actions: list[Action]):
        """Map Monkey actions to corresponding Monkey events"""
        mapped_events = []
        monkey_idx = 0

        for event in events:
            # Non-Monkey events are mapped directly to mapped_events
            if event["type"] != "monkey":
                mapped_events.append(event)
                continue

            action = event["action"]
            monkey_action = monkey_actions[monkey_idx]
            # Check if the action is known
            if action in self.KNOWN_ACTIONS:
                if action != monkey_action.action_type:
                    raise ValueError(f"Event {action} does not match Monkey action {monkey_action.action_type}")
                mapped_event = event.copy()
                mapped_event["touch_series"] = monkey_action.touch_series
                mapped_events.append(mapped_event)
                monkey_idx += 1
            else:
                raise ValueError(f"Unknown action type: {action}")

        return mapped_events


    def execute_events(self, events: list[dict]):
        """Execute events in the sequence"""
        if not events:
            self.logger.info("No events to execute")
            return

        for event in events:
            if event["type"] == "monkey":
                self.logger.info(f"[{event['step_count']}] Execute Monkey event: {event['action']}")
                self._execute_monkey_event(event)
                time.sleep(1)  # Event interval
                if not self.is_top_package(self.package_name):
                    self.logger.info(f"App {self.package_name} is in background, restarting...")
                    self.d.app_start(self.package_name)
                    time.sleep(2)  # Wait for app to start
            elif event["type"] == "script_info":
                state = event["state"]
                prop_name = event["prop_name"]
                if state == "start":
                    self.logger.info(f"Script execution start state: {prop_name} - {state}")
                elif state == "pass" or state == "fail":
                    self.logger.info(f"Script execution end state: {prop_name} - {state}")
                elif state == "error":
                    self.logger.error(f"Script execution error: {prop_name} - {state}")
                else:
                    raise RuntimeError(f"Unknown script execution state: {state}")
            elif event["type"] == "script":
                self.logger.info(f"[{event['step_count']}] Execute Script event: {event['method']}")
                self._execute_script_event(event)
                time.sleep(1)  # Event interval
            else:
                raise RuntimeError(f"Unknown event type: {event['type']}")


    def _execute_script_event(self, event: dict):
        """Execute Script event"""
        method = event["method"]
        params = event["params"]
        if method == "click":
            x = params[0]
            y = params[1]
            if len(params) == 3:
                duration = float(int(params[2]) / 1000)
                self.d.long_click(x, y, duration=duration)
            else:
                self.d.click(x, y)
            self.logger.info(f"Click coordinate: ({x}, {y})")
        elif method == "long_click":
            x = params[0]
            y = params[1]
            duration = float(int(params[2]) / 1000)
            self.d.long_click(x, y, duration=duration)
            self.logger.info(f"Long click coordinate: ({x}, {y}) duration: {duration}")
        elif method == "setText":
            widget_data = params[0].copy()
            widget_data.pop("mask", None)
            widget_data.pop("childOrSibling", None)
            widget_data.pop("childOrSiblingSelector", None)
            text = params[1]
            self.d(**widget_data).set_text(text)
            self.logger.info(f"Set text to: {text}")
        elif method == "swipe":
            start_x = params[0]
            start_y = params[1]
            end_x = params[2]
            end_y = params[3]
            self.d.swipe(start_x, start_y, end_x, end_y, duration=0.5)
            self.logger.info(f"Swipe: ({start_x}, {start_y}) -> ({end_x}, {end_y})")
        elif method == "pressKey":
            key = params[0]
            self.d.press(key)
            self.logger.info(f"Press key: {key}")
        elif method == "setOrientation":
            orientation = params[0]
            self.d.set_orientation(orientation)
            self.logger.info(f"Set screen orientation: {orientation}")
        else:
            raise RuntimeError(f"Unknown Script event method: {method}")


    def _execute_monkey_event(self, event: dict):
        """Execute Monkey event"""
        action = event["action"]
        if action == self.BACK_ACTION:
            self.d.press("back")
            self.logger.info(f"Press back key")
            return

        try:
            touch_series = event["touch_series"]
            for touch in touch_series:
                self.logger.info(f"Touch: {touch}")
                touch_type = touch.touch_type
                if touch_type == "down":
                    self.d.touch.down(touch.x, touch.y)
                    self.logger.info(f"Press coordinate at: ({touch.x}, {touch.y})")
                    time.sleep(touch.wait_duration)
                elif touch_type == "move":
                    self.d.touch.move(touch.x, touch.y)
                    self.logger.info(f"Move coordinate to: ({touch.x}, {touch.y})")
                    time.sleep(touch.wait_duration)
                elif touch_type == "up":
                    self.d.touch.up(touch.x, touch.y)
                    self.logger.info(f"Release coordinate at: ({touch.x}, {touch.y})")
                    time.sleep(touch.wait_duration)
                else:
                    raise RuntimeError(f"Unknown touch type: {touch_type}")
        except Exception as e:
            raise RuntimeError(f"Execute Monkey event failed: {str(e)}")


    def get_events(self, monkey_log_path: str, step_log_path: str) -> list[dict]:
        """Get event series"""
        events = self.log_parser.parse_step_log(step_log_path)
        self.logger.info(f"Parse {len(events)} events")
        monkey_actions = self.log_parser.parse_monkey_log(monkey_log_path)
        self.logger.info(f"Parse {len(monkey_actions)} Monkey actions")
        mapped_events = self.map_monkey_to_event(events, monkey_actions)
        return mapped_events


    def run(self, package_name: str, monkey_log_path: str, step_log_path: str):
        """Run replay program"""
        try:
            self.connect_device()
            events = self.get_events(monkey_log_path, step_log_path)
            self.d.app_start(package_name)
            time.sleep(1)
            self.execute_events(events)
            self.logger.info("Event series executed successfully")
        except Exception as e:
            raise RuntimeError(f"Program run error: {str(e)}")


    def get_prop_name(self, events: list[dict]) -> set[str]:
        """Get property names from event series"""
        prop_names = set()

        for event in events:
            if event["type"] != "script_info" or event["state"] != "start":
                continue
            prop_names.add(event["prop_name"])

        return prop_names


    def cut_events_by_prop_name(self, prop_name: str, events: list[dict], filte: bool = True) -> Optional[PairTestCase]:
        """
        Cut event series by property name
        
        Args:
            prop_name: Property name to cut event series by
            events: Event series to cut
            filte: Whether to filter test cases by happy_path and bug_path, default is True.
                If filte is True, only keep test cases where happy_path and bug_path both exist.
                If filte is False, keep all test cases regardless of happy_path and bug_path.
        Returns:
            PairTestCase instance if happy_path and bug_path both exist, None otherwise
        """
        

        happy_path = []
        bug_path = []
        happy_idx = 0 # Index of the first event in happy_path that is property event
        bug_idx = 0 # Index of the first event in bug_path that is property event

        for i, event in enumerate(events):
            if happy_path and bug_path:
                break

            if event["type"] != "script_info" or event["prop_name"] != prop_name:
                continue

            if event["state"] == "start":
                if not happy_path:
                    happy_idx = i
                if not bug_path:
                    bug_idx = i
            elif event["state"] == "pass" and not happy_path:
                happy_path = events[:i+1]
            elif event["state"] == "fail" and not bug_path:
                bug_path = events[:i+1]

        if happy_path:
            happy_precondition = happy_path[:happy_idx]
            happy_property = happy_path[happy_idx:]
        else:
            happy_precondition = []
            happy_property = []

        if bug_path:
            bug_precondition = bug_path[:bug_idx]
            bug_property = bug_path[bug_idx:]
        else:
            bug_precondition = []
            bug_property = []

        case_name = prop_name.split(".")[-1]
        happy_test_case = TestCase(HAPPY_PREFIX + case_name, happy_precondition, happy_property)
        bug_test_case = TestCase(BUG_PREFIX + case_name, bug_precondition, bug_property)

        if filte and (not happy_path or not bug_path):
            self.logger.info(f"Property {prop_name} not found, skip: [happy_path] = {bool(happy_path)}, [bug_path] = {bool(bug_path)}")
            return None

        return PairTestCase(case_name, happy_test_case, bug_test_case)


