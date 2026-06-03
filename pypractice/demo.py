import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(10)
driver.quit()