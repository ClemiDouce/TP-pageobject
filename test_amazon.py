from selenium import webdriver
from amazon_pages.home_page import HomePage


def test__amazon():
    """ Go to book_page categorie, add first item to cart, change quantity to 2"""
    driver = webdriver.Chrome()
    home = HomePage(driver)
    cart_page = home.accept_cookie()\
        .open_all_book()\
        .select_first_book_nouveautes()\
        .add_to_cart().open_cart()\
        .set_quantity(2)
    assert cart_page.get_quantity() == "2"
