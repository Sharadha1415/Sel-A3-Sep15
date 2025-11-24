'''
iframes :   The application present inide another application, we call it as iframe
            The tagname of an iframe is always iframe

            STEPS TO HANDLE IFRAMES
            *   Locate the frame
            *   Switch the driver from the parent frame to the child frame
                SYNTAX  :   driver.switch_to.frame(frame)
            *   Perform the operations in the frame
            *   Once we are done performing the operations inside the frame, we should switch back to the parent_frame

'''


import time

## Eg1
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)

driver.get('https://www.linkedin.com')
time.sleep(2)

## locate the google frame
google_frame = driver.find_element('xpath', '//iframe[@title="Sign in with Google Button"]')

## switch the driver to the google_frame
driver.switch_to.frame(google_frame)

## perform operations inside the google frame
driver.find_element('xpath', '//span[text()="Continue with Google"]').click()
time.sleep(2)

## switch back to the parent frame
driver.switch_to.parent_frame()
time.sleep(2)

## locate microsoft frame
microsoft_frame = driver.find_element('xpath', '//iframe[@name="microsoft_signin_iframe_1"]')

## switch the driver to the microsoft frame
driver.switch_to.frame(microsoft_frame)

## perform operations inside the microsoft frame
driver.find_element('xpath', '//span[text()="Continue with Microsoft"]').click()        ## It will go to next page
time.sleep(2)

## switch back to the parent frame
driver.switch_to.parent_frame()

##
driver.back()       ## back to previous page(home page)
time.sleep(2)

## scroll down until youtube ad is visible
ele = driver.find_element('xpath', '//h2[contains(text(), "Join your colleagues")]')
ac_obj.scroll_to_element(ele).perform()
time.sleep(2)

## locate youtube frame
youtube_frame = driver.find_element('xpath', '//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')

## switch the driver to the youtube frame
driver.switch_to.frame(youtube_frame)

## perform the operations inside
driver.find_element('xpath', '//button[@title="Play"]').click()
time.sleep(3)

driver.find_element('xpath', '//button[@aria-label="Pause keyboard shortcut k"]').click()
time.sleep(2)

# ## switch back to the parent frame
driver.switch_to.parent_frame()

driver.quit()
#####################################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\iframe.html')
# time.sleep(2)
#
# ## locate the frame
# frame1 = driver.find_element('xpath', '//iframe[@id="FR1"]')
#
# ## switch the driver to the frame
# driver.switch_to.frame(frame1)
#
# ## perform the operations inside the frame
# driver.find_element('xpath', '//input[@id="small-searchterms"]').send_keys('books')
# time.sleep(2)
#
# ## switch back to the parent frame
# driver.switch_to.parent_frame()
# time.sleep(2)
#
# ## locate the frame
# frame2 = driver.find_element('xpath', '//iframe[@id="FR2"]')
#
# ## switch the driver to the frame2
# driver.switch_to.frame(frame2)
#
# ## perform the operations inside the frame
# driver.find_element('xpath', '//input[@id="search_form"]').send_keys('vehicle insurance')
# time.sleep(2)
#
# ## switch back to the parent frame
# driver.switch_to.parent_frame()








