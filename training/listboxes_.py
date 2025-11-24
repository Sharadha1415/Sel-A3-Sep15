import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# date_ = driver.find_element('xpath', '//select[@id="day"]')
# date_select = Select(date_)

## select_by_index
## select_by_value
## select_by_visible_text
#
# date_select.select_by_index(5)
# time.sleep(1)
# date_select.select_by_index(10)
# time.sleep(1)
# date_select.select_by_index(19)

# date_select.select_by_value('5')
# time.sleep(1)
# date_select.select_by_value('10')
# time.sleep(1)
# date_select.select_by_value('15')

# date_select.select_by_visible_text('13')
# time.sleep(1)
# date_select.select_by_visible_text('20')
# time.sleep(1)
# date_select.select_by_visible_text('25')

###########################################################################


driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(3)

colors = driver.find_element('xpath', '//select[@id="colors"]')
select_obj = Select(colors)

# select_obj.select_by_index(2)
# time.sleep(1)
# select_obj.select_by_index(3)
# time.sleep(1)
# select_obj.select_by_index(4)

# select_obj.select_by_value('red')
# time.sleep(1)
# select_obj.select_by_value('blue')
# time.sleep(1)
# select_obj.select_by_value('yellow')







