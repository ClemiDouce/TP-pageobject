from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from locators import HomeLocator, CartLocator
from .base_page import BasePage

class CartPage(BasePage):
    def set_quantity(self, quantity):
        quantity_select_element = Select(
            self.wait.until(EC.visibility_of_element_located(CartLocator.quantity_select))
        )
        quantity_select_element.select_by_value(str(quantity))
        return self

    def get_quantity(self):
        quantity_select_element = Select(
            self.wait.until(EC.visibility_of_element_located(CartLocator.quantity_select))
        )
        return quantity_select_element.first_selected_option.text