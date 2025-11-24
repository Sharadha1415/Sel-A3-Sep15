import time

'''
text    :   It is a property of a web-element.
            It gives the text of the web-element.
            SYNTAX  :   element = driver.find_element('loc_name', 'loc_value')
                        print(element.text)
'''

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
# men = driver.find_element('xpath', '//a[@data-group="men"]')
# print(men.text)
#
# home = driver.find_element('xpath', '//a[@data-group="home"]')
# print(home.text)
#
# beauty = driver.find_element('xpath', '//a[@data-group="beauty"]')
# print(beauty.text)

##################################################################################

'''
get_attribute   :   It is an attribute of the web-element, it gives the attribute value of attribute names passed
'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/')
time.sleep(2)

beauty = driver.find_element('xpath', '(//a[text()="Beauty"])[1]')
print(beauty.get_attribute('href'))
print(beauty.get_attribute('class'))
print(beauty.get_attribute('style'))
print(beauty.get_attribute('data-type'))








