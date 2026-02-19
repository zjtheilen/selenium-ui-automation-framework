# from helpers import login
from tests.helpers import login

def test_login(driver):
    heading = login(driver)
    assert "Secure Area" in heading.text
