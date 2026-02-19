from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, locator, timeout=10):
    """
    Wait until the element is present in the DOM.
    """
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located(locator))


def wait_for_clickable(driver, locator, timeout=10):
    """
    Wait until the element is clickable.
    """
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable(locator))


def toggle_checkbox(driver, index=1):
    """
    Toggle a checkbox by its 1-based index (1 = first checkbox, 2 = second checkbox)
    Works for the-internet checkboxes page.
    Returns True if checkbox is now checked, False otherwise.
    """
    checkbox = wait_for_element(driver, (By.CSS_SELECTOR, f"#checkboxes input:nth-of-type({index})"))
    checkbox.click()
    return checkbox.is_selected()


def login(driver, username="tomsmith", password="SuperSecretPassword!"):
    """
    Logs into the-internet login page.
    Waits for the Secure Area page to be loaded.
    """
    driver.get("https://the-internet.herokuapp.com/login")

    # Fill login form
    wait_for_element(driver, (By.ID, "username")).send_keys(username)
    wait_for_element(driver, (By.ID, "password")).send_keys(password)
    wait_for_clickable(driver, (By.CSS_SELECTOR, "button.radius")).click()

    # Wait for Secure Area heading
    wait = WebDriverWait(driver, 10)
    heading = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Secure Area')]")))
    return heading
