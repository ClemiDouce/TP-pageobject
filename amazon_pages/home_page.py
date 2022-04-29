from amazon_pages.base_page import BasePage


class HomePage(BasePage):
    """Home page"""
    url = "http://www.amazon.fr/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.url)