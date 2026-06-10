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
from pages import cartpage
from pages import productpage
@pytest.mark.usefixtures("setup_tearDown")
class Testcart:

    @pytest.fixture
    def add_product(self):
     self.homepage.search_item("hp")
     self.homepage.search_click()
     self.spage.prod_add()
     self.productpage.add_prod_cart()

    def test_addtocart_valid(self, add_product):
        
        assert self.cartpage.prod_check()

    def test_removeele(self, add_product):
        val = self.cartpage.remove_prod()
        assert val == "Your shopping cart is empty!"
