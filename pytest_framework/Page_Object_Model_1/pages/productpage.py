from selenium .webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class productpage:
    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait
    add_to_cart_but = (By.XPATH,"//button[@id='button-cart']")    
    shop=(By.XPATH,"//span[text()='Shopping Cart']")
    def add_prod_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart_but)).click()
        ele=self.wait.until(EC.element_to_be_clickable(self.shop))
        self.driver.execute_script("arguments[0].click();",ele)