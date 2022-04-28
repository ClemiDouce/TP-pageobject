from selenium.webdriver.common.by import By
from .base_page import BasePage
from .product_page import ProductPage


class BooksPage(BasePage):
    """ Book's category page"""

    nouveaute_item = (By.CSS_SELECTOR, "div.octopus-best-seller-card li.octopus-pc-item")

    def select_first_book_nouveautes(self):
        """Select first item of the Nouveauté section"""
        self.wait_and_click(self.nouveaute_item)
        return ProductPage(self.driver)