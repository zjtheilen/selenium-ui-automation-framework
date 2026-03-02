from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class FileUploadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/upload"

    # Locators
    FILE_INPUT = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    UPLOADED_FILE_NAME = (By.ID, "uploaded-files")

    def load(self):
        self.driver.get(self.URL)

    def upload_file(self, file_path):
        self.wait_for_element(self.FILE_INPUT).send_keys(file_path)
        self.wait_for_clickable(self.UPLOAD_BUTTON).click()
        return self.wait_for_element(self.UPLOADED_FILE_NAME).text