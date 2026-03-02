from tests.pages.alerts_page import AlertsPage

def test_js_alert(driver):
    page = AlertsPage(driver)
    page.load()
    alert_text, result_text = page.trigger_alert()
    assert alert_text == "I am a JS Alert"
    assert result_text == "You successfully clicked an alert"

def test_js_confirm_accept(driver):
    page = AlertsPage(driver)
    page.load()
    alert_text, result_text = page.trigger_confirm(accept=True)
    assert alert_text == "I am a JS Confirm"
    assert result_text == "You clicked: Ok"

def test_js_confirm_dismiss(driver):
    page = AlertsPage(driver)
    page.load()
    alert_text, result_text = page.trigger_confirm(accept=False)
    assert alert_text == "I am a JS Confirm"
    assert result_text == "You clicked: Cancel"