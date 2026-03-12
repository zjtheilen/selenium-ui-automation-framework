import pytest

from tests.pages.alerts_page import AlertsPage
from selenium.common.exceptions import NoAlertPresentException


@pytest.mark.regression
@pytest.mark.ui
def test_js_alert(driver, logger):
    page = AlertsPage(driver, logger)
    page.load()

    page.trigger_alert()
    alert_text = page.get_alert_text()
    logger.info(f"Alert text: {alert_text}")

    page.accept_alert()
    result_text = page.get_result_text()
    logger.info(f"Result text: {result_text}")

    assert alert_text == "I am a JS Alert"
    assert result_text == "You successfully clicked an alert"
    logger.info(
        "JS Alert test completed successfully with alert text: "
        + alert_text
        + " and result text: "
        + result_text
    )


@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.parametrize(
    "action, expected_text",
    [
        ("accept", "You clicked: Ok"),
        ("dismiss", "You clicked: Cancel"),
    ],
)
def test_js_confirm_variations(driver, action, expected_text, logger):
    page = AlertsPage(driver, logger)
    page.load()
    page.trigger_confirm()

    logger.info(f"Performing action: {action}")

    if action == "accept":
        page.accept_alert()
    else:
        page.dismiss_alert()

    assert page.get_result_text() == expected_text
    logger.info(
        f"JS Confirm test completed successfully with action: {action} and expected text: {expected_text}"
    )


@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("Hello", "You entered: Hello"),
        ("", "You entered:"),
    ],
)
def test_js_prompt_variations(driver, input_text, expected, logger):
    page = AlertsPage(driver, logger)
    page.load()
    page.trigger_prompt()

    logger.info(f"Sending text to prompt: '{input_text}'")

    page.send_text_to_alert(input_text)
    page.accept_alert()

    assert page.get_result_text() == expected
    logger.info(
        f"JS Prompt test completed successfully with input: '{input_text}' and expected result: '{expected}'"
    )


@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.negative
def test_alert_not_present(driver, logger):
    page = AlertsPage(driver, logger)
    page.load()

    logger.info("Ensuring no alert is present")

    with pytest.raises(NoAlertPresentException):
        driver.switch_to.alert.accept()

    logger.info("No alert present as expected, test passed successfully")
