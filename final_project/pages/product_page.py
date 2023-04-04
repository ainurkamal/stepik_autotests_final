from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*self.PRODUCT_NAME).text
        return product_name

    def get_product_price(self):
        product_price = self.browser.find_element(*self.PRODUCT_PRICE).text
        return product_price
