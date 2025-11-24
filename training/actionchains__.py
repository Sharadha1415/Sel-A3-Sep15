'''
The operations performed using mouse/keyboard, we call it as "low-level operations"
To perform low-level operation in selenium, we go for ActionChains

We should import ActionChains
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
        action_chains   --> module
        ActionChains    --> class
        keys            --> module
        Keys            --> class

    actionchain_obj = ActionChains(driver)
    For every actionchain_obj, .perform() is the mandatory operation

'''
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

ac_obj = ActionChains(driver)

###########################################################################################

'''
Mouse hovering  :   
    move_to_element is an attribute of ActionChains class, which will perform Mouse Hovering operations
    *   Locate the web-element 
        ele = driver.find_element('loc_name', 'loc_value')
    *   actionchain_obj.move_to_element(ele).perform()
        The control will be hovered to the given element
    *   For every actionchain_obj, .perform() is the mandatory operation

'''
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# men = driver.find_element('xpath', '(//a[text()="Men"])[1]')
# ac_obj.move_to_element(men).perform()
# time.sleep(2)
#
# kids = driver.find_element('xpath', '(//a[text()="Kids"])[1]')
# ac_obj.move_to_element(kids).perform()
# time.sleep(2)
#
# beauty = driver.find_element('xpath', '(//a[text()="Beauty"])[1]')
# ac_obj.move_to_element(beauty).perform()

##-----------------------------------------------------------------------------------------

driver.get('https://www.myntra.com/')
time.sleep(2)

men = driver.find_element('xpath', '(//a[text()="Men"])[1]')
ac_obj.move_to_element(men).perform()
time.sleep(2)

mens_options = driver.find_elements('xpath', '//div[@data-group="men"]//a')     ## list of web-elements

for ele in mens_options:
    print(ele.text)



##########################################################################################

'''
Double click    :   To double click on the web-element, we have double_click attribute in ActionChains class
'''

#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# element = driver.find_element('xpath', '//button[text()="Copy Text"]')
# ac_obj.double_click(element).perform()
# time.sleep(2)
#
# ele2 = driver.find_element('xpath', '//label[text()="Name:"]')
# ac_obj.double_click(ele2).perform()

###########################################################################################

'''
Right click :   
context_click is an attribute of ActionChains class, it will perform right click operation
SYNTAX  :   ac_obj.context_click().perform()
            The above syntax will right click at the start of the application

            ac_obj.context_click(ele).perform()
            The above syntax will right click at that element
'''
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# #
# # ac_obj.context_click().perform()
# # time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="Tabs"]')
# ac_obj.context_click(ele).perform()

###########################################################################################

## Scrolling operations

# ## scroll down till a particular element
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//a[text()=" ONLINE SHOPPING "]')
# ac_obj.scroll_to_element(ele).perform()

##------------------------------------------------------------------------------

# ## To scroll down till the end of the application
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(2)
#
# ## To go back to the start of the application
# ac_obj.send_keys(Keys.HOME).perform()
#
# #------------------------------------------------------------------------------
#
# ## Pageup Pagedown scrolling
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(3)
#
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()
#
# ###########################################################################################
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ## Scroll down by pixels
# driver.execute_script("window.scrollBy(0, 1500);")
#
# ## scroll down till the end of the application
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
#
# ## scroll back to the start of the application
# driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
#
# ## scroll down till a specific element
# ele = driver.find_element('xpath', '//a[text()=" ONLINE SHOPPING "]')
# driver.execute_script("arguments[0].scrollIntoView(true);", ele)

###########################################################################################

# ## drag and drop
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ele).perform()
# time.sleep(2)
#
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
# droppable_ele = driver.find_element('xpath', '//div[@id="droppable"]')
#
# ac_obj.drag_and_drop(draggable_ele, droppable_ele).perform()


###########################################################################################


'''
ANALYZE THE BELOW CODE
'''

# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="firstname"]').send_keys('Harry')
# time.sleep(1)
#
# ac_obj.send_keys(Keys.TAB).perform()        ## The control will shift to the lastname
# time.sleep(1)
# ac_obj.send_keys('Potter').perform()
# time.sleep(2)
#
# ac_obj.send_keys(Keys.BACKSPACE).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.BACKSPACE).perform()
#
# ##-------------------------------------------------------------------
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# fname = driver.find_element('xpath', '//input[@name="firstname"]')
# lname = driver.find_element('xpath', '//input[@name="lastname"]')
#
# fname.send_keys('Harry')
# time.sleep(2)
#
# fname.send_keys(Keys.CONTROL + 'a')         ## select the data
# fname.send_keys(Keys.CONTROL + 'c')         ## copy the data
#
# ac_obj.send_keys(Keys.TAB).perform()        ## switching the control to last name
# lname.send_keys(Keys.CONTROL + 'v')         ## paste the data
#
# # ##-------------------------------------------------------------------
#
# ## ctrl + a
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# ac_obj.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
#
# # ############################################################################################################
#
# ## ctrl + backspace
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="name"]').send_keys('Harry Potter')
# time.sleep(2)
# ac_obj.key_down(Keys.CONTROL).send_keys(Keys.BACKSPACE).key_up(Keys.CONTROL).perform()
#
# # ##-------------------------------------------------------------------
#
# ## shift
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="name"]').send_keys('harry')
# time.sleep(2)
# ac_obj.key_down(Keys.SHIFT).send_keys('a').perform()
#
# # ##-------------------------------------------------------------------
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="name"]').send_keys('Harry Potter')
# time.sleep(2)
# ac_obj.send_keys(Keys.TAB).perform()
# time.sleep(2)
# ac_obj.send_keys('harry@gmail.com').perform()


'''
Go to https://crossbrowsertesting.github.io/drag-and-drop.html, perform drag and drop
'''





















