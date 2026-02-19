from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    wait = WebDriverWait(driver, 10)  # give extra time

    # Wait for the heading to be visible (not just present in DOM)
    secure_heading = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(., 'Secure Area')]"))
    )

    assert "Secure Area" in secure_heading.text
