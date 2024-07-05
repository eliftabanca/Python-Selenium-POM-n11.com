from selenium.webdriver.common.by import By

BASE_URL ="https://www.n11.com/"

CATEGORY_ELECTRONIC = (By.XPATH , "//*[@id='header']/nav/ul/li[2]/a")
CATEGORY_TEXT = "Elektronik"
CATEGORY_TEXT_LOCATER = (By.LINK_TEXT, "Elektronik")

SUBCATEGORY_COMPUTER = (By.XPATH, "//*[@id='header']/nav/ul/li[2]/div/ul/li[2]/a") 
SUBCATEGORY_TEXT_LOCATOR = (By.XPATH, "//*[@id='breadCrumb']/ul/li[3]/a")
SUBCATEGORY_COMPUTER_TEXT = "Bilgisayar"

SEARCHBOX_LOCATOR = (By.ID, "searchData")
SEARCH_BUTTON_LOCATOR = (By.CLASS_NAME, "iconsSearch")

FILTER_LOCATOR = (By.LINK_TEXT, "Masaüstü Bilgisayar")
FILTER_TEXT_LOCATOR = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[2]/section/div[1]/div[1]/div[1]/div/h1")
FILTER_TEXT = ("Bilgisayar")

BRAND_LOCATOR = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[2]/section/div[1]/div[3]/div/ul/div/div/li[1]/a")
BRAND_TEXT = "Lenovo"
BRAND_TEXT_LOCATOR = (By.XPATH, "//*[@id='contentListing']/div/div[2]/div[2]/section/div[1]/div[1]/div[1]/div/h1/text()")

PRODUCT = (By.ID, "p-555169372")