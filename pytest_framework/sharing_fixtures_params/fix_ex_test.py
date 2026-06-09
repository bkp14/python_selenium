from selenium.webdriver.common.by import By
import pytest
import pytest_check as check
import sys
import os

from Data_Driven_test_config.read_config import get_config

@pytest.mark.usefixtures("setup_and_teardown")
class Testsearch:
    @pytest.mark.order(3)
    @pytest.mark.valid
    def test_validproduct(self):
        value1 = get_config("search term", "valid")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(value1)

        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()

        check.is_true(self.driver.find_element(By.XPATH,"//img[@title='Canon EOS 5D']").is_displayed(),"Canon product is not displayed")
    @pytest.mark.order(2)
    def test_invalidproduct(self):
        value2 = get_config("search term","invalid")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(value2)

        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()

        actual_text = self.driver.find_element(By.XPATH,"//p[contains(text(),'There is no product that matches the search criter')]").text

        check.equal(actual_text,"There is no product that matches the search criteria.","Invalid product message mismatch")
    @pytest.mark.order(1)
    @pytest.mark.valid
    def test_noproduct(self):
        value3 = get_config("search term","blank")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(value3)

        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()

        actual_text = self.driver.find_element( By.XPATH,"//p[contains(text(),'There is no product that matches the search criter')]").text

        check.equal(actual_text, "There is no product that matches the search criteria.","No product search message mismatch")