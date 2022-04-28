from time import sleep

from selenium import webdriver

from amazon_pages.home_page import HomePage


def test__amazon():
    """ Go to book categorie, add first item to cart, change quantity to 2"""
    driver = webdriver.Chrome()
    home = HomePage(driver)
    home.accept_cookie()
    home.open_all_menu()
    home.open_book_category()
    book_page = home.open_all_books()
    product_page = book_page.select_first_book_nouveautes()
    confirmation_page = product_page.add_to_cart()
    cart_page = confirmation_page.open_cart()
    cart_page.set_quantity(2)
    assert cart_page.get_quantity() == "2"
    sleep(2)