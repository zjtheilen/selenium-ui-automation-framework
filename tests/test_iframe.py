import pytest

from tests.pages.iframe_page import IframePage


@pytest.mark.regression
@pytest.mark.ui
def test_iframe_editor(driver, logger):
    page = IframePage(driver, logger)
    page.load()

    logger.info("Testing TinyMCE editor within an iframe")

    if page.is_readonly_notification_present():
        text = page.get_readonly_notification_text()
        assert "TinyMCE is in read-only mode" in text
        logger.warning("TinyMCE editor is in read-only mode, skipping text input test")
    else:
        success = page.write_in_editor("Hello World!")
        assert success is True
        assert page.get_editor_text() == "Hello World!"
        logger.info("Successfully wrote text in the TinyMCE editor and verified it")
