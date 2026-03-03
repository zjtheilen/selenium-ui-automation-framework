from tests.pages.login_page import LoginPage

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    heading = login_page.login("tomsmith", "SuperSecretPassword!")
    assert "Secure Area" in heading.text
