from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.base_page import BasePage


class DynamicControlsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_controls"

    # Locators
    INPUT_FIELD = (By.CSS_SELECTOR, "#input-example input")
    ENABLE_BUTTON = (By.CSS_SELECTOR, "#input-example button")
    MESSAGE = (By.ID, "message")

    def load(self):
        self.logger.info("Loading Dynamic Controls page")
        self.driver.get(self.URL)

    def enable_input(self):
        self.logger.info("Enabling input field")
        self.wait_for_clickable(self.ENABLE_BUTTON).click()
        self.wait_for_element(self.MESSAGE)
        return self.wait_for_element(self.INPUT_FIELD).is_enabled()

    def enter_text_in_input(self, text):
        self.logger.info("Entering text in input field")
        input_field = self.wait.until(EC.presence_of_element_located(self.INPUT_FIELD))
        input_field.send_keys(text)

    def get_input_element(self):
        self.logger.info("Getting input element")
        return self.wait.until(EC.presence_of_element_located(self.INPUT_FIELD))
