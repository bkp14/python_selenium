import pytest
from pytest_check import check
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.excelreader import get_data
from log import logCreator
import os
log = logCreator.log_generator()
from pages import Homepage
from pages import searchpage
@pytest.mark.usefixtures("setup_tearDown")
class Testsearch:
    @pytest.mark.dependency(name="search")
    def test_valid_search(self):
        self.homepage.search_item("hp")
        self.homepage.search_click()
        val = self.spage.hp_lap()
        assert val == "HP LP3065"

    def test_invalid_search(self):
        self.homepage.search_item("hi")
        self.homepage.search_click()
        val = self.spage.error_check() 
        assert val=="There is no product that matches the search criteria."      