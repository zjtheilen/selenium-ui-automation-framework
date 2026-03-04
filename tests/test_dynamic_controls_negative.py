import pytest
from selenium.common.exceptions import ElementNotInteractableException

from tests.pages.dynamic_controls_page import DynamicControlsPage


def test_enable_input_negative(driver):
    page = DynamicControlsPage(driver)
    page.load()

    with pytest.raises(ElementNotInteractableException):
        page.enter_text_in_input("text")
