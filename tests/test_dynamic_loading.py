import pytest

from tests.pages.dynamic_loading_page import DynamicLoadingPage


@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.slow
def test_dynamic_loading_example1(driver, logger):
    page = DynamicLoadingPage(driver, logger, example=1)
    page.load()
    logger.info("Testing Dynamic Loading Example 1")

    result_text = page.start_loading()
    assert result_text == "Hello World!"
    logger.info(
        f"Dynamic Loading Example 1 test completed successfully with loaded text: {result_text}"
    )


@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.slow
def test_dynamic_loading_example2(driver, logger):
    page = DynamicLoadingPage(driver, logger, example=2)
    page.load()
    logger.info("Testing Dynamic Loading Example 2")

    result_text = page.start_loading()
    assert result_text == "Hello World!"
    logger.info(
        f"Dynamic Loading Example 2 test completed successfully with loaded text: {result_text}"
    )
