import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")  # Avoid Chrome popups
    options.add_argument("--start-maximized")  # Optional: maximize window
    # options.add_argument("--headless=new")  # Uncomment for headless mode

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
