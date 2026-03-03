from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    # Locators
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.radius")
    SECURE_HEADING = (By.XPATH, "//h2[contains(text(),'Secure Area')]")
    ERROR_MESSAGE = (By.ID, "flash")  # Or correct locator for the error div

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password, expect_success=True):
        self.wait_for_element(self.USERNAME).clear()
        self.wait_for_element(self.USERNAME).send_keys(username)
        self.wait_for_element(self.PASSWORD).clear()
        self.wait_for_element(self.PASSWORD).send_keys(password)
        self.wait_for_clickable(self.LOGIN_BUTTON).click()
        
        if expect_success:
            return self.wait_for_element(self.SECURE_HEADING)
    
    def get_error_message(self):
        error_elem = self.wait_for_element(self.ERROR_MESSAGE)
        text = error_elem.text.strip()
        return text.splitlines()[0]
        # return error_elem.text.strip()
