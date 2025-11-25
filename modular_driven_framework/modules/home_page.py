import time


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element('xpath', '//div[text()="Sauce Labs Backpack"]/../../..//button[text()="Add to cart"]').click()
        time.sleep(2)

    def clik_cart_icon(self):
        self.driver.find_element('xpath', '//a[@class="shopping_cart_link"]').click()
        time.sleep(2)

    def open_menu(self):
        self.driver.find_element('xpath', '//button[text()="Open Menu"]').click()
        time.sleep(2)

    def logout_link(self):
        self.driver.find_element('xpath', '//a[@id="logout_sidebar_link"]').click()










