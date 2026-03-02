import pytest
from tests.pages.iframe_page import IframePage

def test_iframe_editor(driver):
    page = IframePage(driver)
    page.load()

    if page.is_readonly_notification_present():
        text = page.get_readonly_notification_text()
        assert "TinyMCE is in read-only mode" in text
        print("Editor is read-only, cannot type.")
    else:
        success = page.write_in_editor("Hello World!")
        assert success is True
        assert page.get_editor_text() == "Hello World!"