from selenium .webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class cartpage:

    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    prod_img = (By.XPATH,"//td[@class='text-center']/following::img")
    
    remove =(By.XPATH,"//i[@class='fa fa-times-circle']")
    err_msg =(By.XPATH,"//div[@id='content']//p[contains(text(),'Your shopping cart is empty!')]")
    def prod_check(self):
        
        return self.wait.until(EC.visibility_of_element_located(self.prod_img)).is_displayed()
    
    def remove_prod(self):
        self.driver.find_element(By.XPATH,"//i[@class='fa fa-times-circle']").click()
        return self.wait.until(EC.presence_of_element_located((self.err_msg))).text