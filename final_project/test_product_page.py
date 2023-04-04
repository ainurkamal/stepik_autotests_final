from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    # Arrange
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, product_link)
    page.open()

    # Act
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    # Assert
    product_name = page.get_product_name()
    assert page.is_element_present(*ProductPage.ADD_TO_BASKET_BUTTON), "Add to basket button is not present"
    assert page.is_element_present(*ProductPage.PRODUCT_NAME), "Product name is not present"
    assert product_name == "The shellcoder's handbook", "Incorrect product name in the message"
    assert page.is_element_present(*ProductPage.PRODUCT_PRICE), "Product price is not present"
