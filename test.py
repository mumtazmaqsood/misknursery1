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


# -------------------------------------------------------------------------------------------------------------------
#        left menus FROM 'THE EMBRACE COLLECTOIN' TO 'CONTACT US'
# -------------------------------------------------------------------------------------------------------------------

    def left_nav1(self):

        side_nav_Menu = driver.find_elements(By.XPATH, "//ul[@class='site-nav side_nav']//li")
        # need iterate from index 6 - 14, left menu items from 'The Embrace Collections, ---> Contact us'
        # 7 is a fix value , dont change otherwise error will occure bcz it iterate on 6-14, which are 8 menus
        # so total len is 15-7 = 8
        for i in range(len(side_nav_Menu)-7):
            # the menu 'the Embrace collection' is on the 6th position
            i = i + 6
            driver.find_elements(By.XPATH, "//ul[@class='site-nav side_nav']//li")[i].click()
            sleep(2)

            emb_Products = driver.find_elements(By.XPATH, "//div[@class = 'grid active-list "
                                                          "grid-list-view grid--uniform grid--view-items']"
                                                          "//div[@class='grid-view-item custom-grid-view']")
            sleep(2)
            # click on product mostly 5 products on each page(choose 0 - 4)
            for emb_Products_Index in range(len(emb_Products)-2):
                emb_Products = driver.find_elements(By.XPATH,
                                                    "//div[@class = 'grid active-list grid-list-view "
                                                    "grid--uniform grid--view-items']"
                                                    "//div[@class='grid-view-item custom-grid-view']")
                emb_Products[emb_Products_Index].click()
                sleep(2)
                # --------------------------------------------------------------------------------------------------------------
                # adding to shopping cart total 15 fields(0 -- 14), on 6th postion , there is 'add to cart' button,
                # thats why loop start 0 --- (15)-9,
                add_to_cart = driver.find_elements(By.XPATH, "//div[@class = 'grid product-single']"
                                                             "//div[@class='product-single__meta']//div")
                for index in range(len(add_to_cart)-9):
                    sleep(2)
                    add_to_cart = driver.find_elements(By.XPATH,
                                         "//div[@class = 'grid product-single']//div[@class="
                                         "'product-single__meta']//div")
                    # select value from dropdown menu 'Type'
                    type_dropdown = Select(driver.find_element_by_id("SingleOptionSelector-0"))
                    type_all_options = len(type_dropdown.options)
                    if type_all_options > 1:
                        type_dropdown.select_by_index(1)
                    else:
                        type_dropdown.select_by_index(0)

                    # select value form dropdown menu 'Size'
                    size_dropdown = Select(driver.find_element_by_id("SingleOptionSelector-1"))
                    size_all_options = len(size_dropdown.options)
                    if size_all_options > 1:
                        size_dropdown.select_by_index(1)
                    else:
                        size_dropdown.select_by_index(0)

                    #--------------------------------------------------------------------------------------------
                    # NEED TO CORRECT BELOW CODE BEACUSE 'THE EMBRACE COLLECTION' 2ND PRODUCT HAS NOT COLOR FIELD
                    # THAT'S WHY THIS CODE GIVES ERROR OTHERWISE FINE
                    # --------------------------------------------------------------------------------------------
                    # select value form dropdown menu 'Colors'
                    # colorDropDown = driver.find_element_by_xpath("//div[@class = 'grid product-single']"
                    #                              "//div[@class='product-single__meta']"
                    #                              "//div[@class='selector-wrapper js product-form__item']"
                    #                              "//select[@id='SingleOptionSelector-2']")
                    #
                    # if not colorDropDown:
                    #     print("Not Found")
                    # else:
                    # color_dropdown = Select(driver.find_element_by_id("SingleOptionSelector-2"))
                    # colors_all_options = color_dropdown.options
                    # color_dropdown.select_by_index(1)
                    sleep(2)
                    # add_to_cart[5] mostly add to cart button , it is not working thats why need if statment
                    if emb_Products_Index == 1 and add_to_cart[index] == add_to_cart[4]:
                        driver.find_element_by_xpath("//div[@class = 'grid product-single']"
                                                     "//div[@class='product-single__meta']"
                                                     "//div[@class='list-inline-cart medium-"
                                                     "-one-half product-form__item product-form__item--submit']"
                                                     "//button[@name='add']").click()
                        sleep(2)
                        driver.back()

                    elif add_to_cart[index] == add_to_cart[5]:
                        driver.find_element_by_xpath("//div[@class = 'grid product-single']"
                                                     "//div[@class='product-single__meta']"
                                                     "//div[@class='list-inline-cart medium-"
                                                     "-one-half product-form__item product-form__item--submit']"
                                                     "//button[@name='add']").click()
                        sleep(2)
                        driver.back()
                    else:
                        add_to_cart[index].click()
                    sleep(2)


                driver.back()
                sleep(2)
            # driver.find_element_by_xpath("//i[@class='fa fa-list']").click()
            driver.back()
#----------------------------------------------------------------------------------------------------------------------
                                            # END OF LEFT MENU
# ---------------------------------------------------------------------------------------------------------------

