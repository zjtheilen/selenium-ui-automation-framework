def test_open_homepage(driver, logger):
    driver.get("https://the-internet.herokuapp.com/")
    assert "The Internet" in driver.title
    logger.info("Homepage opened successfully with title: " + driver.title)
