#!/usr/bin/env python3


from playwright.sync_api import sync_playwright
from modules.login import LoginManager


def main():

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()

            login_manager = LoginManager()
            login_manager.login(page)

    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
