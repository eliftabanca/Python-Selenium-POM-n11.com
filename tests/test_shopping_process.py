import time
import unittest
import pytest
from selenium import webdriver
from constants.globalConstants import *
from pages.PageBase import PageBase
from pages.categories import *
import softest
from selenium.webdriver.support.ui import Select
from pages.categories import *
from pages.shopping_process import *

@pytest.mark.usefixtures("setup")
class ShoppingProcessTest(softest.TestCase, unittest.TestCase):

    def test_add_to_basket(self):
        object_shopping_process = ShoppingProcess(self.driver)
        object_categories = CategoryProductListing(self.driver)
        object_categories.click_search_bar()
        object_categories.click_search_button()
        object_shopping_process.scroll_down()
        object_shopping_process.click_add_item()
        object_shopping_process.scroll_up()
        self.soft_assert(self.assertEqual, object_shopping_process.assert_basket_number() , BASCET_NUM_TEXT, "The bascet number text is not matching")
        self.assert_all()

    def test_update_cart_with_added_product(self):
        object_shopping_process = ShoppingProcess(self.driver)
        object_categories = CategoryProductListing(self.driver)
        object_shopping_process = ShoppingProcess(self.driver)
        object_categories = CategoryProductListing(self.driver)
        object_categories.click_search_bar()
        object_categories.click_search_button()
        object_shopping_process.scroll_down()
        object_shopping_process.click_add_item()
        object_shopping_process.scroll_up()
        object_shopping_process.click_bascet_button()
        object_shopping_process.scroll_down()
        time.sleep(10)
        object_shopping_process.click_plus_button()
        time.sleep(10)
        object_shopping_process.scroll_down()
        self.soft_assert(self.assertEqual, object_shopping_process.assert_quantity() , PLUS_QUANTITY_TEXT, "The bascet quantity number is not matching")
        self.assert_all()



       
