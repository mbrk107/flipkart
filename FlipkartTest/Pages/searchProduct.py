import time


class ProductSearch:

    def __init__(self, driver):
        self.driver = driver
        self.search_box_input_xpath = "//input[@name='q']"
        self.close_button_login_popup_xpath = "/html/body/div[2]/div/div/button"
        self.flipkart_logo_xpath = "//a/img[@title='Flipkart']"
        self.search_button_xpath = "//button[@type='submit']"
        self.search_popularity_xpath = "//div[text()='Popularity']"
        self.top_first_popularity_search_result_xpath = "//div[text()='Popularity']/following::a[1]"
        self.search_by_price_low_to_high_xpath = "//div[text()='Price -- Low to High']"
        self.top_first_low_to_high_search_result_xpath = "//div[text()='Price -- Low to High']/following::a[1]"
        self.search_by_price_high_to_low_xpath = "//div[text()='Price -- High to Low']"
        self.top_first_high_to_low_search_result_xpath  = "//div[text()='Price -- High to Low']/following::a[1]"
        self.search_by_newest_result_xpath = "//div[text()='Newest First']"
        self.top_first_Newest_search_result_xpath = "//div[text()='Newest First']/following::a[1]"
        self.no_search_results_xpath = "//div[text()='Sorry, no results found!']"
        self.top_first_relevance_search_result_xpath = "//div[text()='Relevance']/following::a[1]"
        self.delivery_to_xpath="//input[@type='text' and @id='pincodeInputId']"
        self.delivery_click_xpath = "//span[text()='Check']"
        self.cart_button_xpath = "//button[text()='ADD TO CART']"
        self.place_order_xpath = "//span[text()='Place Order']"
        self.continue_order_summary_xpath = "//span[@id='to-payment']"
        self.payment_options_xpath = "//span[text()='Payment Options']"
        self.credit_as_payment_option_xpath = "//div[contains(text(),'Credit / Debit / ATM Card')]"
        self.net_banking_as_payment_option_xpath = "//div[text()='Net Banking']"
        self.cart_product_count_xpath = "//div[contains(text(),'My Cart')]/following::input[1]"
        self.cart_xpath = "//span[text()='Cart']"
        self.product_count_from_search_page_cart = "//span[text()='Cart']/preceding-sibling::div"
        self.remove_product_from_cart_xpath = "//div[text()='Remove']"
        #self.remove_product_from_cart_xpath = "//div[text()='Remove']/following::div[text()='Remove']"
        self.remove_item_button_xpath = "//div[text()='Remove Item']/following::div[text()='Remove'][1]"
        self.search_by_customer_ratings_xpath = "//div[text()='Customer Ratings']"
        self.four_star_rating_xpath = "//div[text()='Customer Ratings']/following::input[1]"
        self.three_star_rating_xpath = "//div[text()='Customer Ratings']/following::input[2]"
        self.email_phone_number_input_xpath = "//span[text()='Login'][1]/following::input[1]"
        self.password_input_xpath = "//span[text()='Login'][1]/following::input[2]"
        self.login_button_xpath = "//span[text()='Get access to your Orders, Wishlist and Recommendations']/following::button[@type='submit']"
        self.invalid_password_error_msg_xpath = "//span[text()='Your username or password is incorrect']"
        self.invalid_username_error_msg_xpath = "//span[text()='Please enter valid Email ID/Mobile number']"
        self.user_menu_logout_xpath = "//div[contains(text(),'uname')]"
        self.logout_button_xpath = "//div[text()='Logout']"
        self.close_login_popup = "//div[@class='mCRfo9']/descendant::button[1]"



    def verify_search_based_on_price_low_to_high(self):
        status = self.driver.find_element_by_xpath(self.search_by_price_low_to_high_xpath).is_displayed()
        return status

    def click_search_filter_price_low_to_high(self):
        self.driver.find_element_by_xpath(self.search_by_price_low_to_high_xpath).click()
        time.sleep(6)

    def verify_search_based_on_price_high_to_low(self):
        status = self.driver.find_element_by_xpath(self.search_by_price_high_to_low_xpath).is_displayed()
        return status

    def click_search_filter_price_high_to_low(self):
        self.driver.find_element_by_xpath(self.search_by_price_high_to_low_xpath).click()
        time.sleep(6)

    def verify_search_based_on_popularity(self):
        status = self.driver.find_element_by_xpath(self.search_popularity_xpath).is_displayed()
        return status

    def click_search_filter_popularity(self):
        self.driver.find_element_by_xpath(self.search_popularity_xpath).click()
        time.sleep(6)

    def click_remove_from_remove_item_popup(self):
        self.driver.find_element_by_xpath(self.remove_item_button_xpath).click()

    def verify_existance_of_logo(self):
        status = self.driver.find_element_by_xpath(self.flipkart_logo_xpath).is_displayed()
        return status

    def click_flipkart_home(self):
        self.driver.find_element_by_xpath(self.flipkart_logo_xpath).click()

    def verify_cart_on_search_page(self):
        status = self.driver.find_element_by_xpath(self.cart_xpath).is_displayed()
        return status

    def click_cart(self):
        self.driver.find_element_by_xpath(self.cart_xpath).click()

    def remove_product_from_cart(self):
        self.driver.find_element_by_xpath(self.remove_product_from_cart_xpath).click()

    def close_login_popup(self):
        self.driver.find_element_by_xpath(self.close_button_login_popup_xpath).click()

    def verify_search_box(self):
        status = self.driver.find_element_by_xpath(self.search_box_input_xpath).is_displayed()
        return status

    def verify_search_button(self):
        status = self.driver.find_element_by_xpath(self.search_button_xpath).is_enabled()
        return status

    def search_product(self, search_key):
        self.driver.find_element_by_xpath(self.search_box_input_xpath).clear()
        self.driver.find_element_by_xpath(self.search_box_input_xpath).send_keys(search_key)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.search_button_xpath).click()
        time.sleep(15)
    def no_search_results(self):
        text = self.driver.find_element_by_xpath(self.no_search_results_xpath).text
        return text

    #self.delivery_to_xpath = "//input[@type='text' and @id='pincodeInputId']"
    #self.delivery_click_xpath = "//span[text()='Check']"

    def deliver_product(self,search_key):
        self.driver.find_element_by_xpath(self.delivery_to_xpath).clear()
        self.driver.find_element_by_xpath(self.delivery_to_xpath).send_keys(search_key)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.delivery_click_xpath ).click()
        time.sleep(10)

    def verify_top_first_relevance_search_item(self):
        status = self.driver.find_element_by_xpath(self.top_first_relevance_search_result_xpath).is_displayed()
        return status
    def click_on_top_first_item(self):
        self.driver.find_element_by_xpath(self.top_first_relevance_search_result_xpath).click()

    def switch_to_cart_page(self):
        handles = self.driver.window_handles
        parent_handle = handles[0]
        child_handle = handles[1]
        self.driver.switch_to.window(child_handle)
        return parent_handle


    def verify_add_to_cart_button(self):
        web_element_status = self.driver.find_element_by_xpath(self.cart_button_xpath).is_enabled()
        return web_element_status

    def add_product_to_cart(self):
        self.driver.find_element_by_xpath(self.cart_button_xpath).click()

    def verify_place_order_button(self):
        web_element_status = self.driver.find_element_by_xpath(self.place_order_xpath).is_enabled()
        return web_element_status

    def click_place_order(self):
        self.driver.find_element_by_xpath(self.place_order_xpath).click()

    def verify_continue_order_summary_button(self):
        web_element_status = self.driver.find_element_by_xpath(self.continue_order_summary_xpath).is_displayed()
        return web_element_status

    def click_continue_from_order_summary(self):
        self.driver.find_element_by_xpath(self.continue_order_summary_xpath).click()

    def verify_payment_option_section(self):
        web_element_status = self.driver.find_element_by_xpath(self.payment_options_xpath).is_displayed()
        return web_element_status

    def select_payment_option(self, payment_option):
        if payment_option == "Credit / Debit / ATM Card":
            payment = self.driver.find_element_by_xpath(self.credit_as_payment_option_xpath)
            payment.click()
        elif payment_option == "Net Banking":
            payment = self.driver.find_element_by_xpath(self.net_banking_as_payment_option_xpath)
            payment.click()
        # self.payment_options_xpath = "//span[text()='Payment Options']"
        # self.credit_as_payment_option_xpath = "//div[contains(text(),'Credit / Debit / ATM Card')]"
        # self.net_banking_as_payment_option_xpath = "//div[text()='Net Banking']"

        # self.search_by_customer_ratings_xpath = "//div[text()='Customer Ratings']"
        # self.four_star_rating_xpath = "//div[text()='Customer Ratings']/following::input[1]"
        # self.three_star_rating_xpath = "//div[text()='Customer Ratings']/following::input[2]"

    def verify_customer_ratings_options(self):
        web_element_status = self.driver.find_element_by_xpath(self.search_by_customer_ratings_xpath).is_displayed()
        return web_element_status

    def select_customer_ratings(self,customer_ratings):
        if customer_ratings == "4★ & above":
            rating = self.driver.find_element_by_xpath(self.four_star_rating_xpath ).click()
        elif customer_ratings == "3★ & above":
            rating = self.driver.find_element_by_xpath(self.three_star_rating_xpath).click()




