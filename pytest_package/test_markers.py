'''
To group the testcases, we use markers
There are 2 types
    *   custom markers
    *   inbuilt markers :   There are 4 types
                            *   skip
                            *   skipif
                            *   parametrize
                            *   xfail

'''
import time

import pytest

# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items / 2 deselected / 2 selected
# ## test_markers.py::test_reg       reg executing       PASSED
# ## test_markers.py::test_signup    signup executing    PASSED

####################################################################################

# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.smoke
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="smoke"                -->     test_reg and test_signup will execute
# ## pytest test_markers.py -vs -m="sanity"               -->     test_login will execute
# ## pytest test_markers.py -vs -m="regression"           -->     test_logout will execute
# ## pytest test_markers.py -vs -m="smoke and sanity"     -->     None
# ## pytest test_markers.py -vs -m="smoke and regression" -->     None
# ## pytest test_markers.py -vs -m="regression and sanity"-->     None
# ## pytest test_markers.py -vs -m="smoke or sanity"      -->     test_login, test_reg and test_signup will execute
# ## pytest test_markers.py -vs -m="smoke or regression"  -->     test_reg, test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="regression or sanity" -->     test_login and test_logout will execute
# ## pytest test_markers.py -vs -m="not smoke"            -->     test_login and test_logout will execute
# ## pytest test_markers.py -vs -m="not sanity"           -->     test_reg, test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="not regression"       -->     test_login, test_reg and test_signup will execute

####################################################################################

# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.regression
# @pytest.mark.smoke
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.sanity
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="smoke"                -->     test_login, test_reg, test_signup will execute
# ## pytest test_markers.py -vs -m="sanity"               -->     test_login, test_logout will execute
# ## pytest test_markers.py -vs -m="regression"           -->     test_signup, test_logout will execute
# ## pytest test_markers.py -vs -m="smoke and sanity"     -->     test_login will execute
# ## pytest test_markers.py -vs -m="smoke and regression" -->     test_signup will execute
# ## pytest test_markers.py -vs -m="regression and sanity"-->     test_logout will execute
# ## pytest test_markers.py -vs -m="smoke or sanity"      -->     all 4 will execute
# ## pytest test_markers.py -vs -m="smoke or regression"  -->     all 4 will execute
# ## pytest test_markers.py -vs -m="regression or sanity" -->     test_login, test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="not smoke"            -->     test_logout will execute
# ## pytest test_markers.py -vs -m="not sanity"           -->     test_reg, test_signup will execute
# ## pytest test_markers.py -vs -m="not regression"       -->     test_login, test_reg will execute

####################################################################################

# @pytest.mark.sanity
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
# ## pytest test_markers.py -vs -m="sanity"   --> All 4 will execute
#
# # ##############################################################################################################
# #
# @pytest.mark.regression
# class TestSample:
#
#     @pytest.mark.sanity
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     @pytest.mark.smoke
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")

####################################################################################

'''
skip    :   To skip the execution of the testcases, we use skip marker.
            It is an unconditional skip. To skip the testcase we dont have to pass any condition or reason
            It will just skip the execution of the testcases which are decorated with @pytest.mark.skip

            SYNTAX  :   @pytest.mark.skip
                        def test_func():
                            pass

'''

# def test_login():
#     print("login executing")
#
# @pytest.mark.skip
# def test_reg():
#     print("reg executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::test_login         login executing     PASSED
# ## test_markers.py::test_reg                               SKIPPED (unconditional skip)
# ## test_markers.py::test_signup        signup executing    PASSED
# ## test_markers.py::test_logout        logout executing    PASSED
#
# ####################################################################################

# def test_login():
#     print("login executing")
#
# @pytest.mark.skip
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.skip(reason="signup still in progress")
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::test_login         login executing         PASSED
# ## test_markers.py::test_reg                                   SKIPPED (unconditional skip)
# ## test_markers.py::test_signup                                SKIPPED (signup still in progress)
# ## test_markers.py::test_logout        logout executing        PASSED

# ####################################################################################

# @pytest.mark.skip
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
# ## test_markers.py::TestSample::test_login     SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_signup    SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_logout    SKIPPED (unconditional skip)

'''
NOTE    :   When we decorate the entire class with @pytest.mark.skip, it will skip the execution of the entire class
            Execution of all the attributes will be skipped
'''

####################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.skip
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 3 items
# ## test_markers.py::TestSample::test_login     login executing         PASSED
# ## test_markers.py::TestSample::test_signup                            SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_logout    logout executing        PASSED

####################################################################################

