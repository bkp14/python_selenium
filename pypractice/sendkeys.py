from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.maximize_window
driver.get("https://www.google.co.in")
print(driver.title)

search = driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
search.send_keys("selenium",Keys.ENTER)
time.sleep(4)
print(driver.title)