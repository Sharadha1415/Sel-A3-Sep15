import time

## Initialize Chrome browser
from selenium import webdriver
c_driver = webdriver.Chrome()

## The above syntax will close the browser automatically

#------------------------------------------------------------------------
## To prevent the browser from automatically closing

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

c_driver = webdriver.Chrome(opts)

#################################################################################################

## Initialize firefox browser
from selenium import webdriver
f_driver = webdriver.Firefox()

## Firefox browser will not close automatically.
## So no need to consider FirefoxOptions and add_experimental_option

# #################################################################################################

## Initialize Edge browser
from selenium import webdriver
e_driver = webdriver.Edge()

## The above syntax will close the browser automatically

#------------------------------------------------------------------------
## To prevent the browser from automatically closing

from selenium import webdriver

opts = webdriver.EdgeOptions()
opts.add_experimental_option("detach", True)

e_driver = webdriver.Edge(opts)

###################################################################################
















































































