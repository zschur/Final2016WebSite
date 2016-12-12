# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        if os.name=='nt':
            self.browser = webdriver.Chrome()
        else:
            self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get('http://localhost:8000/index.html')


if __name__=="__main__":
        unittest.main(warnings="ignore")

