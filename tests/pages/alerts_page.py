from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class AlertsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    # Locators
    JS_ALERT_BUTTON = (By.XPATH, "//button[text()='Click for JS Alert']")
    JS_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Click for JS Confirm']")
    RESULT_TEXT = (By.ID, "result")

    def load(self):
        self.driver.get(self.URL)

    def trigger_alert(self):
        """Click the JS Alert button and accept the alert."""
        self.wait_for_clickable(self.JS_ALERT_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        result_text = self.wait_for_element(self.RESULT_TEXT).text
        return alert_text, result_text

    def trigger_confirm(self, accept=True):
        """Click the JS Confirm button and accept or dismiss the alert."""
        self.wait_for_clickable(self.JS_CONFIRM_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        if accept:
            alert.accept()
        else:
            alert.dismiss()
        result_text = self.wait_for_element(self.RESULT_TEXT).text
        return alert_text, result_text