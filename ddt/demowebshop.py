import time
from reading_excel import excel_read

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

data = excel_read()
print(data)     ## {'firstname': 'James', 'lastname': 'Watt', 'email_id': 'james@gmail.com', 'password': 'james@12345'}

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

driver.find_element('xpath', '//a[@class="ico-register"]').click()
time.sleep(2)
driver.find_element('xpath', '//input[@id="gender-male"]').click()
driver.find_element('xpath', '//input[@id="FirstName"]').send_keys(data['firstname'])
driver.find_element('xpath', '//input[@id="LastName"]').send_keys(data['lastname'])
driver.find_element('xpath', '//input[@id="Email"]').send_keys(data['email_id'])
driver.find_element('xpath', '//input[@id="Password"]').send_keys(data['password'])
driver.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys(data['password'])


























