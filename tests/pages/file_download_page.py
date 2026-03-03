from selenium.webdriver.common.by import By
from .base_page import BasePage

class FileDownloadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/download"

    FILE_LINKS = (By.CSS_SELECTOR, "div.example a")

    def load(self):
        self.driver.get(self.URL)

    # def download_first_file(self, download_dir):
    #     file_link = self.wait_for_element(self.FILE_LINK)
    #     filename = file_link.text

    #     file_link.click()
    #     return filename

    def get_all_filenames(self):
        links = self.wait_for_elements(self.FILE_LINKS)
        return [link.text for link in links]
    
    def download_all_files(self):
        links = self.wait_for_elements(self.FILE_LINKS)
        filenames = []

        for link in links:
            filenames.append(link.text)
            link.click()

        return filenames
    