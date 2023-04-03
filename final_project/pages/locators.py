from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_URL_SUBSTRING = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")