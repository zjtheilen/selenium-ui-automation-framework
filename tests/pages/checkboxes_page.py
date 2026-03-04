from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage


class CheckboxesPage(BasePage):
    URL = "https://the-internet.herokuapp.com/checkboxes"

    def load(self):
        self.driver.get(self.URL)

    def toggle_checkbox(self, index=1):
        checkbox = self.wait_for_element(
            (By.CSS_SELECTOR, f"#checkboxes input:nth-of-type({index})")
        )
        checkbox.click()
        return checkbox.is_selected()
