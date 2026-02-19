from selenium.webdriver.common.by import By
from utils.driver_factory import wait_for_page_load

def test_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    wait_for_page_load(driver)

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")

    username_input.send_keys("tomsmith")
    password_input.send_keys("SuperSecretPassword!")
    login_button.click()

    wait_for_page_load(driver)
    assert "Secure Area" in driver.page_source
