import pytest
from selenium import webdriver
from demoblaze_config.read_config import get_config
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture()
def setup_and_teardown(request):
    br= get_config("basic info","browser")
    if br == "Chrome":
     driver =webdriver.Chrome()
    ul= get_config("basic info","url")
    driver.get(ul)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.quit()