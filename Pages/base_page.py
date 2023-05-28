import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This is a parent class to all pages"""
"""it contains generic methods and utilities"""


class BasePage(unittest.TestCase):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def click_on(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def wait_for(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def input_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
