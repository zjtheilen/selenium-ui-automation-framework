import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()

    chrome_options.add_argument("--incognito")  # Use incognito mode to avoid cached logins
    
    # Disable Chrome password manager and save-password bubbles
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    
    # Optional: disable other UI distractions
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    
    # Use a fresh temporary profile (optional but helps avoid cached logins)
    chrome_options.add_argument("--user-data-dir=C:/temp/selenium-profile")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    yield driver
    driver.quit()
