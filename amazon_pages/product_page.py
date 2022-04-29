from selenium.webdriver.common.by import By

from amazon_pages.base_page import BasePage


class ProductPage(BasePage):
    """ Page of a product"""

    add_to_cart_button = (By.CSS_SELECTOR, "input#add-to-cart-button")

    def add_to_cart(self):
        """ Add the product on page to cart"""
        self.wait_and_click(self.add_to_cart_button)
        from .confirmation_page import ConfirmationPage
        return ConfirmationPage(self.driver)
