import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


@pytest.mark.xfail(reason="AssertionError: Success message is presented, but should not be")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # открываем страницу товара
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, product_link)
    page.open()

    # добавляем товар в корзину
    page.add_to_basket()

    # проверяем, что нет сообщения об успехе
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"


def test_guest_cant_see_success_message(browser):
    # открываем страницу товара
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, product_link)
    page.open()

    # проверяем, что нет сообщения об успехе
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"


@pytest.mark.xfail(reason="AssertionError: Success message is not disappeared after adding product to basket")
def test_message_disappeared_after_adding_product_to_basket(browser):
    # открываем страницу товара
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, product_link)
    page.open()

    # добавляем товар в корзину
    page.add_to_basket()

    # проверяем, что сообщение об успехе исчезает
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not disappeared after adding product to basket"

