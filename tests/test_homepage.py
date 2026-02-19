def test_open_homepage(driver):
    driver.get("https://the-internet.herokuapp.com/")
    assert "The Internet" in driver.title
