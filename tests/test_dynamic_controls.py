from tests.pages.dynamic_controls_page import DynamicControlsPage


def test_enable_input_field(driver):
    page = DynamicControlsPage(driver)
    page.load()
    is_enabled = page.enable_input()
    assert is_enabled, "Input field should be enabled after clicking the enable button"
