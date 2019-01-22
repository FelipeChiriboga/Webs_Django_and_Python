from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:/Users/Pippo/Anaconda3/Scripts/chromedriver")
driver.get('http://www.google.com')
elem = driver.find_element_by_link_text('About')
time.sleep(5)
elem.click()
time.sleep(5)
elem = driver.find_element_by_link_text('Our products')
time.sleep(5)
elem.click()