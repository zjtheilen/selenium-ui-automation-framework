from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tests.pages.base_page import BasePage


class DragAndDropPage(BasePage):
    URL = "https://the-internet.herokuapp.com/drag_and_drop"

    COLUMN_A = (By.ID, "column-a")
    COLUMN_B = (By.ID, "column-b")

    HEADER = (By.TAG_NAME, "header")

    def load(self):
        self.logger.info("Loading Drag and Drop page")
        self.driver.get(self.URL)

    def get_column_headers(self):
        self.logger.info("Getting column headers")
        header_a = (
            self.wait_for_element(self.COLUMN_A)
            .find_element(By.TAG_NAME, "header")
            .text
        )
        header_b = (
            self.wait_for_element(self.COLUMN_B)
            .find_element(By.TAG_NAME, "header")
            .text
        )
        return header_a, header_b

    def drag(self, source_locator, target_locator):
        self.logger.info("Dragging element")
        source = self.wait_for_element(source_locator)
        target = self.wait_for_element(target_locator)

        ActionChains(self.driver).drag_and_drop(source, target).perform()
