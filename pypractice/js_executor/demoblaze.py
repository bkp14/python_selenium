from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
#getpagetitle
title=driver.execute_script("return document.title;")
print(title)
#click
contact = driver.find_element(By.XPATH,"//a[normalize-space()='Contact']")
driver.execute_script("arguments[0].click();",contact)
wait = WebDriverWait(driver,10)


#entervalues
email = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="recipient-email"]')))
driver.execute_script("arguments[0].value='kp@gmail.com'",email)
but = driver.find_element(By.XPATH,"//button[normalize-space()='Send message']")
driver.execute_script("arguments[0].click();",but)
driver.switch_to.alert.accept()
time.sleep(5)

#scrolldown
driver.execute_script("window.scrollTo(0,100)")
time.sleep(5)

#scrollup
driver.execute_script("window.scrollTo(0,0)")
time.sleep(5)

#scrolltoelement
iphone= driver.find_element(By.XPATH,"//a[normalize-space()='Iphone 6 32gb']")
driver.execute_script("arguments[0].scrollIntoView();",iphone)
time.sleep(5)

#newtab
cur_win = driver.current_window_handle

new_tab=driver.execute_script("window.open('https://www.google.com')")
driver.switch_to.window(driver.window_handles[1])

#get cur url
print(driver.execute_script("return window.location.href"))
driver.switch_to.window(cur_win)

#gettext
sam = driver.find_element(By.XPATH,"//a[normalize-space()='Samsung galaxy s6']")
text= driver.execute_script("return arguments[0].innerText;",sam)
print(text)
time.sleep(5)
#scrollBY
#down
driver.execute_script("window.scrollBy(0,700)")
time.sleep(5)
#up
driver.execute_script("window.scrollBy(0,-700)")
time.sleep(5)
#right
driver.execute_script("window.scrollBy(200,0)")
time.sleep(5)
#left
driver.execute_script("window.scrollBy(-200,0)")
time.sleep(5)