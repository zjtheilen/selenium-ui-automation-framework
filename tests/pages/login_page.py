from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    # Locators
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.radius")
    SECURE_HEADING = (By.XPATH, "//h2[contains(text(),'Secure Area')]")

    def load(self):
        self.driver.get(self.URL)

    def login(self, username="tomsmith", password="SuperSecretPassword!"):
        self.wait_for_element(self.USERNAME).send_keys(username)
        self.wait_for_element(self.PASSWORD).send_keys(password)
        self.wait_for_clickable(self.LOGIN_BUTTON).click()
        # Wait for the secure area heading
        return self.wait_for_element(self.SECURE_HEADING)
