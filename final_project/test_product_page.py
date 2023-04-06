import time
import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()

        email = str(time.time()) + "@fakemail.org"
        password = "test_password"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        product_link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, product_link)
        page.open()

        page.add_to_basket()
        page.solve_quiz_and_get_code()

        product_name = page.get_product_name()
        assert page.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not present"
        assert page.is_element_present(
            *ProductPageLocators.PRODUCT_NAME), "Product name is not present"
        assert page.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE), "Product price is not present"
        assert page.get_success_message() == product_name, "Success message is not equal to product name"

    def test_user_cant_see_success_message(self, browser):
        product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, product_link)
        page.open()
        assert page.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    cart_page = BasketPage(browser, browser.current_url)
    cart_page.shouldnt_be_any_product_in_a_cart()

