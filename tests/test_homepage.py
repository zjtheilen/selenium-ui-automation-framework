from utils.driver_factory import create_driver

def test_open_homepage():
    driver = create_driver()
    driver.get("https://the-internet.herokuapp.com")
    
    assert "The Internet" in driver.title
    
    driver.quit()
    