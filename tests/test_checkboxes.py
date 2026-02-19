from tests.pages.checkboxes_page import CheckboxesPage

def test_checkboxes(driver):
    page = CheckboxesPage(driver)
    page.load()
    assert page.toggle_checkbox(1) is True
    assert page.toggle_checkbox(2) is False
