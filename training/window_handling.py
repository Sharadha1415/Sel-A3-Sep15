'''
In web automation, sometimes actions open a new browser window or tab (e.g., clicking a link, pop-up, advertisement, or login window).
Selenium initially controls only the main window where the driver started.
To interact with other windows/tabs, we need to switch between them.

Window Handles
    Every window or tab opened by the browser has a unique ID, called a window handle.
    Selenium provides methods to get and switch between these handles.
    handles = driver.window_handles     ## Returns a list of handles for all open windows/tabs.

    To switch the driver to the window
    driver.switch_to.window(handles[index_num])

'''

import time

# ## Eg1
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# handles = driver.window_handles
# print(handles)
#
# ## scroll down till the end of the application
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(2)
#
# ## clicking on google+
# driver.find_element('xpath', '//a[text()="Google+"]').click()           ## opens in a new tab
# time.sleep(2)
#
# ## Initalizing window_handles
# handles2 = driver.window_handles
# print(handles2)             ## list of handles          ##  [parent_handle, child_handle]
#
# ## handles2[0] --> parent_handle, By default driver will be present on the parent handle
# ## handles2[1] --> child_handle
#
# ## switching the driver to the child handle
# driver.switch_to.window(handles2[1])
# time.sleep(2)
#
# ## entering the data to the searchbox
# driver.find_element('xpath', '//input[@class="header__search"]').send_keys('Google pixel')
# time.sleep(2)
#
# ## switch to the parent tab
# driver.switch_to.window(handles2[0])
# time.sleep(2)
#
# ## clicking on youtube
# driver.find_element('xpath', '//a[text()="YouTube"]').click()       ## opens in new tab
# time.sleep(2)
#
# ## Initalizing window_handles
# handles3 = driver.window_handles
# print(handles3)             ## [parent, child1, child2]
#
# ## switching the driver to the child2 handle
# driver.switch_to.window(handles3[2])
# time.sleep(2)
#
# ##
# driver.find_element('xpath', '//input[@name="search_query"]').send_keys('Leo')

#################################################################################################################

## Eg2

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)

driver.get('https://www.myntra.com/')
time.sleep(2)

## Hovering to the Home
home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
ac_obj.move_to_element(home).perform()
time.sleep(2)

## clicking on festive decor
driver.find_element('xpath', '//a[text()="Festive Decor"]').click()
time.sleep(2)

## click on the product
driver.find_element('xpath', '//h4[@class="product-product"]').click()      ## opens in a new tab
time.sleep(2)

## Initialize window handles
handles = driver.window_handles
print(handles)          ## [parent, child]

## switch the driver to the child handle
driver.switch_to.window(handles[1])
time.sleep(2)

## perform the operations in the child tab
driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
time.sleep(2)

## switch back to the parent tab
driver.switch_to.window(handles[0])
time.sleep(2)

##
driver.find_element('xpath', '(//h4[@class="product-product"])[2]').click()     ## opens in a new tab
time.sleep(2)

## Initialize window handles
handles2 = driver.window_handles
print(handles2)          ## [parent, child1, child2]

## switch the driver to the child2
driver.switch_to.window(handles2[2])
time.sleep(2)

## perform the operations in the child2 tab
driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
time.sleep(2)








