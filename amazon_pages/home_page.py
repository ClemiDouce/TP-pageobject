from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .books_page import BooksPage

class HomePage(BasePage):
    """Home page"""
    url = "http://www.amazon.fr/"
    cookie_accept = (By.CSS_SELECTOR, "input#sp-cc-accept")
    burger_menu = (By.CSS_SELECTOR, "span.hm-icon-label")
    book_categorie = (By.CSS_SELECTOR, "a[data-ref-tag='nav_em_1_1_1_15']")
    all_book_categorie = (By.CSS_SELECTOR, "ul.hmenu-visible > li:nth-of-type(3)")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.url)

    def accept_cookie(self):
        """ Click on Accept All on cookie modal"""
        self.wait_and_click(self.cookie_accept)

    def open_all_menu(self):
        """Open the burger menu"""
        self.wait_and_click(self.burger_menu)

    def open_book_category(self):
        """Choose the book category on burger menu"""
        self.wait_and_click(self.book_categorie)
        self.wait.until(EC.invisibility_of_element(self.book_categorie))

    def open_all_books(self):
        """Go to the All Book page"""
        self.wait_and_click(self.all_book_categorie)
        return BooksPage(self.driver)