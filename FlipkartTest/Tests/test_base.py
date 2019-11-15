import time
import logging
from selenium import webdriver
import unittest
import json
from Pages.loginPage import LoginPage

logging.basicConfig(filename="../logs.log",format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)
with open('../locators.json') as f:
    data = json.load(f)

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #logging.info("SETTING UP BROWSER CONFIGURATIONS")
        cls.driver = webdriver.Firefox(executable_path="E:..//DriverExecutables//geckodriver.exe")
        #logging.info("Maximizing Browser")
        cls.driver.maximize_window()
        #logging.info("Launching the Application")
        cls.driver.implicitly_wait(20)
        cls.driver.get("https://www.flipkart.com/")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.driver.close()
        #logging.info("closing browser")


