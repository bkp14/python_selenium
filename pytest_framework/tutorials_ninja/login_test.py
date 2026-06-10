import pytest
from pytest_check import check
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from tutorials_ninja.utilities import excelReader
from tutorials_ninja.log import logCreator

log = logCreator.log_generator()


@pytest.mark.usefixtures("setup_tearDown")
class Testlogin:
    @pytest.mark.order(2)
    def test_valid_login(self):

        data = excelReader.get_data(r"E:\\py_selenium\py_project\\pytest_framework\\tutorials_ninja\\Excelfiles\\login_data.xlsx","Sheet1")

        username = data[0][0]
        password = data[0][1]

        log.info("Data is extracted")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='My Account']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Login']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "input-email"))).send_keys(username)

        self.d.find_element(By.ID, "input-password").send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']"))).click()
        log.info("Login successful")
        my_account_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='My Account']"))).text

        assert my_account_text == "My Account"

    @pytest.mark.order(1)
    def test_invalid_login(self):

        data = excelReader.get_data(r"E:\\py_selenium\py_project\\pytest_framework\\tutorials_ninja\\Excelfiles\\login_data.xlsx","Sheet1")
        username = data[1][0]
        password = data[1][1]
        log.info("Data is extracted")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='My Account']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Login']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "input-email"))).send_keys(username)
        self.d.find_element(By.ID, "input-password").send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']"))).click()
        msg = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-danger alert-dismissible']"))).text
        print(msg)
        check.equal("Warning: No match for E-Mail Address and/or Password.",msg)