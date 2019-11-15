from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):

        self.driver = driver
        self.email_phone_number_input_xpath = "//span[text()='Login'][1]/following::input[1]"
        self.password_input_xpath = "//span[text()='Login'][1]/following::input[2]"
        self.login_button_xpath = "//span[text()='Get access to your Orders, Wishlist and Recommendations']/following::button[@type='submit']"
        self.invalid_password_error_msg_xpath = "//span[text()='Your username or password is incorrect']"
        self.invalid_username_error_msg_xpath = "//span[text()='Please enter valid Email ID/Mobile number']"
        self.user_menu_logout_xpath = "//div[contains(text(),'uname')]"
        self.logout_button_xpath = "//div[text()='Logout']"
        self.close_login_popup = "//div[@class='mCRfo9']/descendant::button[1]"

    def close_login_popup(self):
        self.driver.find_element_by_xpath(self.close_login_popup()).click()

    def enter_email_phone(self, email_phone):
        self.driver.find_element_by_xpath(self.email_phone_number_input_xpath).send_keys(email_phone)

    def verify_email_phone_number_field(self):
        web_element_status = self.driver.find_element_by_xpath(self.email_phone_number_input_xpath).is_displayed()
        return web_element_status

    def verify_password_input_field(self):
        web_element_status = self.driver.find_element_by_xpath(self.password_input_xpath).is_displayed()
        return web_element_status

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_input_xpath).send_keys(password)

    def verify_login_button(self):
        web_element_status = self.driver.find_element_by_xpath(self.login_button_xpath).is_enabled()
        return web_element_status

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def get_error_msg_for_invalid_username(self):
        error_msg = self.driver.find_element_by_xpath(self.invalid_username_error_msg_xpath).text
        return error_msg

    def get_error_msg_for_invalid_password(self):
        error_msg = self.driver.find_element_by_xpath(self.invalid_password_error_msg_xpath).text
        return error_msg

    def hover_on_user_menu_click_on_logout(self, username):
        web_element = self.user_menu_logout_xpath.replace("uname", "username")
        user_menu = self.driver.find_element(By.XPATH,web_element)
        actions = ActionChains(self.driver)
        actions.move_to_element(user_menu).move_to_element(self.logout_button_xpath).click().perform()



