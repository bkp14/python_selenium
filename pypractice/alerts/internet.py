from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver  = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
driver.switch_to.alert.accept()

msg1 = driver.find_element(By.XPATH,"//p[@id='result']").text
assert msg1=="You successfully clicked an alert","invalid"
print("simple alert executed successfully")

driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
driver.switch_to.alert.dismiss()
msg1 = driver.find_element(By.XPATH,"//p[@id='result']").text
assert msg1=="You clicked: Cancel","invalid"
print("confirmation (dismiss) alert executed successfully")

driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
driver.switch_to.alert.accept()
msg1 = driver.find_element(By.XPATH,"//p[@id='result']").text
assert msg1=="You clicked: Ok","invalid"
print("confirmation(accept) alert executed successfully")

driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("this is prompt alert")
alert.accept()
msg1 = driver.find_element(By.XPATH,"//p[@id='result']").text
assert msg1=="You entered: this is prompt alert","invalid"
print("prompt(accept) alert executed successfully")

driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("this is prompt alert")
alert.dismiss()
msg1 = driver.find_element(By.XPATH,"//p[@id='result']").text
assert msg1=="You entered: null","invalid"
print("prompt(dismiss) alert executed successfully")