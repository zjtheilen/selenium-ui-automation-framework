import pytest

from tests.pages.alerts_page import AlertsPage
from selenium.common.exceptions import NoAlertPresentException

def test_js_alert(driver):
    page = AlertsPage(driver)
    page.load()
    
    page.trigger_alert()
    alert_text = page.get_alert_text()
    page.accept_alert()
    result_text = page.get_result_text()

    assert alert_text == "I am a JS Alert"
    assert result_text == "You successfully clicked an alert"

# def test_js_confirm_accept(driver):
#     page = AlertsPage(driver)
#     page.load()

#     page.trigger_confirm()

#     # alert = driver.switch_to.alert
#     # alert_text = alert.text
#     alert_text = page.get_alert_text()
#     page.accept_alert()

#     # alert.accept()

#     result_text = page.get_result_text()

#     assert alert_text == "I am a JS Confirm"
#     assert result_text == "You clicked: Ok"

# def test_js_confirm_dismiss(driver):
#     page = AlertsPage(driver)
#     page.load()

#     page.trigger_confirm()
#     alert_text = page.get_alert_text()
#     page.dismiss_alert()

#     # alert = driver.switch_to.alert
#     # alert_text = alert.text

#     # alert.dismiss()
#     result_text = page.get_result_text()

#     # result_text = page.get_result_text()

#     assert alert_text == "I am a JS Confirm"
#     assert result_text == "You clicked: Cancel"

@pytest.mark.parametrize(
    "action, expected_text",
    [
        ("accept", "You clicked: Ok"),
        ("dismiss", "You clicked: Cancel"),
    ]
)
def test_js_confirm_variations(driver, action, expected_text):
    page = AlertsPage(driver)
    page.load()
    page.trigger_confirm()

    if action == "accept":
        page.accept_alert()
    else:
        page.dismiss_alert()
    
    assert page.get_result_text() == expected_text

@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("Hello", "You entered: Hello"),
        ("", "You entered:"),
    ],
)
def test_js_prompt_variations(driver, input_text, expected):
    page = AlertsPage(driver)
    page.load()
    page.trigger_prompt()

    page.send_text_to_alert(input_text)
    page.accept_alert()

    assert page.get_result_text() == expected

def test_alert_not_present(driver):
    page = AlertsPage(driver)
    page.load()

    with pytest.raises(NoAlertPresentException):
        driver.switch_to.alert.accept()