from selenium.webdriver.common.by import By

from amazon_pages.page_element import PageElement
from amazon_pages.top_bar import TopBar


class BasePage(PageElement):
    """Base class for all pages"""

    cookie_accept = (By.CSS_SELECTOR, "input#sp-cc-accept")

    def __init__(self, driver):
        super().__init__(driver)
        self.top_bar = TopBar(driver)

    def accept_cookie(self):
        """ Click on Accept All on cookie modal"""
        self.wait_and_click(self.cookie_accept)
