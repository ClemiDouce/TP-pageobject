from time import sleep

from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from locators import HomeLocator

from .base_page import BasePage
from .confirmation_page import ConfirmationPage
from locators import ProductLocator


class ProductPage(BasePage):
    def add_to_cart(self):
        self.wait_and_click(ProductLocator.add_to_cart_button)
        return ConfirmationPage(self.driver)
