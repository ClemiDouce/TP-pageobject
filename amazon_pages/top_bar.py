from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from amazon_pages.page_element import PageElement


class TopBar(PageElement):
    burger_menu = (By.CSS_SELECTOR, "span.hm-icon-label")
    book_categorie = (By.CSS_SELECTOR, "a[data-ref-tag='nav_em_1_1_1_15']")
    all_book_categorie = (By.CSS_SELECTOR, "ul.hmenu-visible > li:nth-of-type(3)")
    search_input = (By.CSS_SELECTOR, "input#twotabsearchtextbox")

    def open_all_menu(self):
        """Open the burger menu"""
        self.wait_and_click(self.burger_menu)

    def open_book_category(self):
        """Choose the book_page category on burger menu"""
        self.wait_and_click(self.book_categorie)
        self.wait.until(EC.invisibility_of_element(self.book_categorie))

    def open_all_books(self):
        """Go to the All Book page"""
        self.wait_and_click(self.all_book_categorie)

    def search_product(self, search_text):
        """Search a product in the search bar"""
        self.enter_text_and_valid(self.search_input, search_text)