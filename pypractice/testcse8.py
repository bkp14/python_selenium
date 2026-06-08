from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

driver.get("https://automationexercise.com")


products = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/products']")
    )
)



if "#google_vignette" in driver.current_url:
    driver.back()

products = driver.find_element(By.XPATH,"//a[@href='/products']")

driver.execute_script("arguments[0].click();",products)
scroll_ele = driver.find_element(By.XPATH,"//h2[@class='title text-center']")
driver.execute_script("arguments[0].scrollIntoView();",scroll_ele)    
view_product = driver.find_element(By.CSS_SELECTOR,"a[href='/product_details/1']")
wait.until(EC.element_to_be_clickable(view_product))

driver.execute_script("arguments[0].click();",view_product)  
  
name =driver.find_element(By.XPATH,"//h2[text()='Blue Top']")
expected=driver.execute_script("return arguments[0].innerText",name)
assert expected=="Blue Top","not valid"
print("product detail page verified")

