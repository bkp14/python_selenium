import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from demoblaze_config.read_config import get_config

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_login_with_valid(self):

        print("Current URL :", self.driver.current_url)
        print("Page Title  :", self.driver.title)

        username = get_config("login", "uname")
        password = get_config("login", "pword")

        
        self.driver.find_element(By.ID, "login2").click()

        
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "loginusername"))
        ).send_keys(username)

        
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)

        
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        
        check_username = self.wait.until(
            EC.visibility_of_element_located((By.ID, "nameofuser"))
        ).text

        assert username in check_username

        print("Login successful")