from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest

@pytest.mark.smoke
@pytest.mark.parametrize("search_item", ["selenium", "wikipedia", "pytest"])
def test_sample(search_item):

    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()

    search_box = driver.find_element(By.CSS_SELECTOR, "#APjFqb")
    search_box.send_keys(search_item)

    ActionChains(driver).send_keys(Keys.ENTER).perform()

    driver.quit()