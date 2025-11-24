# def login():
#     print("login executing")
#
# def logout():
#     print("logout executing")
#
# login()
# logout()
#
## To execute the function, we should give the function call
#
# ##################################################################################

# class Sample:
#
#     def login(self):
#         print("login executing")
#
#     def logout(self):
#         print("logout executing")
#
# sample_obj = Sample()
# sample_obj.login()
# sample_obj.logout()
#
# ## create the object and call the attributes

##################################################################################

'''
Pytest  :   It is a unit testing framework.
            Testing the small portion of the entire code, we call it as unit testing.
            To perform unit testing in selenium we will go for Pytest

            To install pytest
            Go to command prompt -->    pip install pytest

            RULES
            *   The file_name should always start with test_
                Eg  :   test_filename.py
            *   The function names also should start with test_
                Eg  :   def test_funcname():
                            pass
            *   The class names should start with Test
                Eg  :   class TestClassName:
                            pass

            Pytest will automatically recognize the files, functions and the classes which are following the pytest rules.
            So, without giving the function call, we can execute the functions and without creating the objects and
                without calling the attributes, we can execute the classes

            To execute the pytest file
            Right click anywhere on the test_file --> open in --> terminal --> pytest test_filename.py -vs
                -v  --> Verbosity. This gives the detailed explanation about the code.
                -s  --> Scripting. This prints all the print statements

'''

# def test_login():
#     print("login executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_basics.py::test_login      login executing         PASSED
# ## test_basics.py::test_logout     logout executing        PASSED
#
# ###############################################################################################
#
# def test_login():
#     print("login executing")
#
# def signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_basics.py::test_login      login executing     PASSED
# ## test_basics.py::test_logout     logout executing    PASSED

'''
signup will not execute because it is not following the pytest rules.
pytest cannot recognize the fuctions which are not following the rules 
'''

################################################################################################

# def test_login():
#     print("login executing")
#     def test_logout():
#         print("logout executing")
#
# ## collected 1 item
# ## test_basics.py::test_login      login executing      PASSED

'''
Incase of nested test_functions, pytest cannot recognize the inner test_function. 
pytest can only recognize the outer most test_function
'''

################################################################################################

# def test_login():
#     raise Exception
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_basics.py::test_login                              FAILED
# ## test_basics.py::test_signup     signup executing        PASSED
# ## test_basics.py::test_logout     logout executing        PASSED

'''
NOTE    :   Error in one test_case will not affect the execution of the other testcases
'''

################################################################################################

# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# test_login()
# test_signup()
# test_logout()
#
# ## collecting ... login executing
# ## signup executing
# ## logout executing
# ## collected 3 items
# ## test_basics.py::test_login      login executing         PASSED
# ## test_basics.py::test_signup     signup executing        PASSED
# ## test_basics.py::test_logout     logout executing        PASSED

'''
NOTE    :   When we call the test_functions, execution will happen twice
'''

################################################################################################

# def test_add(a, b):
#     print(a + b)
#
# ## collected 1 item
# ## test_basics.py::test_add          ERROR

'''
NOTE    :   test_functions donot take any parameters
'''

################################################################################################

# def test_login():
#     print("hello world")
#
# def test_login():
#     print("hello universe")
#
# ## collected 1 item
# ## test_basics.py::test_login          hello universe              PASSED

'''
NOTE    :   If we are having multiple test functions with the same test function name, then pytest will always
            consider the latest occurance
'''

################################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 3 items
# ## test_basics.py::TestSample::test_login      login executing         PASSED
# ## test_basics.py::TestSample::test_signup     signup executing        PASSED
# ## test_basics.py::TestSample::test_logout     logout executing        PASSED


################################################################################################

# class Sample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 0 items
'''
classname is not following the pytest rules
'''

################################################################################################

# class TestSample:
#
#     def login(self):
#         print("login executing")
#
#     def signup(self):
#         print("signup executing")
#
#     def logout(self):
#         print("logout executing")
#
# ## collected 0 items

'''
The attributes are not following the rules
'''

################################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# s = TestSample()
# s.test_login()
# s.test_signup()
# s.test_logout()
#
# ## collecting ... login executing
# ## signup executing
# ## logout executing
# ## collected 3 items
# ## test_basics.py::test_login      login executing         PASSED
# ## test_basics.py::test_signup     signup executing        PASSED
# ## test_basics.py::test_logout     logout executing        PASSED

################################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         pri("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 3 items
# ## test_basics.py::TestSample::test_login      login executing         PASSED
# ## test_basics.py::TestSample::test_signup                             FAILED
# ## test_basics.py::TestSample::test_logout     logout executing        PASSED

################################################################################################

# class TestSample:
#
#     def test_login(self, name):
#         print("login executing")
#
# ## collected 1 item
# ## test_basics.py::TestSample::test_login       ERROR

'''
test_methods also donot take any parameters 
'''

################################################################################################
#
# class TestSample:
#
#     def __init__(self):
#         pass
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
# ## collected 0 items
# ## PytestCollectionWarning: cannot collect test class 'TestSample' because it has a __init__ constructor

################################################################################################

import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

class TestRegister:

    def test_reg(self):
        driver.find_element('xpath', '//a[@class="ico-register"]').click()
        time.sleep(2)

    def test_gender(self):
        driver.find_element('xpath', '//input[@id="gender-male"]').click()

    def test_fname(self):
        driver.find_element('xpath', '//input[@id="FirstName"]').send_keys('James')

    def test_lname(self):
        driver.find_element('xpath', '//input[@id="LastName"]').send_keys('Thor')

    def test_reg_email(self):
        driver.find_element('xpath', '//input[@id="Email"]').send_keys('thor@gmail.com')

    def test_reg_pwd(self):
        driver.find_element('xpath', '//input[@id="Password"]').send_keys('thor@12345')

    def test_confirm_pwd(self):
        driver.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('thor@12345')


class TestLogin:

    def test_login(self):
        driver.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(2)

    def test_login_email(self):
        driver.find_element('xpath', '//input[@id="Email"]').send_keys('thor@gmail.com')

    def test_login_pwd(self):
        driver.find_element('xpath', '//input[@id="Password"]').send_keys('thor@12345')


































