from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class CartPage(BasePage):
    """ Page of cart"""
    quantity_select = (By.CSS_SELECTOR, "select[name='quantity']")

    def set_quantity(self, quantity):
        """ Set the quantity of the first item"""
        quantity_select_element = Select(
            self.wait.until(EC.visibility_of_element_located(self.quantity_select))
        )
        quantity_select_element.select_by_value(str(quantity))
        return self

    def get_quantity(self):
        """ Get the quantity of the first item"""
        quantity_select_element = Select(
            self.wait.until(EC.visibility_of_element_located(self.quantity_select))
        )
        return quantity_select_element.first_selected_option.text
