'''
class name  :   If we are having "class" attribute, then we can go for "class name" locator


    DRAWBACKS
    *   class name is not unique
        Incase of multiple occurances, class name will always consider the first occurance
    *   It cannot locate spaces
        Whenever we have space in the value of the class attribute, we should replace the space with dot(.)

'''

import time

## Eg1
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

driver.find_element('class name', 'ico-register').click()
time.sleep(2)
driver.find_element('class name', 'ico-login').click()
time.sleep(2)
driver.find_element('class name', 'ico-cart').click()

##############################################################################

## Eg2

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\css_selector.html')
time.sleep(2)

driver.find_element('class name', 'first_row').send_keys('Shubhangi')
time.sleep(1)
driver.find_element('class name', 'first_row').send_keys('Vibha')
time.sleep(1)
driver.find_element('class name', 'first_row').send_keys('Solai')

##############################################################################

## Eg3

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element('class name', 'inputtext _58mg _5dba _2ph-').send_keys('Misbah')

## ERROR
## Because class name locator cannot recognize the spaces

##------------------------------------------------------------------------------------------------

## To overcome this drawback, we will replace the space with dot(.)

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element('class name', 'inputtext._58mg._5dba._2ph-').send_keys('Misbah')

























