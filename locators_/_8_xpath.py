'''
xpath   :   It is a locator used to locate any element on the application uniquely
            We can locate the elements using attributes, we can locate elements using text, indexing is possible,
            can locate dynamically changing elements
            We can locate any element on the web-application using xpath

There are 2 types of xpath
*   absolute xpath  :   Starts from the root of html
*   relative xpath

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
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\css_selector_dup.html')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/input[1]').send_keys('Vibha')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/input[2]').send_keys('vibha@12345')

###############################################################################################

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
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/input').click()


###############################################################################################
'''
attribute name and value    :   //tagname[@attr_name="attr_value"]
'''

# ## Eg1
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
# driver.find_element('xpath', '//a[@class="ico-register"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="gender-male"]').click()
# driver.find_element('xpath', '//input[@id="FirstName"]').send_keys('James')
# driver.find_element('xpath', '//input[@id="LastName"]').send_keys('Watt')
# driver.find_element('xpath', '//input[@id="Email"]').send_keys('james@gmail.com')
# driver.find_element('xpath', '//input[@id="Password"]').send_keys('james@12345')
# driver.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('james@12345')

###################################################################################################

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
# driver.find_element('xpath', '//input[@name="firstname"]').send_keys('John')
# driver.find_element('xpath', '//input[@name="lastname"]').send_keys('Snow')
# driver.find_element('xpath', '//input[@value="2"]').click()
# driver.find_element('xpath', '//input[@name="reg_email__"]').send_keys('john@gmail.com')
# driver.find_element('xpath', '//input[@type="password"]').send_keys('john@12345')

###################################################################################################

# ## Eg3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="name"]').send_keys('John Snow')
# driver.find_element('xpath', '//input[@id="email"]').send_keys('john@gmail.com')
# driver.find_element('xpath', '//input[@id="phone"]').send_keys('9080706050')
# driver.find_element('xpath', '//textarea[@id="textarea"]').send_keys('Bengaluru')
# driver.find_element('xpath', '//input[@id="male"]').click()
# driver.find_element('xpath', '//input[@id="friday"]').click()


###################################################################################################
'''
Group indexing
'''

# ## Eg1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# driver.find_element('xpath', '(//input[@type="text"])[1]').send_keys('John')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[2]').send_keys('john@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[3]').send_keys('9080706050')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="radio"])[1]').click()
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="checkbox"])[6]').click()

###################################################################################################

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
# driver.find_element('xpath', '(//input[@class="inputtext _58mg _5dba _2ph-"])[1]').send_keys('Vivek')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@class="inputtext _58mg _5dba _2ph-"])[2]').send_keys('Samon')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@class="inputtext _58mg _5dba _2ph-"])[5]').send_keys('vivek@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@class="inputtext _58mg _5dba _2ph-"])[7]').send_keys('vivek@123456')
#
# ###################################################################################################
#
# ## Eg3
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
# driver.find_element('xpath', '(//a[@class="desktop-main"])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[4]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[5]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[6]').click()

###################################################################################################
'''
text    :   //tagname[text()="text"]
'''

# ## Eg1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.flipkart.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Electronics"]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//span[text()="Become a Seller"])[1]').click()
# time.sleep(2)
# driver.find_element('xpath', '//button[text()="Start Selling"]').click()
#
# ###################################################################################################
#
# ## Eg2
#
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
# driver.find_element('xpath', '//a[text()="Bestsellers"]').click()
# time.sleep(2)
# driver.find_element('xpath', '''//a[text()="Today's Deals"]''').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Mobiles"]').click()


# ###################################################################################################
'''
contains    :   This is another type of relative xpath where we can locate the element using its partial text of any tagname
                STNTAX  :   //tagname[contains(text(), "partial_text)]
'''

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.giva.co/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[contains(text(), "Gold with Lab Diamonds")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "GIVA Gift Card")]').click()
#
# ###################################################################################################
#
# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.kushals.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[contains(text(), "Accessories")])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Wedding Store")])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Happy Customers")])[2]').click()


