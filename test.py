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



# -------------------------------------------------------------------------------------------------------------------
#                               SHOPPING CART
# -------------------------------------------------------------------------------------------------------------------

    def shopping_cart(self):

        driver.find_element_by_xpath("//div[@id='shopify-section-header']//li[4]//a[1]//i[1]").click()
        sleep(2)

        # XPATH OF QUANTITY BOX
        change_quantity = driver.find_elements(By.XPATH, "//div[@class='grid']//div[@class='grid__item medium-"
                                                         "-up-three-fifths']//form[@class='cart']"
                                                         "//table//tr//td[4]//div//input")
        quantity = len(change_quantity)
        for i in range(quantity):
            change_quantity = driver.find_elements(By.XPATH, "//div[@class='grid']//div[@class='grid__item medium-"
                                                             "-up-three-fifths']//form[@class='cart']"
                                                                 "//table//tr//td[4]//div//input")

            #putting different values in quantity box , other than digit
            if i == 0:
                change_quantity[i].clear()
                change_quantity[i].send_keys("1.1")
            elif i == 1:
                change_quantity[i].clear()
                change_quantity[i].send_keys(-1)
            elif i == 2:
                change_quantity[i].clear()
                change_quantity[i].send_keys("@")
            else:
                change_quantity[i].clear()
                change_quantity[i].send_keys(0)

        # XPATH OF UPDATE
        driver.find_element_by_xpath("//div[@id='shopify-section-cart-template']"
                                     "//div[@class='page-width']//form[@action='/cart']"
                                     "/input[@name='update']").click()
        sleep(2)
        # XPATH OF CONTINOU SHOPPING
        driver.find_element_by_xpath("//a[@class='btn btn--secondary cart__update cart_"
                                                        "_continue--large small--hide']").click()
        sleep(2)

# -------------------------------------------------------------------------------------------------------------------
#        END OF SHOPPING CART
# -------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------
#        CHECKOUT MENU
# -------------------------------------------------------------------------------------------------------------------

    def checkOut(self):

        driver.find_element_by_xpath("//div[@id='shopify-section-header']//li[4]//a[1]//i[1]").click()
        sleep(2)
        driver.find_element(By.XPATH, "//input[@name='checkout']").click()
        sleep(2)

        # form elements
        cus_Name = driver.find_element(By.XPATH,"//input[@id='checkout_email_or_phone']")
        cus_Name.send_keys("m@abc.com")
        sleep(1)
        chk_box = driver.find_element_by_xpath("//input[@id='checkout_buyer_accepts_marketing']")
        if chk_box.is_selected():
            chk_box.click()
        else:
            chk_box.click()
        sleep(2)

        # Customer details
        customer_Detail = driver.find_elements(By.XPATH, "//div[@class='section__content']//input")
        for i in range(len(customer_Detail)):
            customer_Detail = driver.find_elements(By.XPATH, "//div[@class='section__content']//input")
            # input boxes starts from 14 and ends on 22
            i = i + 14
            if i == 14:
                customer_Detail[i].send_keys("M")
            elif i == 15:
                customer_Detail[i].send_keys("Ma")
            elif i == 16:
                customer_Detail[i].send_keys("Software Testing")
            elif i == 17:
                customer_Detail[i].send_keys("goje xladsaxe")
            elif i == 18:
                customer_Detail[i].send_keys("33")
            elif i == 19:
                customer_Detail[i].send_keys("Copenhagen")
            elif i == 20:
                country_option = Select(driver.find_element_by_xpath("//div[@class = 'field__input-wrapper"
                                                                     " field__input-wrapper--select']//select"))

                country_option.select_by_visible_text("Pakistan")
            elif i == 21:
                customer_Detail[i].send_keys("2800")
            elif i == 22:
                customer_Detail[i].send_keys("000000000")
            elif i == 23 or i == 24:
                i = i + 1
            elif i == 25:
                if not customer_Detail[i].is_selected():
                    customer_Detail[i].click()
                else:
                    customer_Detail[i].click()
            sleep(2)

        continue_Shopping = driver.find_element_by_xpath("//button[@id='continue_button']")
        continue_Shopping.click()
        sleep(2)
        return_cusInfo = driver.find_element_by_xpath("//div[@class='step__footer']//a")
        return_cusInfo.click()
        sleep(2)
        driver.find_element_by_xpath("//button[@id='continue_button']").click()
        sleep(2)
        continue_Payment = driver.find_element_by_xpath("//button[@id='continue_button']")
        continue_Payment.click()
        sleep(2)

# -------------------------------------------------------------------------------------------------------------------
#        END OF CHECKOUT
# -------------------------------------------------------------------------------------------------------------------
