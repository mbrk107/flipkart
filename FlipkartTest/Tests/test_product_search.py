import logging
import time
from Pages.loginPage import LoginPage
from Pages.searchProduct import ProductSearch
from Tests.test_base import TestBase
import unittest


class TestProductSearch(TestBase):

    @classmethod
    def setUp(cls):
        global lp
        lp = LoginPage(cls.driver)
        #logging.info("entered phone number : 8970907650")
        lp.enter_email_phone("8970907650")
        #logging.info("entered password : honeyb19")
        lp.enter_password("honeyb19")
        #logging.info("logging into the application")
        lp.click_login()
        time.sleep(10)

    @classmethod
    def tearDown(cls):
         pass

    ##Search product by brand name #########

    # def test_search_product_by_brand_name(self):
    #     ps = ProductSearch(self.driver)
    #     self.assertTrue(ps.verify_search_box(), "Search bar not displayed...")
    #     #logging.info("searching product by searchkey : Samsung Galaxy S9 Plus (Midnight Black, 64 GB)")
    #     ps.search_product("samsun")
    #     self.assertTrue(ps.verify_top_first_relevance_search_item(), "No Results found with the search key")
    #     #ps.deliver_product("500081")
    #     ps.click_on_top_first_item()
    #     time.sleep(10)
    #     parent_window_handle = ps.switch_to_cart_page()
    #     self.assertTrue(ps.verify_add_to_cart_button(), "Add to cart option not available")
    #     ps.add_product_to_cart()
    #     time.sleep(10)
    #     self.assertTrue(ps.verify_place_order_button(), "Place order option not available")
    #     ps.click_place_order()
    #     time.sleep(5)
    #     self.assertTrue(ps.verify_continue_order_summary_button(), "Continue from Order Summary Option not available")
    #     ps.click_continue_from_order_summary()
    #     time.sleep(5)
    #     self.assertTrue(ps.verify_payment_option_section(), "Payment Option Section not present")
    #     ps.select_payment_option("Net Banking")
    #     time.sleep(5)
    #     self.driver.switch_to.window(parent_window_handle)
    #     time.sleep(5)
    #     self.driver.refresh()
    #     self.assertTrue(ps.verify_cart_on_search_page(), "cart button not avaibale on search page")
    #     ps.click_cart()
    #     time.sleep(5)
    #     ps.remove_product_from_cart()
    #     ps.click_remove_from_remove_item_popup()


#### Search_product_based_on_popularity #######


    def test_search_product_based_on_popularity(self):
        ps = ProductSearch(self.driver)
        self.assertTrue(ps.verify_search_box(), "Search bar not displayed...")
        ps.search_product("electronics")
        self.assertTrue(ps.verify_search_based_on_popularity(), "Search By Popularity Option not available")
        ps.deliver_product("500082")
        ps.click_search_filter_popularity()
        self.assertTrue(ps.verify_top_first_relevance_search_item(), "No Results found with the search key")
        ps.click_on_top_first_item()
        time.sleep(10)
        parent_window_handle = ps.switch_to_cart_page()
        self.assertTrue(ps.verify_add_to_cart_button(), "Add to cart option not available")
        ps.add_product_to_cart()
        time.sleep(10)
        self.assertTrue(ps.verify_place_order_button(), "Place order option not available")
        ps.click_place_order()
        time.sleep(5)
        self.assertTrue(ps.verify_continue_order_summary_button(), "Continue from Order Summary Option not available")
        ps.click_continue_from_order_summary()
        time.sleep(5)
        self.assertTrue(ps.verify_payment_option_section(), "Payment Option Section not present")
        ps.select_payment_option("Net Banking")
        time.sleep(5)
        self.driver.switch_to.window(parent_window_handle)
        time.sleep(5)
        self.driver.refresh()
        self.assertTrue(ps.verify_cart_on_search_page(), "cart button not avaibale on search page")
        ps.click_cart()
        time.sleep(5)
        ps.remove_product_from_cart()
        ps.click_remove_from_remove_item_popup()


