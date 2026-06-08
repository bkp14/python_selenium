from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

driver.get("https://automationexercise.com")
testcase = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Test Cases']")))
driver.execute_script("arguments[0].click();",testcase)

expected = driver.find_element(By.CSS_SELECTOR,"h2[class='title text-center'] b")

expected1=driver.execute_script("return arguments[0].innerText;",expected)
assert expected1 == "TEST CASES" , "invalid assertion"
print("test cases page navigation successful")







