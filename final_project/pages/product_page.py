from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.ADD_TO_BASKET_BUTTON))
        add_to_basket_button.click()

    def get_product_name(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_product_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def get_success_message(self):
        success_message = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE).text
        return success_message

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Message is not disappeared, but should"

    def check_product_details(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not present"
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME), "Product name is not present"
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE), "Product price is not present"

        product_name = self.get_product_name()
        assert self.get_success_message() == product_name, \
            "Success message is not equal to product name"

    def check_user_cant_see_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
