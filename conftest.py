import os
import logging

# from urllib import request
import pytest
import base64
import re

from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from datetime import datetime

# from config.config import HEADLESS

# from tests.helpers import safe_filename

# -------------------------------
# Constants / directories
# -------------------------------
SCREENSHOTS_DIR = os.path.abspath("screenshots")
LOGS_DIR = os.path.abspath("logs")
REPORTS_DIR = os.path.abspath("reports")

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


@pytest.fixture(scope="session")
def screenshots_dir(worker_id):
    base = "screenshots"
    path = os.path.join(base, worker_id)
    os.makedirs(path, exist_ok=True)
    return path


# -------------------------------
# WebDriver fixture
# -------------------------------
@pytest.fixture
def driver(request, tmp_path):

    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless").lower() == "true"

    if browser == "chrome":
        options = webdriver.ChromeOptions()

        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")

        # Headless
        if headless:
            options.add_argument("--headless=new")

        # Set download prefs
        prefs = {
            "download.default_directory": str(tmp_path),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        }
        options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        # Set download preferences directly on options
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", str(tmp_path))
        options.set_preference(
            "browser.helperApps.neverAsk.saveToDisk", "application/pdf,image/jpeg"
        )
        options.set_preference("pdfjs.disabled", True)

        service = FirefoxService(executable_path=r"C:\Tools\geckodriver.exe")
        driver = webdriver.Firefox(service=service, options=options)

        # driver = webdriver.Firefox(options=options)
        # driver = webdriver.Firefox(executable_path=r"C:\Program Files\geckodriver.exe", options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    try:
        driver.maximize_window()
    except Exception as e:
        print(f"Warning: Could not maximize window: {e}")

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
            worker_id = getattr(item.config, "workerinput", {}).get("workerid", "gw0")

            file_name = f"{worker_id}_{item.nodeid}_{timestamp}.png"
            file_name = safe_filename(file_name)
            path = os.path.join(SCREENSHOTS_DIR, file_name)

            driver.save_screenshot(path)
            print(f"\nScreenshot saved to {path}")

            if item.config.pluginmanager.hasplugin("html"):
                extra = getattr(rep, "extra", [])

                try:
                    with open(path, "rb") as image_file:
                        encoded = base64.b64encode(image_file.read()).decode("utf-8")
                        extra.append(extras.image(encoded, mime_type="image/png"))
                except FileNotFoundError:
                    print(f"Warning: Screenshot not found for {item.nodeid}")
                    rep.extra = extra


def safe_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', "_", filename)


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


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on (chrome, firefox, etc.)",
    )

    parser.addoption(
        "--headless",
        action="store",
        default="true",
        help="Run tests in headless mode (no browser UI)",
    )
