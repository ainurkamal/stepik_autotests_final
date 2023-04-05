from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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