####  Search_product by LOW_TO_HIGH  ####

    # def test_search_product_based_on_price_low_to_high(self):
    #     ps = ProductSearch(self.driver)
    #     self.assertTrue(ps.verify_search_box(), "Search bar not displayed...")
    #     ps.search_product("oppo f11 pro")
    #     self.assertTrue(ps.verify_search_based_on_price_low_to_high(), "Search By Popularity Option not available")
    #     ps.click_search_filter_price_low_to_high()
    #     self.assertTrue(ps.verify_top_first_relevance_search_item(), "No Results found with the search key")
    #     ps.click_on_top_first_item()
    #     time.sleep(10)
    #     parent_window_handle = ps.switch_to_cart_page()
    #     self.assertTrue(ps.verify_add_to_cart_button(), "Add to cart option not available")
    #     ps.add_product_to_cart()
    #     time.sleep(10)
    #     self.assertTrue(ps.verify_place_order_button(), "Place order option not available")
    #     ps.click_place_order()
    #     time.sleep(5)
    #     self.assertTrue(ps.verify_continue_order_summary_button(), "Continue from Order Summary Option not available")
    #     ps.click_continue_from_order_summary()
    #     time.sleep(5)
    #     self.assertTrue(ps.verify_payment_option_section(), "Payment Option Section not present")
    #     ps.select_payment_option("Net Banking")
    #     time.sleep(5)
    #
    #     self.driver.switch_to.window(parent_window_handle)
    #     time.sleep(5)
    #     self.driver.refresh()
    #     self.assertTrue(ps.verify_cart_on_search_page(), "cart button not avaibale on search page")
    #     ps.click_cart()
    #     time.sleep(5)
    #     ps.remove_product_from_cart()
    #     ps.click_remove_from_remove_item_popup()
    #


####      Search_product by HIGH_TO_LOW   #####

#     def test_search_product_based_on_price_high_to_low(self):
#         ps = ProductSearch(self.driver)
#         self.assertTrue(ps.verify_search_box(), "Search bar not displayed...")
#         ps.search_product("oppo f11 pro")
#         self.assertTrue(ps.verify_search_based_on_price_high_to_low(), "Search Byhigh to low Option not available")
#         ps.click_search_filter_price_high_to_low()
#         self.assertTrue(ps.verify_top_first_relevance_search_item(), "No Results found with the search key")
#         ps.click_on_top_first_item()
#         time.sleep(10)
#         parent_window_handle = ps.switch_to_cart_page()
#         self.assertTrue(ps.verify_add_to_cart_button(), "Add to cart option not available")
#         ps.add_product_to_cart()
#         time.sleep(10)
#         self.assertTrue(ps.verify_place_order_button(), "Place order option not available")
#         ps.click_place_order()
#         time.sleep(5)
#         self.assertTrue(ps.verify_continue_order_summary_button(), "Continue from Order Summary Option not available")
#         ps.click_continue_from_order_summary()
#         time.sleep(5)
#         self.assertTrue(ps.verify_payment_option_section(), "Payment Option Section not present")
#         ps.select_payment_option("Net Banking")
#         time.sleep(5)
#
#         self.driver.switch_to.window(parent_window_handle)
#         time.sleep(5)
#         self.driver.refresh()
#         self.assertTrue(ps.verify_cart_on_search_page(), "cart button not avaibale on search page")
#         ps.click_cart()
#         time.sleep(5)
#         ps.remove_product_from_cart()
#         ps.click_remove_from_remove_item_popup()
#
# ####  search product by invalid product ###
#
#     def test_search_product_by_invalid_product_name(self):
#         ps = ProductSearch(self.driver)
#         self.assertTrue(ps.verify_search_box(), "Search bar not displayed...")
#         #logging.info("searching product which is not availabe")
#         ps.search_product("adsfadf")
#         expected_msg = "Sorry, no results found!"




    # def test_search_product_based_on_Customer_ratings(self):
    #     ps = ProductSearch(self.driver)
    #     self.assertTrue(ps.verify_search_box(), "Search bar not displayed...")
    #     ps.search_product("oppo f11 pro")
    #     time.sleep(5)
    #     self.assertTrue(ps.verify_customer_ratings_options(), "Customer rating options not present")
    #     ps.select_payment_option("4★ & above")
    #     time.sleep(5)
    #     self.assertTrue(ps.verify_top_first_relevance_search_item(), "No Results found with the search key")
    #     ps.click_on_top_first_item()
    #     time.sleep(10)
    #     parent_window_handle = ps.switch_to_cart_page()
    #     self.assertTrue(ps.verify_add_to_cart_button(), "Add to cart option not available")
    #     ps.add_product_to_cart()
    #     time.sleep(10)
    #     self.assertTrue(ps.verify_place_order_button(), "Place order option not available")
    #     ps.click_place_order()
    #     time.sleep(5)
    #     self.assertTrue(ps.verify_continue_order_summary_button(), "Continue from Order Summary Option not available")
    #     ps.click_continue_from_order_summary()
    #     time.sleep(5)
    #     self.assertTrue(ps.verify_payment_option_section(), "Payment Option Section not present")
    #     ps.select_payment_option("Net Banking")
    #     time.sleep(5)
    #     self.driver.switch_to.window(parent_window_handle)
    #     time.sleep(5)
    #     self.driver.refresh()
    #     self.assertTrue(ps.verify_cart_on_search_page(), "cart button not avaibale on search page")
    #     ps.click_cart()
    #     time.sleep(5)
    #     ps.remove_product_from_cart()
    #     ps.click_remove_from_remove_item_popup()


if __name__ == "__main__":
    unittest.main()