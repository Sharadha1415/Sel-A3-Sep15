import time
import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Firefox()
    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver
    driver.close()

## setup --> driver = webdriver.Chrome(opts)













