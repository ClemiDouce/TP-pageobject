from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from locators import HomeLocator

from .base_page import BasePage
from .books_page import BooksPage

class HomePage(BasePage):
    url = "http://www.amazon.fr/"

    def accept_cookie(self):
        self.wait_and_click(HomeLocator.cookie_accept)

    def open_all_menu(self):
        self.wait_and_click(HomeLocator.burger_menu)
        return self

    def open_book_category(self):
        self.wait_and_click(HomeLocator.book_categorie)
        self.wait.until(EC.invisibility_of_element(HomeLocator.book_categorie))
        return self

    def open_all_books(self):
        self.wait_and_click(HomeLocator.all_book_categorie)
        return BooksPage(self.driver)