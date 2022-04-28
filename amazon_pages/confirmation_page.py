from time import sleep

from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from locators import HomeLocator

from .base_page import BasePage

class ConfirmationPage(BasePage):
    def open_cart(self):
        pass