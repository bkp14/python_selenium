from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
@pytest.mark.regression
@pytest.mark.parametrize("input",(["chrome","firefox"]))
@pytest.mark.parametrize(("input_url"),(["https://www.flipkart.com","https://www.amazon.com"]))
def test_url(input,input_url):
    if input == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    if input == "firefox":
        options= FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get(input_url)
    print(driver.current_url)
    time.sleep(5)
    driver.quit()        