'''
assert  :   It is a keyword.
            It is used to validate the expected output with the actual output.
            assert will take a condition

            SYNTAX  :   assert condition

            If the condition is True, the test case passes and the execution will continue
            If the condition is False, then it will always give AssertionError
'''

import time

# assert 10%2==0
# print("hello world")
#
# ## output --> hello world

##---------------------------------------------------------------------------------------

# assert 11%2==0
# print("hello world")
#
# ## output --> AssertionError

##---------------------------------------------------------------------------------------

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

ele1 = driver.find_element('xpath', '(//a[contains(text(), "Books")])[1]')
ele2 = driver.find_element('xpath', '(//a[contains(text(), "Books")])[2]')

assert ele1.is_displayed()
assert ele2.is_displayed()





















