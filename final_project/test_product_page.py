import time
import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


promoes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
@pytest.mark.parametrize('promo_num', promoes)
@pytest.mark.xfail(reason="AssertionError with success message on offer7")
def test_guest_can_add_product_to_basket(browser, promo_num):
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_num}"
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


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    # открываем нужную страницу
    page.open()
    # выполняем метод страницы: переходим на страницу логина
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    # проверка, что перешли действительно на страницу логина
    login_page.should_be_login_page()
