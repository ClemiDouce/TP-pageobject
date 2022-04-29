from time import sleep
from selenium import webdriver

from amazon_pages.books_page import BooksPage
from amazon_pages.cart_page import CartPage
from amazon_pages.confirmation_page import ConfirmationPage
from amazon_pages.home_page import HomePage
from amazon_pages.product_page import ProductPage


def test__amazon():
    """ Go to book categorie, add first item to cart, change quantity to 2"""
    driver = webdriver.Chrome()
    home = HomePage(driver)
    home.accept_cookie()
    home.top_bar.open_all_menu()
    home.top_bar.open_book_category()
    home.top_bar.open_all_books()
    book_page = BooksPage(driver)
    book_page.select_first_book_nouveautes()
    product_page = ProductPage(driver)
    product_page.add_to_cart()
    confirmation_page = ConfirmationPage(driver)
    confirmation_page.open_cart()
    cart_page = CartPage(driver)
    cart_page.set_quantity(2)
    assert cart_page.get_quantity() == "2"
    sleep(2)