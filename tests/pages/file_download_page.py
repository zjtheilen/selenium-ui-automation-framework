from selenium.webdriver.common.by import By
from .base_page import BasePage

class FileDownloadPage(BasePage):
    Url = "https://the-internet.herokuapp.com/download"

    FILE_LINK = (By.CSS_SELECTOR, "div.example a")

    def load(self):
        self.driver.get(self.Url)

    def download_first_file(self, download_dir):
        file_link = self.wait_for_element(self.FILE_LINK)
        filename = file_link.text

        file_link.click()
        return filename