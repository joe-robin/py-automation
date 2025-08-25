import time
from typing import Literal
from dotenv import load_dotenv
from playwright.sync_api import Page
from config import get_config

load_dotenv()


class Attendance:

    def __init__(self):
        self.config = get_config()

    def go_to_attendance(self, page: Page):
        page.goto(self.config.get_attendance_page_url())

    def get_attendance_status(self, page: Page) -> Literal["green", "red"]:
        color = page.locator(
            "//button[@id='toggle-btn' and not(contains(@disabled, 'true'))]"
        ).evaluate("el => getComputedStyle(el).backgroundColor")

        if color == self.config.get_check_in_button_color():
            return "green"
        elif color == self.config.get_check_out_button_color():
            return "red"
        else:
            raise ValueError(f"Invalid attendance status: {color}")

    def click_attendance_toggle_button(self, page: Page):
        page.locator("//button[@id='toggle-btn']").click()

    # wait for maxmimum of 1 minute
    def wait_for_attendance_status(self, page: Page, status: Literal["green", "red"]):
        time.sleep(1)
        start_time = time.time()

        while True:
            current_status = self.get_attendance_status(page)
            if current_status == status:
                return
            else:
                time.sleep(1)
            if time.time() - start_time > 60:
                raise ValueError("Timeout waiting for attendance status")
