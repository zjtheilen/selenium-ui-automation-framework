from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tests.pages.base_page import BasePage

class HoversPage(BasePage):
    URL = "https://the-internet.herokuapp.com/hovers"

    FIGURES = (By.CLASS_NAME, "figure")
    FIGCAPTION = (By.CLASS_NAME, "figcaption")
    PROFILE_LINK = (By.TAG_NAME, "a")

    def load(self):
        self.driver.get(self.URL)

    def hover_over_figure(self, index):
        figures = self.wait_for_elements(self.FIGURES)
        figure = figures[index]

        ActionChains(self.driver).move_to_element(figure).perform()
    
    def get_caption_text(self, index):
        captions = self.wait_for_elements(self.FIGCAPTION)
        return captions[index].text
    
    def is_profile_link_visible(self, index):
        captions = self.wait_for_elements(self.FIGCAPTION)
        link = captions[index].find_element(*self.PROFILE_LINK)
        return link.is_displayed()