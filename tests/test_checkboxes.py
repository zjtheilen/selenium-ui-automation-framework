from selenium.webdriver.common.by import By
from utils.driver_factory import wait_for_page_load

def test_checkboxes(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    wait_for_page_load(driver)

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")

    wait_for_page_load(driver)
    assert len(checkboxes) == 2