import os
import time
import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logger

    def wait_for_element(self, locator):
        self.logger.debug(f"Waiting for element: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_elements(self, locator):
        self.logger.debug(f"Waiting for elements: {locator}")
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_clickable(self, locator):
        self.logger.debug(f"Waiting for clickable element: {locator}")
        return self.wait.until(EC.element_to_be_clickable(locator))


def wait_for_file(download_dir, filename, timeout=10):
    logger = logging.getLogger("selenium_framework")

    logger.info(f"Waiting for file {filename} in {download_dir}")

    file_path = os.path.join(download_dir, filename)
    end_time = time.time() + timeout

    while time.time() < end_time:
        if os.path.exists(file_path) and not file_path.endswith(".crdownload"):
            logger.info(f"File downloaded: {filename}")
            return file_path
        time.sleep(0.25)

    raise TimeoutError(f"File {filename} was not downloaded within {timeout} seconds.")
