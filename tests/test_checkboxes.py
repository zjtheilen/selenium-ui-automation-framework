from tests.pages.checkboxes_page import CheckboxesPage


def test_checkboxes(driver, logger):
    page = CheckboxesPage(driver, logger)
    page.load()

    logger.info("Testing checkboxes on the page")

    assert page.toggle_checkbox(1) is True
    assert page.toggle_checkbox(2) is False

    logger.info(
        "Checkboxes test completed successfully with checkbox 1 selected and checkbox 2 deselected"
    )
