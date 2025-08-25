#!/usr/bin/env python3
"""
Login module for web automation using Playwright.
"""

from dotenv import load_dotenv
import os
from playwright.sync_api import Page

from config import get_config

# Load environment variables from .env file
load_dotenv()


class LoginManager:
    """Handles login operations using Playwright."""

    def login(self, page: Page):
        config = get_config()

        page.goto(config.get_login_page_url())
        # Fill in the email field
        page.fill(
            'input[type="email"][placeholder="email@icanio.com"]', config.get_email()
        )
        # Fill in the password field

        page.fill(
            'input[type="password"][placeholder="Password"]', config.get_password()
        )
        # Click the login button using its text
        page.click('button:has-text("Login")')
        # Wait for login to complete
        page.wait_for_url(config.get_home_page_url(), wait_until="commit")
