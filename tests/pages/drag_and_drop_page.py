from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tests.pages.base_page import BasePage

class DragAndDropPage(BasePage):
    URL = "https://the-internet.herokuapp.com/drag_and_drop"

    COLUMN_A = (By.ID, "column-a")
    COLUMN_B = (By.ID, "column-b")

    HEADER = (By.TAG_NAME, "header")

    def load(self):
        self.driver.get(self.URL)

    def get_column_headers(self):
        header_a = self.wait_for_element(self.COLUMN_A).find_element(By.TAG_NAME, "header").text
        header_b = self.wait_for_element(self.COLUMN_B).find_element(By.TAG_NAME, "header").text
        return header_a, header_b
    
    def drag_and_drop(self):
        source = self.wait_for_element(self.COLUMN_A)
        target = self.wait_for_element(self.COLUMN_B)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()