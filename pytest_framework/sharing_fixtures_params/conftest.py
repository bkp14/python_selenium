import pytest
from selenium import webdriver
@pytest.fixture(params=["chrome"])
def setup_and_teardown(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver=driver
    yield
    driver.quit()        
