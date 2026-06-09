import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
def setup_function(function):
    global driver 
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")

def teardown_function(function):
    driver.quit()

def test_validproduct():
        driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("canon")
        driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        assert driver.find_element(By.XPATH,"//img[@title='Canon EOS 5D']").is_displayed()    