'''
skipif  :   skipif is also used to skip the execution of the testcases, but the skip is based on a condition.
            It takes two parameters, condition and reason.
            condition is the first parameter, reason is the second parameter.
            Both are mandatory parameters
            
            SYNTAX  :   @pytest.mark.skipif(condition, reason)
                        def test_case():
                            pass
                        
                        If the condition is True, it will skip the execution of the testcase
                        If the condition is False, it will execute the testcase 
            
'''

# @pytest.mark.skipif(True, reason='login already done')
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login         SKIPPED (login already done)
#
# ##############################################################
#
# @pytest.mark.skipif(False, reason='login already done')
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login         login executing         PASSED

###############################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# def test_login():
#     driver.find_element('id', "user-name").send_keys('standard_user')
#     time.sleep(1)
#     driver.find_element('id', 'password').send_keys('secret_sauceee')
#     time.sleep(1)
#     driver.find_element('id', 'login-button').click()
#     time.sleep(3)
#     url = driver.current_url
#     print(url)
#
# def test_logout():
#     if 'inventory' not in driver.current_url:
#         pytest.skip("login failed")
#     driver.find_element('id', 'react-burger-menu-btn').click()
#     time.sleep(2)
#     driver.find_element('id', 'logout_sidebar_link').click()

####################################################################################

'''
xfail   :   This is an expected failure

            SYNTAX  :   @pytest.mark.xfail
                        def test_func():
                            pass  
                        
                        We are expecting the test_func to fail.
                        If the testcase is failed, then the output will be XFAIL
                        If the testcase is passed, then the output will be XPASS
'''



# def test_case1():
#     print("tc1 executing")
#
# @pytest.mark.xfail
# def test_case2():           ## expecting failure
#     prt("tc2 executing")
#
# def test_case3():
#     prin("tc3 executing")
#
# def test_case4():
#     pnt("tc4 executing")
#
# ## collected 4 items
# ## test_markers.py::test_case1     tc1 executing       PASSED
# ## test_markers.py::test_case2                         XFAIL
# ## test_markers.py::test_case3                         FAILED
# ## test_markers.py::test_case4                         FAILED

####################################################################################

# def test_case1():
#     print("tc1 executing")
#
# @pytest.mark.xfail
# def test_case2():
#     prt("tc2 executing")
#
# ## collected 2 items
# ## test_markers.py::test_case1     tc1 executing       PASSED
# ## test_markers.py::test_case2                         XFAIL

####################################################################################
#
# def test_case1():
#     print("tc1 executing")
#
# @pytest.mark.xfail
# def test_case2():
#     print("tc2 executing")
#
# ## collected 2 items
# ## test_markers.py::test_case1     tc1 executing       PASSED
# ## test_markers.py::test_case2     tc2 executing       XPASS

####################################################################################

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_obj = WebDriverWait(driver, 5)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# @pytest.mark.xfail
# def test_login():
#     driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
#     time.sleep(1)
#     driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauceeeee')
#     time.sleep(1)
#     driver.find_element('xpath', '//input[@id="login-button"]').click()
#     time.sleep(2)
#     wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))

####################################################################################
'''
parametrize     :   To pass parameters for the testcases, we use parametrize markers  
'''

# @pytest.mark.parametrize("a, b", [(10, 20)])
# def test_add(a, b):
#     print(a + b)
#
# ## collected 1 item
# ## test_markers.py::test_add[10-20]        30          PASSED

##----------------------------------------------------------------

# @pytest.mark.parametrize("a, b", [(10, 20), (1, 2), (-10, -10), (0, 9), (1, 20), (-2, 6)])
# def test_add(a, b):
#     print(a + b)
#
# ## collected 6 items
# ## test_markers.py::test_add[10-20]    30      PASSED
# ## test_markers.py::test_add[1-2]      3       PASSED
# ## test_markers.py::test_add[-10--10] -20      PASSED
# ## test_markers.py::test_add[0-9]      9       PASSED
# ## test_markers.py::test_add[1-20]     21      PASSED
# ## test_markers.py::test_add[-2-6]     4       PASSED

## ----------------------------------------------------------------

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

@pytest.mark.parametrize("username, pwd", [('standard_user', 'secret_sauce'), ('standard', 'secret'), ('hihello', '123456')])
def test_login(username, pwd):
    driver.get('https://www.saucedemo.com/')
    time.sleep(2)
    driver.find_element('id', "user-name").send_keys(username)
    time.sleep(1)
    driver.find_element('id', 'password').send_keys(pwd)
    time.sleep(1)
    driver.find_element('id', 'login-button').click()
    time.sleep(3)

    if 'inventory' in driver.current_url:
        print("succesfull login")
    else:
        print("unsuccesfull login")




























