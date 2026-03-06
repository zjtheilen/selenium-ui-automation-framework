from selenium.webdriver.common.by import By
from .base_page import BasePage


class FileDownloadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/download"

    FILE_LINKS = (By.CSS_SELECTOR, "div.example a")

    def load(self):
        self.logger.info("Loading File Download page")
        self.driver.get(self.URL)

    def get_all_filenames(self):
        self.logger.info("Getting all filenames")
        links = self.wait_for_elements(self.FILE_LINKS)
        return [link.text for link in links]

    def download_all_files(self, limit=None):
        self.logger.info("Downloading all files")
        links = self.wait_for_elements(self.FILE_LINKS)
        filenames = [link.text for link in links]

        if limit:
            links = links[:limit]
            filenames = filenames[:limit]

        for i in range(len(filenames)):
            links = self.wait_for_elements(self.FILE_LINKS)
            links[i].click()

        return filenames
