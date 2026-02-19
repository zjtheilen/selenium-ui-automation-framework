import pytest
from utils.driver_factory import create_driver

@pytest.fixture(scope="session")
def driver():
    """
    Session-scoped driver: launched once per pytest session.
    Quits automatically after all tests finish.
    """
    driver = create_driver()
    yield driver
    driver.quit()
