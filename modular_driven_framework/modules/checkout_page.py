import time

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_fname(self):
        self.driver.find_element('xpath', '//input[@id="first-name"]').send_keys('Deepak')
        time.sleep(1)

    def enter_lname(self):
        self.driver.find_element('xpath', '//input[@id="last-name"]').send_keys('suvarna')
        time.sleep(1)

    def enter_postalcode(self):
        self.driver.find_element('xpath', '//input[@id="postal-code"]').send_keys('560003')
        time.sleep(2)

    def click_continue(self):
        self.driver.find_element('xpath', '//input[@id="continue"]').click()
        time.sleep(2)

    def click_finish(self):
        self.driver.find_element('xpath', '//button[@id="finish"]').click()
        time.sleep(2)

    def back_home(self):
        self.driver.find_element('xpath', '//button[text()="Back Home"]').click()
        time.sleep(2)
