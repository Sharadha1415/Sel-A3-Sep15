import time

class TestLogin:

    def test_login(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(2)

    def test_login_email(self, setup):
        setup.find_element('xpath', '//input[@id="Email"]').send_keys('thor@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('xpath', '//input[@id="Password"]').send_keys('thor@12345')

