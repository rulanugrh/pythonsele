from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://google.co.id')
driver.find_element("name", 'q').send_keys('rulanugrh' + Keys.ENTER)
time.sleep(10)

driver.quit()