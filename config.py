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

        assert url is not None, "URL must be set in environment variables"
        assert email is not None, "EMAIL must be set in environment variables"
        assert password is not None, "PASSWORD must be set in environment variables"

        self.url = url
        self.email = email
        self.password = password

        self.home_page = "/event"
        self.login_page = "/home"
        self.time_log_page = "/time-sheet"

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

    def get_time_log_page_url(self) -> str:
        return self.url + self.time_log_page


# Singleton instance
_config_instance: Optional[Config] = None


def get_config() -> Config:
    global _config_instance
    if _config_instance is None:
        _config_instance = Config()
    return _config_instance
