import os
from dotenv import load_dotenv

load_dotenv()

from typing import Optional


class Config:

    url: str
    email: str
    password: str

    def __init__(self):
        url = os.getenv("URL")
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")
        headless = os.getenv("HEADLESS")

        assert url is not None, "URL must be set in environment variables"
        assert email is not None, "EMAIL must be set in environment variables"
        assert password is not None, "PASSWORD must be set in environment variables"
        assert headless is not None, "HEADLESS must be set in environment variables"

        self.url = url
        self.email = email
        self.password = password
        self.headless = headless

        self.home_page = "/event"
        self.login_page = "/home"
        self.attendance_page = "/time-sheet"

        self.check_out_button_color = "rgb(233, 91, 109)"
        self.check_in_button_color = "rgb(20, 180, 116)"

    def get_url(self) -> str:
        return self.url

    def get_email(self) -> str:
        return self.email

    def get_password(self) -> str:
        return self.password

    def get_login_page_url(self) -> str:
        return self.url + self.login_page

    def get_home_page_url(self) -> str:
        return self.url + self.home_page

    def get_attendance_page_url(self) -> str:
        return self.url + self.attendance_page

    def get_check_out_button_color(self) -> str:
        return self.check_out_button_color

    def get_check_in_button_color(self) -> str:
        return self.check_in_button_color

    def get_headless(self) -> bool:
        return True if self.headless == "1" else False


# Singleton instance
_config_instance: Optional[Config] = None


def get_config() -> Config:
    global _config_instance
    if _config_instance is None:
        _config_instance = Config()
    return _config_instance
