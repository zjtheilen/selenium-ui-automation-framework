from utils.driver_factory import wait_for_page_load

def test_open_homepage(driver):
    driver.get("https://the-internet.herokuapp.com")
    wait_for_page_load(driver)
    
    wait_for_page_load(driver)
    assert "The Internet" in driver.title
    