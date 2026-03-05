import os
import shutil
import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DOWNLOAD_DIR = os.path.abspath("downloads")
SCREENSHOTS_DIR = os.path.abspath("screenshots")


@pytest.fixture
def driver(tmp_path):
    if os.path.exists(DOWNLOAD_DIR):
        shutil.rmtree(DOWNLOAD_DIR)
    os.makedirs(DOWNLOAD_DIR)

    download_dir = str(tmp_path)

    chrome_options = Options()
    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        },
    )

    driver = webdriver.Chrome(options=chrome_options)

    # Enable downloads in headless / Chromium
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    driver.execute(
        "send_command",
        {
            "cmd": "Page.setDownloadBehavior",
            "params": {"behavior": "allow", "downloadPath": download_dir},
        },
    )

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            if not os.path.exists(SCREENSHOTS_DIR):
                os.makedirs(SCREENSHOTS_DIR)

            file_name = f"{item.name}_{int(time.time())}.png"
            path = os.path.join(SCREENSHOTS_DIR, file_name)
            driver.save_screenshot(path)
            print(f"\nScreenshot saved to {path}")
