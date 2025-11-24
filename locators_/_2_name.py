'''
name    :   name is an attribute which is also a locator.
            So if we have name attribute, then we can go for name locator

            DRAWBACKS
            *   name is not unique
            *   Incase of multiple occurances, name will always consider the first occurance

'''

import time

# ## Eg1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/')
# time.sleep(2)
# driver.find_element('name', 'username').send_keys('sherlock_holmes')
# time.sleep(1)
# driver.find_element('name', 'password').send_keys('sherlock@12345')

##############################################################################################

# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('name', 'firstname').send_keys('Hermoine')
# time.sleep(1)
# driver.find_element('name', 'lastname').send_keys('Granger')
# time.sleep(1)
# driver.find_element('name', 'sex').click()
# time.sleep(1)
# driver.find_element('name', 'reg_email__').send_keys('hermoine@gmail.com')
# time.sleep(1)
# driver.find_element('name', 'reg_passwd__').send_keys('hermoine@12345')

##############################################################################################

## Eg3

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\css_selector.html')
time.sleep(2)

driver.find_element('name', 'fname').send_keys('Sneha')
time.sleep(1)
driver.find_element('name', 'fname').send_keys('Solai')
time.sleep(1)
driver.find_element('name', 'fname').send_keys('Vibha')

## ALl the above data will be filled in the first textbox






















