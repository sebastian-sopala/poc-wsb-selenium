from logging import log
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class AboutUs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url="https://www.demoblaze.com/")

    def tearDown(self):
        self.driver.close()


    def test_close_form_with_close_button(self):
        about_us_link = self.driver.find_element(By.XPATH, '//a[text()="About us"]')
        video_modal = self.driver.find_element(By.XPATH, '//div[@class="modal fade"] [@id="videoModal"]')
        close_btn = self.driver.find_element(By.XPATH, '//div[@id="videoModal"]//button[text()="Close"]')

        about_us_link.click()
        sleep(1)
        self.assertTrue(video_modal.get_attribute("class").split().__contains__("show"))

        close_btn.click()
        sleep(1)
        self.assertFalse(video_modal.get_attribute("class").split().__contains__("show"))


    def test_close_form_with_X_button(self):
        about_us_link = self.driver.find_element(By.XPATH, '//a[text()="About us"]')
        video_modal = self.driver.find_element(By.XPATH, '//div[@class="modal fade"] [@id="videoModal"]')

        about_us_link.click()
        sleep(1)
        self.assertTrue(video_modal.get_attribute("class").split().__contains__("show"))

        x_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="videoModal"]//div[@class="modal-header"]/button/span[text()="×"]')))
        x_btn.click()
        sleep(1)
        self.assertFalse(video_modal.get_attribute("class").split().__contains__("show"))


    def test_video_is_playing(self):
        about_us_link = self.driver.find_element(By.XPATH, '//a[text()="About us"]')
        
        about_us_link.click()
        sleep(1)

        video_player = self.driver.find_element(By.XPATH, '//*[@id="example-video"]')
        self.assertTrue(video_player.get_attribute("class").split().__contains__("vjs-paused"))

        play_btn = self.driver.find_element(By.XPATH, '//button[@title="Play Video"]')
        sleep(1)
        play_btn.click()
        self.assertTrue(video_player.get_attribute("class").split().__contains__("vjs-playing"))




        