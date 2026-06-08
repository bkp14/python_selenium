from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")
driver.maximize_window()

single = driver.find_element(By.CSS_SELECTOR,"#course")
select = Select(single)
select.select_by_visible_text("Java")
time.sleep(2)
select.select_by_index(3)
time.sleep(2)
select.select_by_value("python")
time.sleep(2)

for i in select.options:
      print(i.text)

wait=WebDriverWait(driver,15)
wait.until(EC.visibility_of_element_located((By.XPATH,"//select[@id='ide']")))
s=Select(driver.find_element(By.XPATH,value="//select[@id='ide']"))
s.is_multiple
s.select_by_index(1)
s.select_by_value("vs")
s.select_by_visible_text("NetBeans")
w=s.all_selected_options
print("All Selected optionS:")
for i in w:
    print(i.text)
time.sleep(3)
s.deselect_by_index(1)
s.deselect_all()      