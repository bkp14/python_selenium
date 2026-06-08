from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


driver = webdriver.Chrome()
driver.get("http://automationexercise.com/")
driver.maximize_window()
wait = WebDriverWait(driver,15)
home=driver.current_url
print(home)
assert home == "https://automationexercise.com/"
print("home page  is verified")
driver.find_element(By.XPATH,"//a[text()=' Signup / Login']").click()
login_msg = wait.until(
    ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='login-form']/h2")
    )
)

actual_login_msg = login_msg.text
print(actual_login_msg)
assert actual_login_msg == "Login to your account"
print("Login page verification passed")
email:WebElement=wait.until(ec.visibility_of_element_located((By.XPATH,"//form[@action='/login']/child::input[@type='email']")))
email.send_keys("demo212@gmail.com")
driver.find_element(By.XPATH,"//form[@action='/login']/child::input[@type='password']").send_keys("12345")

driver.find_element(By.XPATH,"//form[@action='/login']/child::button[@type='submit']").click()

invalid_msg = driver.find_element(By.XPATH,"//form[@action='/login']/child::p").text
print(invalid_msg)
assert invalid_msg == "Your email or password is incorrect!"
print("invalid email and password is asserted")
driver.quit()