import pytest
from selenium.common.exceptions import ElementNotInteractableException

from tests.pages.dynamic_controls_page import DynamicControlsPage


@pytest.mark.regression
@pytest.mark.ui
def test_enable_input_negative(driver, logger):
    page = DynamicControlsPage(driver, logger)
    page.load()

    logger.info("Testing that input field cannot be interacted with when disabled")

    with pytest.raises(ElementNotInteractableException):
        page.enter_text_in_input("text")

    logger.info(
        "ElementNotInteractableException raised as expected when trying to interact with disabled input field"
    )


@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.negative
def test_input_starts_disabled(driver, logger):
    logger.info("Testing that input field starts disabled")
    page = DynamicControlsPage(driver, logger)
    page.load()

    input_field = page.get_input_element()
    assert not input_field.is_enabled()

    logger.info("Input field is disabled on page load as expected")
