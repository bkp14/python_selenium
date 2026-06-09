from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Utilities import excelReader
import pytest
from selenium.webdriver.support import expected_conditions as EC
import time
from Utilities.logCreator import log_creator

log = log_creator()
@pytest.fixture
def setup_and_teardown():
   global driver
   driver=webdriver.Chrome()
   log.info("Application launched")
   driver.get("https://www.demoblaze.com/")
   driver.maximize_window()
   global wait
   wait = WebDriverWait(driver, 10)
   yield
   driver.quit()

def test_validlogin(setup_and_teardown):
   driver.find_element(By.ID, "login2").click()
   valid_list= excelReader.get_data("Excelfiles/login_Data.xlsx","login")
   wait.until(EC.visibility_of_element_located((By.ID, "loginusername")) ).send_keys(valid_list[0][0])
   log.info("username has been entered")
       
   driver.find_element(By.ID, "loginpassword").send_keys(valid_list[0][1])
   log.info("password has been entered")
        
   driver.find_element(By.XPATH, "//button[text()='Log in']").click()
   log.info("submit has been clicked")
   check_username = wait.until(EC.visibility_of_element_located((By.ID, "nameofuser"))).text

   assert valid_list[0][0] in check_username
   
   print("Login successful")
   log.info("valid test completed")
def test_invalidlogin(setup_and_teardown):
   driver.find_element(By.ID, "login2").click()
   valid_list= excelReader.get_data("Excelfiles/login_Data.xlsx","login")
   wait.until(EC.visibility_of_element_located((By.ID, "loginusername")) ).send_keys(valid_list[1][0])
   log.info("username has been entered")
        
   driver.find_element(By.ID, "loginpassword").send_keys(valid_list[1][1])
   log.info("password has been entered")
        
   driver.find_element(By.XPATH, "//button[text()='Log in']").click()  
   log.info("submit has been clicked")
   wait.until(EC.alert_is_present())
   msg = driver.switch_to.alert
   assert msg.text == "Wrong password.","wrong"
   msg.accept()
   print("invalid test successful")
   log.info("invalid test completed")
