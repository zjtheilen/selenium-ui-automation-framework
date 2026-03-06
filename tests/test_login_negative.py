import pytest
from tests.pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("wronguser", "SuperSecretPassword!", "Your username is invalid!"),
        ("tomsmith", "wrongpass", "Your password is invalid!"),
        ("wronguser", "wrongpass", "Your username is invalid!"),
        ("", "", "Your username is invalid!"),
    ],
)
def test_login_negative(driver, username, password, expected_error, logger):
    page = LoginPage(driver, logger)
    page.load()

    logger.info(f"Testing login with username: '{username}' and password: '{password}' expecting error: '{expected_error}'")

    page.login(username, password, expect_success=False)
    assert expected_error in page.get_error_message()

    logger.info("Login negative test completed with expected error: " + expected_error)