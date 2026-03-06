from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.base_page import BasePage


class AlertsPage(BasePage):

    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    JS_ALERT_BUTTON = (By.XPATH, "//button[text()='Click for JS Alert']")
    JS_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Click for JS Confirm']")
    JS_PROMPT_BUTTON = (By.XPATH, "//button[text()='Click for JS Prompt']")
    RESULT_TEXT = (By.ID, "result")

    def load(self):
        self.logger.info("Loading JS Alerts page")
        self.driver.get(self.URL)

    def trigger_alert(self):
        self.logger.info("Triggering JS Alert")
        self.wait_for_clickable(self.JS_ALERT_BUTTON).click()

    def trigger_confirm(self):
        self.logger.info("Triggering JS Confirm")
        self.wait_for_clickable(self.JS_CONFIRM_BUTTON).click()

    def trigger_prompt(self):
        self.logger.info("Triggering JS Prompt")
        self.wait_for_clickable(self.JS_PROMPT_BUTTON).click()

    def accept_alert(self):
        self.logger.info("Accepting alert")
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def dismiss_alert(self):
        self.logger.info("Dismissing alert")
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()

    def send_text_to_alert(self, text):
        self.logger.info(f"Sending text to alert: {text}")
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys(text)

    def get_result_text(self):
        text = self.wait_for_element(self.RESULT_TEXT).text
        self.logger.info(f"Result text: {text}")
        return text

    def get_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        self.logger.info(f"Alert text: {text}")
        return text