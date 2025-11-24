import time

class TestRegister:

    def test_reg(self, setup):      ## setup --> driver
        setup.find_element('xpath', '//a[@class="ico-register"]').click()
        time.sleep(2)

    def test_gender(self, setup):
        setup.find_element('xpath', '//input[@id="gender-male"]').click()

    def test_fname(self, setup):
        setup.find_element('xpath', '//input[@id="FirstName"]').send_keys('James')

    def test_lname(self, setup):
        setup.find_element('xpath', '//input[@id="LastName"]').send_keys('Thor')

    def test_reg_email(self, setup):
        setup.find_element('xpath', '//input[@id="Email"]').send_keys('thor@gmail.com')

    def test_reg_pwd(self, setup):
        setup.find_element('xpath', '//input[@id="Password"]').send_keys('thor@12345')

    def test_confirm_pwd(self, setup):
        setup.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('thor@12345')
        time.sleep(2)

