from selenium.webdriver.common.by import By


class HomeLocator:
    cookie_accept = (By.CSS_SELECTOR, "input#sp-cc-accept")
    burger_menu = (By.CSS_SELECTOR, "span.hm-icon-label")
    book_categorie = (By.CSS_SELECTOR, "a[data-ref-tag='nav_em_1_1_1_15']")
    all_book_categorie = (By.CSS_SELECTOR,"ul.hmenu-visible > li:nth-of-type(3)")

class BooksLocator:
    nouveaute_item = (By.CSS_SELECTOR, "div.octopus-best-seller-card li.octopus-pc-item")