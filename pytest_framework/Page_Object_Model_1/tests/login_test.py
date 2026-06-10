import pytest
from pytest_check import check
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.excelreader import get_data
from log import logCreator
import os
log = logCreator.log_generator()
from pages.Homepage import Homepage

@pytest.mark.usefixtures("setup_tearDown")
class Testlogin:
    @pytest.mark.order(2)
    def test_valid_login(self):

        data = get_data(r"E:\py_selenium\py_project\pytest_framework\Page_Object_Model_1\test_data\login_data.xlsx","Sheet1")

        username = data[0][0]
        password = data[0][1]

        log.info("Data is extracted")
        self.homepage.click_my_account()
        self.homepage.click_login_option()
        self.homepage.enter_username(username)
        self.homepage.enter_password(password)
        self.homepage.click_login_button()
        log.info("Login successful")
        my_account_text = self.homepage.get_my_account_text()

        assert my_account_text == "My Account"

    @pytest.mark.order(1)
    def test_invalid_login(self):

        data = get_data(r"E:\py_selenium\py_project\pytest_framework\Page_Object_Model_1\test_data\login_data.xlsx","Sheet1")
        username = data[1][0]
        password = data[1][1]
        log.info("Data is extracted")
        self.homepage.click_my_account()
        self.homepage.click_login_option()
        self.homepage.enter_username(username)
        self.homepage.enter_password(password)
        self.homepage.click_login_button()
        msg = self.homepage.get_error_message()
        print(msg)
        check.equal("Warning: No match for E-Mail Address and/or Password.",msg)