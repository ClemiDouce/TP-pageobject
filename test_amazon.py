from time import sleep

from selenium import webdriver

from amazon_pages.home_page import HomePage


def test__amazon():
    driver = webdriver.Chrome()
    driver.get("http://amazon.fr/")
    home = HomePage(driver)
    home.accept_cookie()
    home.open_all_menu()
    home.open_book_category()
    book_page = home.open_all_books()
    product_page = book_page.select_first_book_nouveautes()
    sleep(2)