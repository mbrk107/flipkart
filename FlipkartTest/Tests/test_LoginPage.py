import unittest
from selenium import webdriver
from Pages.loginPage import LoginPage
import time
from Tests.test_base import TestBase


class LoginPageTests(TestBase):
    global loginpage

    def test_login_with_valid_username_invalid_password(self):
        loginpage = LoginPage(self.driver)
        self.assertTrue(loginpage.verify_email_phone_number_field(), "Email or Phone Number Field doesnot exists")
        loginpage.enter_email_phone("8970907650")
        self.assertTrue(loginpage.verify_password_input_field(), "Password input field doesnot exists")
        loginpage.enter_password("asldkfj")
        self.assertTrue(loginpage.verify_login_button(), "Login Button Not enabled")
        loginpage.click_login()
        time.sleep(10)
        expected_error_msg = "Please enter valid Email ID/Mobile number"
        self.assertEqual(expected_error_msg, loginpage.get_error_msg_for_invalid_username())
        loginpage.close_login_popup()

    def test_login_with_invalid_credentials(self):
        loginpage = LoginPage(self.driver)
        self.assertTrue(loginpage.verify_email_phone_number_field(), "Email or Phone Number Field doesnot exists")
        loginpage.enter_email_phone("897090765")
        self.assertTrue(loginpage.verify_password_input_field(), "Password input field doesnot exists")
        loginpage.enter_password("honey")
        self.assertTrue(loginpage.verify_login_button(), "Login Button Not enabled")
        loginpage.click_login()
        time.sleep(10)
        expected_error_msg = "Your username or password is incorrect"
        self.assertEqual(expected_error_msg, loginpage.get_error_msg_for_invalid_password(), "Login Successful..")
        loginpage.close_login_popup()

