# def outer(func):
#     def wrapper(*args, **kwargs):
#         print("Good afternoon")         ## pre-task
#         func(*args, **kwargs)           ## main function
#         print("Good evening")           ## post-task
#     return wrapper
#
#
# @outer      ## add = outer(add)
# def add(a, b, c):
#     print(a + b + c)
#
# add(1, 2, 3)                ## wrapper(1, 2, 3)
#
#
# @outer      ## sub = outer(sub)
# def sub(a, b):
#     print(a - b)
#
# sub(10, 20)

#################################################################################
import pytest

# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 2 items
# ## test_fixtures.py::test_login        Good morning        login executing     PASSED
# ## test_fixtures.py::test_logout       Good morning        logout executing    PASSED
#
#
# #################################################################################
#
# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::test_signup                       signup executing    PASSED
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSED
#
#
# #################################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup(greet):
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing         PASSEDGood evening
# ## test_fixtures.py::test_signup   Good morning        signup executing        PASSEDGood evening
# ## test_fixtures.py::test_logout   Good morning        logout executing        PASSEDGood evening

'''
The operations before yield will execute before the execution of the test_function
The operations after yield will execute after the execution of the test_function

setup       -->     The operations before yield
teardown    -->     The operations after yield
'''

# #################################################################################

# @pytest.fixture(autouse=True)
# def setup():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSEDGood evening
# ## test_fixtures.py::test_signup   Good morning        signup executing    PASSEDGood evening
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSEDGood evening

# #################################################################################

# @pytest.fixture(autouse=True)
# def setup():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 4 items
# ## test_fixtures.py::TestSample::test_login    Good morning        login executing     PASSEDGood evening
# ## test_fixtures.py::TestSample::test_reg      Good morning        reg executing       PASSEDGood evening
# ## test_fixtures.py::TestSample::test_signup   Good morning        signup executing    PASSEDGood evening
# ## test_fixtures.py::TestSample::test_logout   Good morning        logout executing    PASSEDGood evening

# #################################################################################

# @pytest.fixture()
# def setup():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self, setup):
#         print("login executing")
#
#     def test_reg(self, setup):
#         print("reg executing")
#
#     def test_signup(self, setup):
#         print("signup executing")
#
#     def test_logout(self, setup):
#         print("logout executing")
#
# # ## collected 4 items
# # ## test_fixtures.py::TestSample::test_login    Good morning        login executing     PASSEDGood evening
# # ## test_fixtures.py::TestSample::test_reg      Good morning        reg executing       PASSEDGood evening
# # ## test_fixtures.py::TestSample::test_signup   Good morning        signup executing    PASSEDGood evening
# # ## test_fixtures.py::TestSample::test_logout   Good morning        logout executing    PASSEDGood evening

# #################################################################################

# @pytest.fixture(scope='class')
# def setup():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self, setup):
#         print("login executing")
#
#     def test_reg(self, setup):
#         print("reg executing")
#
#     def test_signup(self, setup):
#         print("signup executing")
#
#     def test_logout(self, setup):
#         print("logout executing")
#
# ## collected 4 items
# ## test_fixtures.py::TestSample::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::TestSample::test_reg                          reg executing       PASSED
# ## test_fixtures.py::TestSample::test_signup                       signup executing    PASSED
# ## test_fixtures.py::TestSample::test_logout                       logout executing    PASSEDGood evening

# #################################################################################

# @pytest.fixture(scope='class')
# def setup():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self, setup):
#         print("login executing")
#
#     def test_reg(self, setup):
#         print("reg executing")
#
# class TestSpam:
#
#     def test_signup(self, setup):
#         print("signup executing")
#
#     def test_logout(self, setup):
#         print("logout executing")
#
# ## collected 4 items
# ## test_fixtures.py::TestSample::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::TestSample::test_reg                          reg executing       PASSEDGood evening
# ## test_fixtures.py::TestSpam::test_signup     Good morning        signup executing    PASSED
# ## test_fixtures.py::TestSpam::test_logout                         logout executing    PASSEDGood evening

# #################################################################################

# @pytest.fixture(scope='class')
# def setup():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# def test_signup(setup):
#     print("signup executing")
#
# class TestSample:
#
#     def test_login(self, setup):
#         print("login executing")
#
#     def test_reg(self, setup):
#         print("reg executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_signup               Good morning        signup executing        PASSEDGood evening
# ## test_fixtures.py::TestSample::test_login    Good morning        login executing         PASSED
# ## test_fixtures.py::TestSample::test_reg                          reg executing           PASSEDGood evening

# #################################################################################

# @pytest.fixture(scope='module')
# def setup():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# def test_signup(setup):
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# class TestSample:
#
#     def test_login(self, setup):
#         print("login executing")
#
#     def test_reg(self, setup):
#         print("reg executing")
#
# class TestSpam:
#
#     def test_google(self):
#         print("google executing")
#
#     def test_gmail(self):
#         print("gmail executing")
#
# ## collected 6 items
# ## test_fixtures.py::test_signup       Good morning    signup executing    PASSED
# ## test_fixtures.py::test_logout                       logout executing    PASSED
# ## test_fixtures.py::TestSample::test_login            login executing     PASSED
# ## test_fixtures.py::TestSample::test_reg              reg executing       PASSED
# ## test_fixtures.py::TestSpam::test_google             google executing    PASSED
# ## test_fixtures.py::TestSpam::test_gmail              gmail executing     PASSEDGood evening

# #################################################################################

import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Chrome(opts)
    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver
    driver.close()

## setup --> driver = webdriver.Chrome(opts)

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

class TestLogin:

    def test_login(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(2)

    def test_login_email(self, setup):
        setup.find_element('xpath', '//input[@id="Email"]').send_keys('thor@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('xpath', '//input[@id="Password"]').send_keys('thor@12345')
















































































