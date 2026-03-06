import os
import shutil
import time
import logging
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# -------------------------------
# Constants / directories
# -------------------------------
DOWNLOAD_DIR = os.path.abspath("downloads")
SCREENSHOTS_DIR = os.path.abspath("screenshots")
LOGS_DIR = os.path.abspath("logs")

os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# -------------------------------
# Logger fixture (autouse)
# -------------------------------
@pytest.fixture(scope="session", autouse=True)
def logger():
    """Returns a logger available to all tests automatically."""
    log_path = os.path.join(LOGS_DIR, "framework.log")

    logger = logging.getLogger("selenium_framework")
    logger.setLevel(logging.DEBUG)

    # File handler (all levels)
    fh = logging.FileHandler(log_path)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    )

    # Console handler (info+)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger

# -------------------------------
# WebDriver fixture
# -------------------------------
@pytest.fixture
def driver(tmp_path):
    # Clean download folder
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

    # Enable downloads in headless/Chromium
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

# -------------------------------
# Hooks: logging + screenshots
# -------------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Logs test start/end and saves screenshot on failure."""
    outcome = yield
    rep = outcome.get_result()

    # logger = item.funcargs.get("logger")

    # # Log start and end
    # if logger:
    #     if rep.when == "setup":
    #         logger.info(f"Starting test: {item.name}")
    #     elif rep.when == "teardown":
    #         logger.info(f"Finished test: {item.name}")

    # Screenshot on failure
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            file_name = f"{item.name}_{int(time.time())}.png"
            path = os.path.join(SCREENSHOTS_DIR, file_name)
            driver.save_screenshot(path)
            print(f"\nScreenshot saved to {path}")


def pytest_runtest_setup(item):
    logger = item.funcargs.get("logger")
    if logger:
        logger.info(f"START TEST: {item.nodeid}")


def pytest_runtest_teardown(item, nextitem):
    logger = item.funcargs.get("logger")
    if logger:
        logger.info(f"END TEST: {item.nodeid}")