from selenium.webdriver.common.by import By
from .base_page import BasePage
from .confirmation_page import ConfirmationPage


class ProductPage(BasePage):
    """ Page of a product"""

    add_to_cart_button = (By.CSS_SELECTOR, "input#add-to-cart-button")

    def add_to_cart(self):
        """ Add the product on page to cart"""
        self.wait_and_click(self.add_to_cart_button)
        return ConfirmationPage(self.driver)
