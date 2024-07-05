from tkinter.tix import Select
from selenium.webdriver.support.ui import Select
import pytest
from constants.globalConstants import *
from pages.PageBase import PageBase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class CategoryProductListing(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_category(self):
        category_buton = self.wait_element_visibility(CATEGORY_ELECTRONIC)
        category_buton.click()

    def hover_category(self):
        self.hover(CATEGORY_ELECTRONIC)
        
    def category_assert(self):
        category_text = self.wait_element_visibility(CATEGORY_TEXT_LOCATER)
        return category_text.text
    

    def click_subcategory(self):
        subcategory_button = self.wait_element_visibility(SUBCATEGORY_COMPUTER)
        subcategory_button.click()
    
    def assert_subcategory(self):
        subcategory_text = self.wait_element_visibility(SUBCATEGORY_COMPUTER)
        return subcategory_text.text
    
    def click_search_bar(self):
        search_bar_area = self.wait_element_visibility(SEARCHBOX_LOCATOR)
        search_bar_area.click()
        search_bar_area.send_keys("Bilgisayar")

    def click_search_button(self):
        search_button = self.wait_element_visibility(SEARCH_BUTTON_LOCATOR)
        search_button.click()

    def select_fiter(self):
        select_masaustu_filter = self.wait_element_visibility(FILTER_LOCATOR)
        select_masaustu_filter.click()

    def assert_filter(self):
        subcategory_text = self.wait_element_visibility(FILTER_TEXT_LOCATOR)
        return subcategory_text.text
    
    def product_details_by_brand(self):
        brand = self.wait_element_visibility(BRAND_LOCATOR)
        brand.click()

    def assert_brand_name(self):
        brand_text = self.wait_element_visibility(BRAND_TEXT_LOCATOR)
        return brand_text.text
    



