from tkinter.tix import Select
from selenium.webdriver.support.ui import Select
import pytest
from constants.globalConstants import *
from pages.PageBase import PageBase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.categories import *

@pytest.mark.usefixtures("setup")
class ShoppingProcess(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_add_item(self):
        add_button_num = self.wait_element_visibility(BASCET_BUTTON_NUM_LOCATOR)
        add_button_num.click()
        
    def scroll_down(self):
        self.driver.execute_script("scrollBy(0,650)")

    def scroll_up(self):
        self.driver.execute_script("scrollBy(0,-650)")

    def assert_basket_number(self):
        bascet_num = self.wait_element_visibility(BASCET_NUM)
        return bascet_num.text

    def click_bascet_button(self):
        bascet_button = self.wait_element_visibility(BASCET_BUTTON_LOCATOR)
        bascet_button.click()

    def click_plus_button(self):
        plus_button = self.wait_element_visibility(PLUS_BUTTON)
        plus_button.click()
    
    def assert_quantity(self):
        quantity = self.wait_element_visibility(PLUS_QUANTITY)
        return quantity.text

    

        

