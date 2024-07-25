from selenium.webdriver.common.by import By

BASE_URL ="https://www.n11.com/"

#categories.py
CATEGORY_ELECTRONIC = (By.XPATH , "//*[@id='header']/nav/ul/li[2]/a")
CATEGORY_TEXT = "Elektronik"
CATEGORY_TEXT_LOCATER = (By.LINK_TEXT, "Elektronik")

SUBCATEGORY_COMPUTER = (By.LINK_TEXT, "Bilgisayar") 
SUBCATEGORY_TEXT_LOCATOR = (By.XPATH, "//*[@id='breadCrumb']/ul/li[3]/a")
SUBCATEGORY_COMPUTER_TEXT = "Bilgisayar"

SEARCHBOX_LOCATOR = (By.ID, "searchData")
SEARCH_BUTTON_LOCATOR = (By.CLASS_NAME, "iconsSearch")

FILTER_LOCATOR = (By.LINK_TEXT, "Masaüstü Bilgisayar")
FILTER_TEXT_LOCATOR = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[2]/section/div[1]/div[1]/div[1]/div/h1")
FILTER_TEXT = ("Bilgisayar")

BRAND_LOCATOR = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[2]/section/div[1]/div[3]/div/ul/div/div/li[1]/a")
BRAND_TEXT = "Asus"
BRAND_TEXT_LOCATOR = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[1]/section[2]/div/div/div/span[1]")
                                
#shopping_process.py
BASCET_BUTTON_NUM_LOCATOR =(By.XPATH, "//*[@id='p-606679208']/div/span")
BASCET_NUM = (By.CLASS_NAME, "basketTotalNum")
BASCET_NUM_TEXT = "1"

BASCET_BUTTON_LOCATOR = (By.CLASS_NAME, "iconsBasketWhite")
PLUS_BUTTON = (By.XPATH,"//*[@id='newCheckout']/div/div[1]/div[1]/div[2]/section/table[2]/tbody/tr/td[1]/div[3]/div[2]/div/span[1]")

PLUS_QUANTITY = (By.ID, "quantity_127254023919")
PLUS_QUANTITY_TEXT = "2"

CLEAR_BUTTON = (By.ID, "127254023919")
AFTER_CLEAR_LOCATOR = (By.CLASS_NAME, "removeProd.svgIcon.svgIcon_trash")
AFTER_CLEAR_TITLE = "Sepetin Boş Görünüyor"


SCREENSHOT_DETAILS_BY_BRAND =  r'/Users/standard/Desktop/Python-Selenium-POM-n11.com/screenshots/details_by_brand.png'
SCREENSHOT_DETAILS =  r'/Users/standard/Desktop/Python-Selenium-POM-n11.com/screenshots/details.png'
SCREENSHOT_DETAILS_SUBCATEGORY = r'/Users/standard/Desktop/Python-Selenium-POM-n11.com/screenshots/subcategory.png'