import time
import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


promoes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
@pytest.mark.parametrize('promo_num', promoes)
@pytest.mark.xfail(reason="AssertionError with success message on offer7")
def test_guest_can_add_product_to_basket(browser, promo_num):
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_num}"
    page = ProductPage(browser, product_link)
    page.open()

    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(2)


    product_name = page.get_product_name()
    assert page.is_element_present(
        *ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not present"
    assert page.is_element_present(
        *ProductPageLocators.PRODUCT_NAME), "Product name is not present"
    assert page.is_element_present(
        *ProductPageLocators.PRODUCT_PRICE), "Product price is not present"
    assert page.get_success_message() == product_name, "Success message is not equal to product name"
