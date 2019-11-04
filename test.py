from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import unittest
import HtmlTestRunner
driver = webdriver.Chrome(executable_path = "C://Users//mumtaz//Desktop//python//selen//drivers//chromedriver.exe")
# driver = webdriver.Chrome(executable_path = '..\drivers\chromedriver.exe')
# driver.get("https://misknursery.com/")
driver.get("https://www.1stdibs.com/")
driver.maximize_window()
driver.implicitly_wait(2)




class Navigation():

# ------------------------------------------------------------------------------------------------
        # left menu 'SHOP COLLECTION -> SUB MENUS'
# ------------------------------------------------------------------------------------------------
    def left_navigation(self):

        shop_submenu = driver.find_elements(By.XPATH, "//div[@class='site-nav__dropdown']//li")
        for subMenu_Index in range(len(shop_submenu)):
            action = ActionChains(driver)
            shop_collection_menu = driver.find_element_by_xpath("//a[@class='site-nav__link "
                                                                "site-nav__link--main']"
                                                                "[contains(text(),'SHOP COLLECTIONS')]")
            action.move_to_element(shop_collection_menu).\
                move_to_element(driver.find_elements(By.XPATH, "//div[@class='site-nav__dropdown']//li")[subMenu_Index])\
                .click().perform()
            driver.implicitly_wait(2)
            cribs_Product = driver.find_elements(By.XPATH, "//div[@class='grid grid-list-view grid--uniform "
                                                           "grid--view-items active-list']"
                                                           "//div[@class='grid__item grid-item grid__"
                                                           "item--collection-template small-"
                                                           "-one-half medium-up--one-quarter']")
            for product_index in range(len(cribs_Product)):
                cribs_Product = driver.find_elements(By.XPATH,
                                                     "//div[@class='grid grid-list-view "
                                                     "grid--uniform grid--view-items active-list']"
                                                     "//div[@class='grid__item grid-item grid__"
                                                     "item--collection-template small--one-half "
                                                     "medium-up--one-quarter']")
                cribs_Product[product_index].click()
                driver.back()
            driver.back()
#----------------------------------------------------------------------------------------------------------------------
                    # END OF SHOP COLLECTION -> SUB MENUS'
# ---------------------------------------------------------------------------------------------------------------
