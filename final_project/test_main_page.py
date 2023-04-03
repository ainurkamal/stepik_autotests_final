from .pages.main_page import MainPage
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    browser.get(link)
    page.open()
    page.go_to_login_page()