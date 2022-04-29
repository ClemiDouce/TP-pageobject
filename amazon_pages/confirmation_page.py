from selenium.webdriver.common.by import By

from .base_page import BasePage
import amazon_pages.cart_page as cart_page

class ConfirmationPage(BasePage):
    """Page who appear after adding an item to the cart"""
    go_to_cart_button = (By.CSS_SELECTOR, "span#sw-gtc a.a-button-text")

    def open_cart(self):
        """ Open the cart page"""
        self.wait_and_click(self.go_to_cart_button)
        return cart_page.CartPage(self.driver)
