from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators import BooksLocator
from .product_page import ProductPage


class BooksPage(BasePage):
    def select_first_book_nouveautes(self):
        self.wait_and_click(BooksLocator.nouveaute_item)
        return ProductPage(self.driver)