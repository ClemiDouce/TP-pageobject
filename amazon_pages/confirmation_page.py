from selenium.webdriver.common.by import By

from amazon_pages.base_page import BasePage


class ConfirmationPage(BasePage):
    """Page who appear after adding an item to the cart"""
    go_to_cart_button = (By.CSS_SELECTOR, "span#sw-gtc a.a-button-text")

    def open_cart(self):
        """ Open the cart page"""
        self.wait_and_click(self.go_to_cart_button)
        from .cart_page import CartPage
        return CartPage(self.driver)
