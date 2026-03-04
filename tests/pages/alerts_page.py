from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    # Locators
    JS_ALERT_BUTTON = (By.XPATH, "//button[text()='Click for JS Alert']")
    JS_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Click for JS Confirm']")
    JS_PROMPT_BUTTON = (By.XPATH, "//button[text()='Click for JS Prompt']")
    RESULT_TEXT = (By.ID, "result")

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def load(self):
        self.driver.get(self.URL)

    def trigger_alert(self):
        self.driver.find_element(*self.JS_ALERT_BUTTON).click()

    def trigger_confirm(self, accept=True):
        self.driver.find_element(*self.JS_CONFIRM_BUTTON).click()
    
    def trigger_prompt(self):
        self.driver.find_element(*self.JS_PROMPT_BUTTON).click()

    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
    
    def dismiss_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()
    
    def send_text_to_alert(self, text):
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys(text)
    
    def get_result_text(self):
        return self.wait.until(
            EC.presence_of_element_located(self.RESULT_TEXT)
        ).text
    
    def get_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        return alert.text