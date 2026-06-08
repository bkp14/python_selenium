from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
@pytest.mark.smoke
@pytest.mark.parametrize("search_item",[("selenium"),("wikipedia"),("pytest")])
def test_sample(search_item):
 driver = webdriver.Chrome()
 driver.get("https://www.google.com/")
 driver.maximize_window()

 driver.find_element(By.CSS_SELECTOR,"#APjFqb").send_keys(search_item)
 action = ActionChains(driver)
 action.send_keys(Keys.ENTER)
