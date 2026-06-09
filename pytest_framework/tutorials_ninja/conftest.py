import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from tutorials_ninja.utilities import read_config
from tutorials_ninja.log import logCreator

log=logCreator.log_generator()
@pytest.fixture
def setup_tearDown(request):
    
    browser=read_config.get_config("basic info","browser")
    url=read_config.get_config("basic info","url")
    if browser=='chrome':
      d=webdriver.Chrome()
      d.maximize_window()
      wait=WebDriverWait(d,10)
      d.get(url)
      log.info("Website launched")
      request.cls.d=d
      request.cls.wait=wait
      yield
      d.quit()