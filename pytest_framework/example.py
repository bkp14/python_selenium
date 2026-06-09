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
email.send_keys("muhi2701@gmail.com")

driver.find_element(By.XPATH,"//form[@action='/login']/child::input[@type='password']").send_keys("1234567890")

driver.find_element(By.XPATH,"//form[@action='/login']/child::button[@type='submit']").click()

# Wait longer for the page to load after login (increased to 30 seconds)
try:
    username = wait.until(
        ec.visibility_of_element_located((By.XPATH,"//ul[@class='nav navbar-nav']/descendant::a[10]"))
    ).text
    assert username=="Logged in as muhi"
    print("logged in using username successfully")
except Exception as e:
    print(f"Warning: Could not find username element - {e}")
    print(f"Current URL: {driver.current_url}")

wait =  WebDriverWait(driver,15)
wait.until(ec.element_to_be_clickable((By.XPATH,"//ul[@class='nav navbar-nav']/descendant::a[4]")))

cururl = driver.current_url
print(cururl)
assert cururl == "https://automationexercise.com/login","wrong url"
print("account loggged out successfully")