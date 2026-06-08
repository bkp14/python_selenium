from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

driver.get("https://automationexercise.com")

print(driver.current_url)

products = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/products']")
    )
)

print(driver.current_url)

driver.find_element(By.XPATH, "//a[@href='/products']").click()

if "#google_vignette" in driver.current_url:
    driver.back()

    products = driver.find_element(
        By.XPATH,
        "//a[@href='/products']"
    )

    driver.execute_script(
        "arguments[0].click();",
        products
    )

wait.until(EC.url_contains("/products"))
print("Current URL:", driver.current_url)

product = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "(//div[@class='product-image-wrapper'])[2]")
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    product
)

ActionChains(driver).move_to_element(product).perform()

wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "(//div[contains(@class,'product-overlay')])[2]")
    )
)

button = driver.find_element(
    By.XPATH,
    "(//a[@data-product-id='2'])[2]"
)

driver.execute_script(
    "arguments[0].click();",
    button
)

print("Product added to cart")