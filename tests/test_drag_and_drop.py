import pytest

from tests.pages.drag_and_drop_page import DragAndDropPage


@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.slow
def test_drag_and_drop(driver, logger):
    page = DragAndDropPage(driver, logger)
    page.load()

    logger.info("Testing drag and drop functionality")

    before = page.get_column_headers()
    assert before == ("A", "B")

    page.drag(page.COLUMN_A, page.COLUMN_B)

    after = page.get_column_headers()
    assert after == ("B", "A")

    logger.info(
        "Drag and drop test completed successfully with column headers swapped from "
        + str(before)
        + " to "
        + str(after)
    )
