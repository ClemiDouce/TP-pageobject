from time import sleep

from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from locators import ConfirmationLocator

from .base_page import BasePage
from .cart_page import CartPage


class ConfirmationPage(BasePage):
    def open_cart(self):
        self.wait_and_click(ConfirmationLocator.go_to_cart_button)
        return CartPage(self.driver)