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
get_attribute   :   It is used to retrieve the full value of any attribute of a web-element
                    SYNTAX  :   web_element.get_attribute("attr_name")
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
# beauty = driver.find_element('xpath', '(//a[text()="Beauty"])[1]')
# print(beauty.get_attribute('href'))
# print(beauty.get_attribute('class'))
# print(beauty.get_attribute('style'))
# print(beauty.get_attribute('data-type'))

##################################################################################

'''
is_enabled  :   It is used to check whether the element is enabled or disabled on the web-page
                If the element is enabled, then it will give True
                If the element is disabled, then it will give False.
                SYNTAX  :   web_element.is_enabled()
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/accounts/emailsignup/')
# time.sleep(2)
#
# signup = driver.find_element('xpath', '//button[text()="Sign up"]')
# print(signup.is_enabled())
#
# fb = driver.find_element('xpath', '//button[text()="Log in with Facebook"]')
# print(fb.is_enabled())


##################################################################################

'''
is_displayed  :   It is used to check whether the element is displayed or not
                If the element is displayed, then it will give True
                If the element is not displayed, then it will give False.
                SYNTAX  :   web_element.is_displayed()
'''

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
# ele1 = driver.find_element('xpath', '(//a[contains(text(), "Books")])[1]')
# print(ele1.is_displayed())      ## True
#
# ele2 = driver.find_element('xpath', '(//a[contains(text(), "Books")])[2]')
# print(ele2.is_displayed())      ## False

##################################################################################
'''
get_dom_attribute   :   It retrieves the attribute value exactly as it is visible in the DOM 
                        SYNTAX  :   web_element.get_dom_attribute("attr_name")
'''

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
# reg = driver.find_element('xpath', '//a[text()="Register"]')
# print(reg.get_attribute('href'))            ## https://demowebshop.tricentis.com/register
# print(reg.get_dom_attribute('href'))        ## /register

##################################################################################
'''
tag_name    :   It is a property. It is used to get the tagname of a web_element.
                Eg  :   a, div, span, p, etc,...
'''

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
# reg = driver.find_element('xpath', '//a[text()="Register"]')
# print(reg.tag_name)

##################################################################################
'''
To Take the screenshot of a web-element, we have screenshot() attribute
    SYNTAX  :   web_element.screenshot("ss_name.png")
                By default the screenshot will be saved in the same location as our python file

To store the screenshot in different location
    SYNTAX  :   web_element.screenshot("location\ss_name.png")

'''

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
# reg = driver.find_element('xpath', '//a[text()="Register"]')
# newsletter = driver.find_element('xpath', '//strong[text()="Newsletter"]')
#
# reg.screenshot(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\screenshots_\reg_ss.png')
# newsletter.screenshot(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\screenshots_\newsletter_ss.png')

##################################################################################
'''
is_selected
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/register')
# time.sleep(2)
#
# gender_btn = driver.find_element('id', 'gender-male')
# print(gender_btn.is_selected())         ## False
# time.sleep(2)
#
# gender_btn.click()
# time.sleep(1)
# print(gender_btn.is_selected())         ## True

##################################################################################
'''
clear   :   
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/register')
# time.sleep(2)
#
# firstname = driver.find_element('id', 'FirstName')
# firstname.send_keys('Jayashree')
# time.sleep(2)
# firstname.clear()
# time.sleep(2)
#
# lastname = driver.find_element('id', 'LastName')
# lastname.send_keys('Shree')
# time.sleep(2)
# lastname.clear()

##################################################################################
'''
submit   :   
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/register')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="register-button"]').submit()


#################################################################################################














































