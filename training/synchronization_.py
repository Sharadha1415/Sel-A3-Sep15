import time

# ## using time.sleep()
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\loading.html')
# time.sleep(20)
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Jaya')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('shree')

#############################################################################################################

# ## implicit_wait
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\loading.html')
# driver.implicitly_wait(30)
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Jaya')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('shree')

# #############################################################################################################
#
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# time.sleep(40)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
#


#############################################################################################################


# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(45)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
#
# driver.find_element('xpath', '//div[text()="100%"]')
# time.sleep(2)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()

#############################################################################################################

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# wait_obj = WebDriverWait(driver, 20)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('id', 'user-name').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('id', 'password').send_keys('secret_sauceeeeeee')
# time.sleep(1)
# driver.find_element('id', 'login-button').click()
# time.sleep(2)
#
# try:
#     wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
#     print("Succesfull login")
# except:
#     print("Unsuccesfull login")


#############################################################################################################

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_obj = WebDriverWait(driver, 30)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\loading.html')

wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//div[contains(text(), "FirstName")]')))

driver.find_element('xpath', '//input[@name="fname"]').send_keys('Jaya')
time.sleep(1)
driver.find_element('xpath', '//input[@name="lname"]').send_keys('shree')
























