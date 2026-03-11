from selenium.webdriver.common.by import By
from config.config import BASE_URL
from tests.pages.base_page import BasePage


class CheckboxesPage(BasePage):
    URL = BASE_URL + "/checkboxes"

    def load(self):
        self.logger.info("Loading Checkboxes page")
        self.driver.get(self.URL)

    def toggle_checkbox(self, index=1):
        self.logger.info(f"Toggle checkbox at index {index}")
        checkbox = self.wait_for_element(
            (By.CSS_SELECTOR, f"#checkboxes input:nth-of-type({index})")
        )
        checkbox.click()
        return checkbox.is_selected()
