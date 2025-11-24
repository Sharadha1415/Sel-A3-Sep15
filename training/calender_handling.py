import time


# ## solution1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.makemytrip.com/')
# driver.maximize_window()
# time.sleep(2)
#
# ## closing the login form
# driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
# time.sleep(2)
#
# ## click on departure
# driver.find_element('xpath', '//span[text()="Departure"]').click()
# time.sleep(2)
#
# while True:
#     try:
#         driver.find_element('xpath', '//div[text()="June 2026"]/../..//p[text()="10"]').click()
#         break
#     except:
#         driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()
#
# ###########################################################################################################
#
# ## Solution2
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.makemytrip.com/')           ## login form will appear
# driver.maximize_window()
# time.sleep(2)
#
# ## closing the login form
# driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
# time.sleep(2)
#
# ## click on departure
# driver.find_element('xpath', '//span[text()="Departure"]').click()
# time.sleep(2)
#
# while True:
#     month = driver.find_element('xpath', '(//div[@class="DayPicker-Caption"])[1]')
#     print(month.text)
#
#     if month.text == 'February 2026':
#         driver.find_element('xpath', '(//p[text()="20"])[1]').click()
#         break
#     else:
#         driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()


###########################################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.booking.com/')
time.sleep(2)
driver.find_element('xpath', '//span[text()="Check-in date"]').click()
time.sleep(2)

while True:
    try:
        driver.find_element('xpath', '//h3[text()="May 2026"]/..//span[text()="24"]').click()
        time.sleep(2)
        break
    except:
        driver.find_element('xpath', '//button[@aria-label="Next month"]').click()
    time.sleep(0.5)




























