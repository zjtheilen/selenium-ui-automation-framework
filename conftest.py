import os
import shutil
import logging
import pytest
import base64

from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# -------------------------------
# Constants / directories
# -------------------------------
# DOWNLOAD_DIR = os.path.abspath("downloads")
SCREENSHOTS_DIR = os.path.abspath("screenshots")
LOGS_DIR = os.path.abspath("logs")
REPORTS_DIR = os.path.abspath("reports")

# os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

# -------------------------------
# Logger fixture (autouse)
# -------------------------------
@pytest.fixture(scope="session", autouse=True)
def logger():
    """Returns a logger available to all tests automatically."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    log_path = os.path.join(LOGS_DIR, f"framework.log_{timestamp}")

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

    chrome_options = Options()
    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": str(tmp_path),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        },
    )
    chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()

# -------------------------------
# Hooks: logging + screenshots
# -------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")

        if rep.failed and driver:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            file_name = f"{item.name}_{timestamp}.png"
            path = os.path.join(SCREENSHOTS_DIR, file_name)

            driver.save_screenshot(path)
            print(f"\nScreenshot saved to {path}")

            if item.config.pluginmanager.hasplugin("html"):
                extra = getattr(rep, "extra", [])
                with open(path, "rb") as image_file:
                    encoded = base64.b64encode(image_file.read()).decode("utf-8")
                    extra.append(extras.image(encoded, mime_type="image/png"))
                rep.extra = extra


def pytest_runtest_setup(item):
    logger = item.funcargs.get("logger")
    if logger:
        logger.info(f"START TEST: {item.nodeid}")


def pytest_runtest_teardown(item, nextitem):
    logger = item.funcargs.get("logger")
    if logger:
        logger.info(f"END TEST: {item.nodeid}")


def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)

    new_report_name = f"{report_dir}/automation_{timestamp}.html"
    config.option.htmlpath = new_report_name