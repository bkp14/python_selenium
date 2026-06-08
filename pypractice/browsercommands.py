import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.maximize_window()

#get command
driver.get("https://www.demoblaze.com/")

driver.find_element(By.PARTIAL_LINK_TEXT,"Abo").click()
time.sleep(10)





















