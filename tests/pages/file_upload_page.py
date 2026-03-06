import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.base_page import BasePage


class FileUploadPage(BasePage):
    FILE_INPUT = (By.ID, "file-upload")
    SUBMIT_BUTTON = (By.ID, "file-submit")
    UPLOADED_FILE_NAME = (By.ID, "uploaded-files")
    ERROR_MESSAGE = (By.TAG_NAME, "h1")  # Adjust if needed

    def __init__(self, driver, logger, timeout=10):
        super().__init__(driver, logger)
        self.wait = WebDriverWait(driver, timeout)

    def load(self):
        self.logger.info("Loading File Upload page")
        self.driver.get("https://the-internet.herokuapp.com/upload")

    def upload_file(self, file_path=None):
        self.logger.info("Uploading file")  
        if file_path:
            abs_path = os.path.abspath(file_path)
            elem = self.wait.until(EC.presence_of_element_located(self.FILE_INPUT))
            elem.send_keys(abs_path)

        # Always click submit
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_uploaded_file_name(self):
        self.logger.info("Getting uploaded file name")
        try:
            return self.wait.until(
                EC.presence_of_element_located(self.UPLOADED_FILE_NAME)
            ).text
        except Exception:
            return None

    def get_error_message(self):
        self.logger.info("Getting error message")
        return self.driver.page_source
