from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://automationexercise.com/")
driver.maximize_window()
wait = WebDriverWait(driver,15)
home=driver.current_url
print(home)
assert home == "https://automationexercise.com/"
print("home page  is verified")
action = ActionChains(driver)

try:
  driver.find_element(By.XPATH,"//a[@href='/products']").click()
  wait.until(EC.url_contains("/products"))
except:
 iframe=driver.find_element(By.TAG_NAME,"iframe")
 driver.switch_to.frame(iframe)
 driver.find_element(By.CSS_SELECTOR,".close").click()
 driver.switch_to.default_content()

ele = driver.find_element(By.XPATH,"//div[@class='features_items']")
action.scroll_to_element(ele).perform()
product = driver.find_element(
    By.XPATH,
    "(//div[@class='product-image-wrapper'])[2]"
)

ActionChains(driver).move_to_element(product).perform()

add_to_cart = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='product-overlay']//a[contains(@class,'add-to-cart')]")
    )
)

add_to_cart.click()