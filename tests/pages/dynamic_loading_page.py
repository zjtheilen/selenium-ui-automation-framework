from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.base_page import BasePage

class DynamicLoadingPage(BasePage):
    """
    Handles dynamic loading pages (example 1 and 2) from the-internet.herokuapp.com
    """
    BASE_URL = "https://the-internet.herokuapp.com/dynamic_loading"

    # Locators
    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    LOADING_INDICATOR = (By.ID, "loading")
    FINISH_TEXT = (By.ID, "finish")

    def __init__(self, driver, example=1):
        """
        example: 1 or 2 for /dynamic_loading/1 or /dynamic_loading/2
        """
        super().__init__(driver)
        self.url = f"{self.BASE_URL}/{example}"

    def load(self):
        self.driver.get(self.url)

    def start_loading(self):
        """
        Clicks start, waits for loading, and returns the final text.
        Works for both hidden-in-DOM and not-in-DOM scenarios.
        """
        self.wait_for_clickable(self.START_BUTTON).click()
        self.wait_for_loading_to_finish()
        return self.wait_for_element(self.FINISH_TEXT).text.strip()

    def wait_for_loading_to_finish(self, timeout=10):
        """
        Wait until the loading indicator disappears or is gone from DOM.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.invisibility_of_element_located(self.LOADING_INDICATOR))