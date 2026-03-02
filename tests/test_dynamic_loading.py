from tests.pages.dynamic_loading_page import DynamicLoadingPage

def test_dynamic_loading_example1(driver):
    page = DynamicLoadingPage(driver, example=1)
    page.load()
    assert page.start_loading() == "Hello World!"

def test_dynamic_loading_example2(driver):
    page = DynamicLoadingPage(driver, example=2)
    page.load()
    assert page.start_loading() == "Hello World!"