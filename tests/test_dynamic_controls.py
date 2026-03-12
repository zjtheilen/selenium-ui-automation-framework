import pytest

from tests.pages.dynamic_controls_page import DynamicControlsPage


@pytest.mark.regression
@pytest.mark.ui
def test_enable_input_field(driver, logger):
    page = DynamicControlsPage(driver, logger)
    page.load()

    logger.info("Testing enabling the input field")

    is_enabled = page.enable_input()
    assert is_enabled, "Input field should be enabled after clicking the enable button"

    logger.info("Input field enabled successfully, now testing text input")
