import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from utilities import read_config
from log import logCreator
from pages.Homepage import Homepage
from pages.searchpage import searchpage
from pages.cartpage import cartpage
from pages.productpage import productpage
log=logCreator.log_generator()
@pytest.fixture
def setup_tearDown(request):

    browser = read_config.get_config("basic info", "browser")
    url = read_config.get_config("basic info", "url")

    if browser == 'chrome':
        d = webdriver.Chrome()
        d.maximize_window()

        wait = WebDriverWait(d, 10)
        d.get(url)

        log.info("Website launched")

        request.cls.d = d
        request.cls.wait = wait

        # Create page object
        request.cls.homepage = Homepage(d, wait)
        request.cls.spage = searchpage(d, wait)
        request.cls.cartpage = cartpage(d, wait)
        request.cls.productpage = productpage(d, wait)
        yield

        d.quit()