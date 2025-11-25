import time
from selenium import webdriver
from modular_driven_framework.modules.login_page import LoginPage
from modular_driven_framework.modules.home_page import HomePage
from modular_driven_framework.modules.cart_page import CartPage
from modular_driven_framework.modules.checkout_page import CheckoutPage

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.saucedemo.com/')
time.sleep(1)


def test_demo():
    login = LoginPage(driver)
    home = HomePage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    login.enter_username()
    login.enter_password()
    login.click_login_btn()
    home.add_to_cart()
    home.clik_cart_icon()
    cart.click_on_checkout()
    checkout.enter_fname()
    checkout.enter_lname()
    checkout.enter_postalcode()
    checkout.click_continue()
    checkout.click_finish()
    checkout.back_home()
    home.open_menu()
    home.logout_link()












