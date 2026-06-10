from selenium .webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Homepage:

    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    my_account = (By.XPATH,"//a[normalize-space()='My Account']")
    login_option = (By.XPATH,"//a[normalize-space()='Login']")
    username_field = (By.ID, "input-email")
    password_field = (By.ID, "input-password")
    login_button = (By.XPATH, "//input[@value='Login']")
    my_account_text = (By.XPATH, "//h2[normalize-space()='My Account']")
    error_message = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    
    def click_my_account(self):
        self.wait.until(EC.element_to_be_clickable(self.my_account)).click()
    def click_login_option(self):
        self.wait.until(EC.element_to_be_clickable(self.login_option)).click()
    def enter_username(self,username):
        self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element(*self.password_field).send_keys(password)
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
    def get_my_account_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.my_account_text)).text
    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_message)).text
    
    search_bar = (By.NAME, "search")
    search_button = (By.XPATH,"//i[@class='fa fa-search']")
    def search_item(self, item):
        self.wait.until(EC.presence_of_element_located(self.search_bar)).clear()
        self.driver.find_element(*self.search_bar).send_keys(item)
        
    def  search_click(self):
       self.wait.until(EC.element_to_be_clickable(self.search_button)).click()
                        