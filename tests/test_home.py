from logging import log
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url="https://www.demoblaze.com")

    def tearDown(self):
        self.driver.close()

    def test_home_link(self):
        cart_link = self.driver.find_element(By.XPATH, '//a[text()="Cart"]')

        # there is abug on site when open "https://www.demoblaze.com/cart.html" directly
        cart_link.click()
        sleep(1)
        place_order_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[text()="Place Order"]')))
        self.assertTrue(place_order_btn)

        home_link = self.driver.find_element(By.XPATH, '//a[text()="Home "]')
        home_link.click()

        # self.assertFalse(place_order_btn.is_displayed()) ?????????????

        image_carousel = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="contcar"]')))
        self.assertTrue(image_carousel)
