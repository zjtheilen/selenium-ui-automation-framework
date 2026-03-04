from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    """Create a Chrome WebDriver instance with stable options."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")  # stability on Windows/CI
    options.add_argument("--disable-gpu")  # avoid GPU rendering issues
    options.add_argument("--disable-extensions")  # disable browser extensions
    options.add_argument("--disable-dev-shm-usage")  # reduce memory issues
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )
    options.add_argument("--user-data-dir=C:/temp/selenium-profile")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    return driver


def wait_for_page_load(driver, timeout=10):
    """Wait until the page's document.readyState is 'complete'."""
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
