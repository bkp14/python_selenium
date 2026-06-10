from selenium .webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class searchpage:
    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait

    hplaptop = (By.XPATH,"//a[contains(text(),'HP LP3065')]")    
    err_msg = (By.XPATH,"//p[contains(text(),'There is no product that matches the search criter')]")
    addprod=(By.XPATH,"//div[@class='product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-12']//button[1]")
    def hp_lap(self):
        return self.wait.until(EC.presence_of_element_located(self.hplaptop)).text
   
    def error_check(self):
        return self.wait.until(EC.presence_of_element_located(self.err_msg)).text
    def prod_add(self):
        self.wait.until(EC.element_to_be_clickable(self.addprod)).click()