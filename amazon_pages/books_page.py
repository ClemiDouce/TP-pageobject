from selenium.webdriver.common.by import By
import amazon_pages.base_page as base_page
import amazon_pages.product_page as product_page


class BooksPage(base_page.BasePage):
    """ Book's category page"""

    nouveaute_item = (By.CSS_SELECTOR, "div.octopus-best-seller-card li.octopus-pc-item")

    def select_first_book_nouveautes(self):
        """Select first item of the Nouveauté section"""
        self.wait_and_click(self.nouveaute_item)
        return product_page.ProductPage(self.driver)
