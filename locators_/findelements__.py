import time

'''
Eg1.    wap to enter the data for the textboxes present in demo.html
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\demo.html')
# time.sleep(2)
# all_textboxes = driver.find_elements('xpath', '//input[@name="fname"]')
# print(all_textboxes)            ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7, wb8, wb9]
#
# data_list = ['Friends', 'Bads', 'Modern family', 'flash', 'big bang theory', 'squid game', 'Suits', 'GOT', 'Money heist']
#
# for textbox, data in zip(all_textboxes, data_list):
#     textbox.send_keys(data)

#############################################################################################################
'''
Eg2
wap tp print the shoe name and shoe price of adidas original shoes in myntra
'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/')
time.sleep(2)

driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('adidas')
time.sleep(2)
driver.find_element('xpath', '//li[text()="Adidas Originals Shoes"]').click()
time.sleep(2)

shoe_names = driver.find_elements('xpath', '//h4[@class="product-product"]')        ## [shoe1, shoe2, shoe3,.., shoe50]
shoe_prices = driver.find_elements('xpath', '//div[@class="product-price"]')        ## [price1, price2, price3,..price50]

for shoe, price in zip(shoe_names, shoe_prices):
    print(shoe.text, '=', price.text)

#############################################################################################################
'''
Eg3.    wap to print the colors available for adidas original shoes in https://www.myntra.com/

'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/')
time.sleep(2)

driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('adidas')
time.sleep(2)
driver.find_element('xpath', '//li[text()="Adidas Originals Shoes"]').click()
time.sleep(2)

driver.find_element('xpath', '//div[@class="colour-more"]').click()
time.sleep(2)

all_colors = driver.find_elements('xpath', '//li[@class="colour-listItem"]')        ## list of web-elements     ## [wb1, wb2, wb3...wb20]

for color in all_colors:
    print(color.text)


#############################################################################################################
'''
Eg4.    wap to print the menu items and its price of the items available in domino's pizza in https://www.zomato.com/bangalore/delivery 

'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.zomato.com/bangalore/delivery')
time.sleep(2)

driver.find_element('xpath', '//input[@placeholder="Search for restaurant, cuisine or a dish"]').send_keys('pizza')
time.sleep(2)

driver.find_element('xpath', '//input[@placeholder="Search for restaurant, cuisine or a dish"]').click()
time.sleep(2)

driver.find_element('xpath', '(//p[text()="Pizza - Delivery"])[1]').click()
time.sleep(2)

driver.find_element('xpath', '''//h4[text()="Domino's Pizza"]''').click()
time.sleep(4)

dominos_menu = driver.find_elements('xpath', '//h4[@class="sc-fZEjqe jToeOs"]')     ## [wb1, wb2, wb3, wb4,..]
items_prices = driver.find_elements('xpath', '//span[@class="sc-17hyc2s-1 cCiQWA"]')      ## [wb1, wb2, wb3, wb4,..]

for item, price in zip(dominos_menu, items_prices):
    print(item.text, '=', price.text)


#############################################################################################################
'''
Eg5.    wap to print the elements present in the footer of https://demowebshop.tricentis.com/

'''
#
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
# footer_elements = driver.find_elements('xpath', '//div[@class="footer-menu-wrapper"]//a')
# # print(footer_elements)          ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7, ,... wb22]
#
# for ele in footer_elements:
#     print(ele.text)

#############################################################################################################
'''
Eg6.    wap to print the elements which is present in the categories section of https://demowebshop.tricentis.com/

'''
#
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
# categories = driver.find_elements('xpath', '//div[@class="block block-category-navigation"]//a')
# # print(categories)       ## list of web-elements         ## [wb1, wb2, wb3, wb4,..wb7]
#
# for ele in categories:
#     print(ele.text)


#############################################################################################################
'''
Eg7.    wap to print all the popular searches in myntra

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
# popular_searches = driver.find_elements('xpath', '//div[@class="desktop-pSearchlinks"]/a')
# # print(popular_searches)     ## list of web-elements             ## [wb1, wb2, wb3, wb4,..wb47]
#
# for ele in popular_searches:
#     print(ele.text)

#############################################################################################################
'''
Eg8.    wap to print all the links present in https://www.python.org/

'''

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://www.python.org/')
time.sleep(2)

## all links --> href --> anchor tags

all_links = driver.find_elements('tag name', 'a')
# print(all_links)        ## list of web-elements     ## [a1, a2, a3, a4, a4, a5,....]

for link in all_links:
    print(link.get_attribute('href'))



































