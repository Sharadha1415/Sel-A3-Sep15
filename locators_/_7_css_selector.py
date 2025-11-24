'''
css selector    :   To locate the web-elements using any attribute
                    SYNTAX  :   tagname[attr_name="attr_value"]

                    DRAWBACKS
                    *   Indexing is not possible in css selector.
                        If we have multiple occurances, css selector will always consider the first occurance
                    *   Cannot locate text using css selector

'''
import time

# ## Eg1
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
# driver.find_element('css selector', 'input[placeholder="Username"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('css selector', 'input[type="password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('css selector', 'input[type="submit"]').click()


#############################################################################################

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
# driver.find_element('css selector', 'input[name="firstname"]').send_keys('Harry')
# time.sleep(1)
# driver.find_element('css selector', 'input[name="lastname"]').send_keys('Potter')
# time.sleep(1)
# driver.find_element('css selector', 'input[value="2"]').click()
# time.sleep(1)
# driver.find_element('css selector', 'input[name="reg_email__"]').send_keys('harry@gmail.com')
# time.sleep(1)
# driver.find_element('css selector', 'input[name="reg_passwd__"]').send_keys('harry@123545')
#
#
# #############################################################################################
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('css selector', 'a[data-group="men"]').click()
# time.sleep(2)
# driver.find_element('css selector', 'a[data-group="kids"]').click()
# time.sleep(2)
# driver.find_element('css selector', 'a[data-group="beauty"]').click()

#############################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)
driver.find_element('css selector', 'input[type="text"]').send_keys('Harry')
time.sleep(1)
driver.find_element('css selector', 'input[type="text"]').send_keys('Potter')

## The data will be filled in the same textbox






























