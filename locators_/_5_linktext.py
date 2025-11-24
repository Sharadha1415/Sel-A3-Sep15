'''
link text   :   The text present between the anchor tag, we call it as link text.
                To locate the link text, we use "link text" locator

'''

import time

## Eg1
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/')
time.sleep(2)

driver.find_element('link text', 'Men').click()
time.sleep(2)
driver.find_element('link text', 'Kids').click()
time.sleep(2)
driver.find_element('link text', 'Beauty').click()


######################################################################################################

# ## Eg2
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.amazon.in/')
# time.sleep(2)
#
# driver.find_element('link text', 'Sell').click()
# time.sleep(2)
# driver.find_element('link text', 'Bestsellers').click()
# time.sleep(2)
# driver.find_element('link text', "Today's Deals").click()

######################################################################################################

# ## Eg3
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('link text', 'Register').click()
# time.sleep(2)
# driver.find_element('link text', 'Log in').click()


######################################################################################################



























