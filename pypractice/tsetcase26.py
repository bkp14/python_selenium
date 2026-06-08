from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

driver.get("https://automationexercise.com")

action = ActionChains(driver)
action.send_keys(Keys.END).perform()
sub = driver.find_element(By.XPATH,"//h2[normalize-space()='Subscription']")
driver.execute_script("return argument[0].innerText;",)
action.send_keys(Keys.HOME).perform()





