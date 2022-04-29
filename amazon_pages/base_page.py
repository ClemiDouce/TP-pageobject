from selenium.webdriver.common.by import By

import amazon_pages.books_page as book_page
from amazon_pages.page_element import PageElement
from amazon_pages.top_bar import TopBar



class BasePage(PageElement):
    """Base class for all pages"""

    cookie_accept = (By.CSS_SELECTOR, "input#sp-cc-accept")

    def __init__(self, driver):
        super().__init__(driver)
        self.top_bar = TopBar(driver)

    def accept_cookie(self):
        """ Click on Accept All on cookie modal"""
        self.wait_and_click(self.cookie_accept)
        return self

    def search_product(self, text):
        self.top_bar.search_product(text)

    def open_all_book(self):
        self.top_bar.open_all_menu()
        self.top_bar.open_book_category()
        self.top_bar.open_all_books()
        return book_page.BooksPage(self.driver)