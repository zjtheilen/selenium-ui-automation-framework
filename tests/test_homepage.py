import pytest

from config.config import BASE_URL


@pytest.mark.smoke
@pytest.mark.ui
def test_open_homepage(driver, logger):
    driver.get(BASE_URL)
    assert "The Internet" in driver.title
    logger.info("Homepage opened successfully with title: " + driver.title)
