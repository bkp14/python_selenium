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

        
        # open login modal
        self.driver.find_element(By.ID, "login2").click()

# wait for modal to fully appear
        self.wait.until( EC.visibility_of_element_located((By.ID, "logInModal")))

# now wait for username field
        username_field = self.wait.until( EC.element_to_be_clickable((By.ID, "loginusername")))
        username_field.clear()
        username_field.send_keys(username)

        
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)

        
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        
        check_username = self.wait.until(
            EC.visibility_of_element_located((By.ID, "nameofuser"))
        ).text

        assert username in check_username

        print("Login successful")