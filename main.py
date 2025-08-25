#!/usr/bin/env python3


import sys
from playwright.sync_api import sync_playwright
from paths import Paths


def main() -> str:

    try:
        with sync_playwright() as playwright:
            paths = Paths(playwright)

            match len(sys.argv):
                case 1:
                    paths.no_args()
                    return "Toggled attendance"
                case 2:
                    message = paths.one_arg()
                    return message
                case _:
                    raise ValueError("Invalid attendance command")

    except Exception as e:
        print(f"Error: {str(e)}")
        return "Error"


if __name__ == "__main__":
    result = main()
    print(result)
    exit(0 if result != "Error" else 1)
