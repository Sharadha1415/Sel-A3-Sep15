import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

## launch the application
driver.get('https://www.myntra.com/')
time.sleep(2)

## To maximize the window
driver.maximize_window()
time.sleep(2)

# ## To minimize window
# driver.minimize_window()
# time.sleep(2)

## To go back
driver.back()
time.sleep(2)

## To go forward
driver.forward()
time.sleep(2)

## To refresh
driver.refresh()
time.sleep(2)

##
print(driver.current_url)           ## Gives the url of the page
print(driver.title)                 ## It will give the title of the page
print(driver.name)                  ## It gives the names of the browser

## Take screenshot of the application
driver.save_screenshot('myntra_ss.png')

#
driver.save_screenshot(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\screenshots_\myntra_ss1.png')

##
driver.close()