###################################################################################################

'''
Dependent-independent xpath
*   Identify the dependent and independent elements
*   Write the xpath of the independent element
*   Traverse back until we get the common match for dependent-independent element
*   Continue writing the xpath for the dependnnet element

'''

'''
Eg1. wap to click on the checkbox of Ruby in demo.html
'''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Ruby"]/..//input[@type="checkbox"]').click()

###################################################################################################
#
'''
Eg2.    wap to click on the download link of windows in demo.html
'''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Windows"]/..//a[text()="Download"]').click()

###################################################################################################

'''
Eg3.    wap to click on the release notes of python 3.13.4 in https://www.python.org/
'''
#
# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[text()="Downloads"])[1]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Python 3.13.4"]/../..//a[text()="Release Notes"]').click()

# driver.find_element('xpath', '//td[text()="Windows"]/..//a[text()="Download"]').click()

###################################################################################################

'''
Eg4.    wap to print the sellprice and buyprice of gold in https://www.iforex.in/tools/live-rates   
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.iforex.in/tools/live-rates')
# time.sleep(2)
#
# ## gives a register pop-up
# ## closing the register pop-up
# driver.find_element('xpath', '(//div[@id="ai-chat-bubble-close"])[2]').click()
# time.sleep(4)
#
# gold_sellprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[2]')
# print(f'The sellprice of gold is {gold_sellprice.text}')
#
# gold_buyprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[3]')
# print(f'The buy price of gold is {gold_buyprice.text}')


###################################################################################################
'''
Eg5.    wap to print the price of MRF in https://in.tradingview.com/
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://in.tradingview.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Search"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="query"]').send_keys('MRF')
# time.sleep(2)
#
# driver.find_element('xpath', '(//button[@aria-label="Search"])[3]').click()
# time.sleep(2)
#
# mrf_price = driver.find_element('xpath', '//span[text()="MRF"]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
# print(mrf_price.text)

#####################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

##-------------------------------------------------------------------------------------------

'''
Parent --> Child
Locate_parent/child
parent//child

# '''
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
# ele = driver.find_element('xpath', '//div[@class="block block-category-navigation"]//a[contains(text(), "Books")]')
#
# ## -------------------------------------------------------------------------------------------
#
# driver.get('https://www.amazon.in/')
# driver.find_element('xpath', '//div[@class="nav-search-field "]/input')

#####################################################################################

'''
child --> parent
'''

# driver.get('https://www.instagram.com/')
# driver.find_element('xpath', '//input[@name="username"]/..')        ## go back to one parent(label)
# driver.find_element('xpath', '//input[@name="username"]/../..')     ## go back to twice(parent of label)

#
# driver.get('https://www.instagram.com/')
# driver.find_element('xpath', '//input[@name="username"]/parent::label')     ## takes to the immediate parent

#####################################################################################
'''
siblings
'''

# driver.get('https://demowebshop.tricentis.com/register')
# time.sleep(2)
#
# ## following sibling
# driver.find_element('xpath', '//label[text()="Email:"]/following-sibling::input')
#
# ## preceding sibling
# driver.find_element('xpath', '//input[@name="Email"]/preceding-sibling::label')

#####################################################################################
'''
ancestors
'''

driver.get('https://demowebshop.tricentis.com/register')
time.sleep(2)
driver.find_element('xpath', '//input[@name="Email"]/ancestor::div')

## If there are multiple occurances, we can index
driver.find_element('xpath', '//input[@name="Email"]/ancestor::div[n]')

#####################################################################################
'''
descendant
'''

# driver.get('https://demowebshop.tricentis.com/register')
# time.sleep(2)
#
# driver.find_element('xpath', '//div[@class="page registration-page"]//input')
#
# driver.find_element('xpath', '//div[@class="page registration-page"]/descendant::input')














