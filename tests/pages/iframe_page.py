from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.base_page import BasePage


class IframePage(BasePage):
    URL = "https://the-internet.herokuapp.com/iframe"

    # Locators
    IFRAME = (By.ID, "mce_0_ifr")
    EDITOR_BODY = (By.ID, "tinymce")
    READONLY_NOTIFICATION = (By.CSS_SELECTOR, "div.tox-notification--warning")

    def load(self):
        self.logger.info("Loading Iframe page")
        self.driver.get(self.URL)

    def is_readonly_notification_present(self):
        """Return True if the TinyMCE read-only notification exists."""
        self.logger.info("Checking if read-only notification is present")
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self.READONLY_NOTIFICATION)
            )
            return True
        except Exception:
            return False

    def get_readonly_notification_text(self):
        """Return the text of the read-only notification if present."""
        self.logger.info("Getting read-only notification text")
        if self.is_readonly_notification_present():
            return self.driver.find_element(*self.READONLY_NOTIFICATION).text
        return None

    def write_in_editor(self, text):
        """Switch to iframe and type text. Returns True if successful."""
        self.logger.info("Writing in editor")
        if self.is_readonly_notification_present():
            return False  # Cannot type if read-only notice exists

        iframe = self.driver.find_element(*self.IFRAME)
        self.driver.switch_to.frame(iframe)
        body = self.driver.find_element(*self.EDITOR_BODY)
        body.clear()
        body.send_keys(text)
        self.driver.switch_to.default_content()
        return True

    def get_editor_text(self):
        """Return the current text in the iframe editor."""
        self.logger.info("Getting editor text")
        iframe = self.driver.find_element(*self.IFRAME)
        self.driver.switch_to.frame(iframe)
        body = self.driver.find_element(*self.EDITOR_BODY)
        text = body.text
        self.driver.switch_to.default_content()
        return text
