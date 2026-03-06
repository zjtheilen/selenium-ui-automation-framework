from tests.pages.login_page import LoginPage


def test_login(driver, logger):
    login_page = LoginPage(driver, logger)
    login_page.load()

    logger.info("Testing login with valid credentials")

    heading = login_page.login("tomsmith", "SuperSecretPassword!")
    assert "Secure Area" in heading.text

    logger.info("Login test completed successfully with heading: " + heading.text)