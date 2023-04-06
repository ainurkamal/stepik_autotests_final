from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def shouldnt_be_any_product_in_a_cart(self):
        substring = BasketPageLocators.SUBSTRING_BASKET_EN_GB
        assert substring in self.browser.find_element(
            *BasketPageLocators.BASKET_EMPTY).text, "No message of empty basket!"
