import os
import shutil

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DOWNLOAD_DIR = os.path.abspath("downloads")


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
