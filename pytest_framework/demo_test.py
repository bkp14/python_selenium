from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://google.com")
print("Loaded")
driver.quit()