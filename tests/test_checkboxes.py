# from helpers import toggle_checkbox
from tests.helpers import toggle_checkbox

def test_checkboxes(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # First checkbox should toggle to checked
    assert toggle_checkbox(driver, 1) is True

    # Second checkbox should toggle to unchecked
    assert toggle_checkbox(driver, 2) is False
