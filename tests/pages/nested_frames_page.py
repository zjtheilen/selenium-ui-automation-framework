from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class NestedFramesPage(BasePage):
    URL = "https://the-internet.herokuapp.com/nested_frames"

    def load(self):
        self.driver.get(self.URL)
    
    def get_frame_text(self, frame_path):
        self.driver.switch_to.default_content()
        for frame in frame_path:
            self.driver.switch_to.frame(frame)
        body = self.driver.find_element(By.TAG_NAME, "body")
        text = body.text
        self.driver.switch_to.default_content()
        return text