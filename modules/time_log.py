from dotenv import load_dotenv
from playwright.sync_api import Page
from config import get_config

load_dotenv()


class TimeLog:

    def go_to_time_log(self, page: Page):
        config = get_config()
        page.goto(config.get_time_log_page_url())
        page.wait_for_load_state("networkidle")

    def get_start_date(self, page: Page):
        #
        #
        #
        #
        #
        #
        #
        #
        #
        return
