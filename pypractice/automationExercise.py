from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")

  
driver.find_element(By.XPATH,"//a[text()=' Signup / Login']").click()
driver.find_element(By.XPATH,"//form[@action='/signup']/child::input[2]").send_keys("demo")
driver.find_element(By.XPATH,"//form[@action='/signup']/child::input[3]").send_keys("khd0006543dwq287@gmail.com")
driver.find_element(By.XPATH,"//button[text()='Signup']").click()

driver.find_element(By.XPATH,"//input[@value='Mr']").click()
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("1234455")
driver.find_element(By.CSS_SELECTOR,"#first_name").send_keys("mahendra singh")
driver.find_element(By.CSS_SELECTOR,"#last_name").send_keys("Dhoni")
driver.find_element(By.XPATH,"//input[@id='address1']").send_keys("KENNfefADY NAGwqAR 2D STREET")
driver.find_element(By.XPATH,"//input[@id='state']").send_keys("tn")
driver.find_element(By.XPATH,"//input[@id='city']").send_keys("salem")
driver.find_element(By.XPATH,"//input[@id='zipcode']").send_keys("231211")
driver.find_element(By.XPATH,"//input[@id='mobile_number']").send_keys("2312111111")
driver.find_element(By.XPATH,"//button[normalize-space()='Create Account']").click()

actual=driver.find_element(By.XPATH,"//b[text()='Account Created!']").text
print(actual)
   

contbtn = driver.find_element(By.XPATH,"//a[@class='btn btn-primary']")
contbtn.click()
userName = driver.find_element(By.XPATH, "//ul[@class = 'nav navbar-nav']/descendant::a[text() = ' Logged in as ']").text
print(userName)
checkuser = userName

if "Logged in as demo" in checkuser:
    print("The Logged username is show")
else:
    print("The logged username is not show")
driver.find_element(By.XPATH,"//a[normalize-space()='Delete Account']").click()
deleted = driver.find_element(By.XPATH,"//b[normalize-space()='Account Deleted!']").text
print(deleted)
driver.find_element(By.XPATH,"//div[@class='pull-right']/child::a").click()










