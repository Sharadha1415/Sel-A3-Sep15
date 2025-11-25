import time


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_checkout(self):
        self.driver.find_element('xpath', '//a[@class="shopping_cart_link"]').click()
        time.sleep(2)