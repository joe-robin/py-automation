import sys
from playwright.sync_api import Page, Playwright
from modules.attendance import Attendance
from modules.login import LoginManager
from config import get_config


class Paths:
    def __init__(self, playwright: Playwright):
        config = get_config()
        # Initialize playwright browser and page
        self.browser = playwright.chromium.launch(headless=config.get_headless())
        self.page = self.browser.new_page()
        # login
        self.login_manager = LoginManager()
        self.login_manager.login(self.page)
        # Initialize required modules
        self.attendance = Attendance()

    def no_args(self) -> None:
        self.attendance.go_to_attendance(self.page)
        self.attendance.click_attendance_toggle_button(self.page)

    def one_arg(self) -> str:
        if sys.argv[1] not in ["check-in", "check-out", "status"]:
            raise ValueError(
                f"Invalid attendance command: {sys.argv[1]}. Must be 'check-in' or 'check-out'"
            )

        command = sys.argv[1]
        self.attendance.go_to_attendance(self.page)
        status = self.attendance.get_attendance_status(self.page)

        if command == "check-in":
            if status == "green":
                self.attendance.click_attendance_toggle_button(self.page)
                self.attendance.wait_for_attendance_status(self.page, "red")
                return "Check-in successful"
            else:
                return "Already checked in"

        elif command == "check-out":
            if status == "red":
                self.attendance.click_attendance_toggle_button(self.page)
                self.attendance.wait_for_attendance_status(self.page, "green")
                return "Check-out successful"
            else:
                return "Already checked out"
        elif command == "status":
            if status == "green":
                return "checked in"
            elif status == "red":
                return "checked in"
            else:
                return "unknown status"
