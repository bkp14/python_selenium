from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

@pytest.mark.usefixtures("setup_and_teardown")
class Testsearch:
    def test_validproduct(self):
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("canon")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.XPATH,"//img[@title='Canon EOS 5D']").is_displayed()

    def test_invalidproduct(self):
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("honda")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.XPATH,"//p[contains(text(),'There is no product that matches the search criter')]").text=="There is no product that matches the search criteria." 

    def test_noproduct(self):
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.XPATH,"//p[contains(text(),'There is no product that matches the search criter')]").text=="There is no product that matches the search criteria." 