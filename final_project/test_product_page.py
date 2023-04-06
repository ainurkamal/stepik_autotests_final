import time
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


class TestUserAddToBasketFromProductPage:
    product_link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "test_password"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.product_link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_product_details()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.product_link)
        page.open()
        page.check_user_cant_see_success_message()


class TestGuestInteractsWithBasketFromProductPage:
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_cart_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        cart_page = BasketPage(browser, browser.current_url)
        cart_page.shouldnt_be_any_product_in_a_cart()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        product_link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, product_link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_product_details()


class TestGuestInteractsWithLogin:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


class TestNegativeCheckFromProductPage:
    @pytest.mark.xfail(reason="AssertionError: Success message is presented, but should not be")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, product_link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="AssertionError: Success message is not disappeared after adding product to basket")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, product_link)
        page.open()
        page.add_to_basket()
        page.should_disappear_success_message()
