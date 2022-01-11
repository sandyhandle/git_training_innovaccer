import sys
sys.path.append("/home/i1582/Downloads/Mayank_POM_assignment/Testing_Swag") 

from selenium import webdriver
import unittest
from test_config import *
from Config.config import *
from page_object.pages.login import Login
import HtmlTestRunner
# import time

class TestLogin(unittest.TestCase):
    driver = setUp()
    
    def test_valid_login(self):
        self.driver.get(Config.PROJECT_BASE_URL)
        Login.doLogin(self, self.driver)
        self.assertEqual(Config.INVENTRY_URL, self.driver.current_url, "Invalid Login")

    

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="testing_output"))



