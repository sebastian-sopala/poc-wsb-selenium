from logging import log
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from HomePageSelectors import HomePageSelectors
from selenium.webdriver.common.alert import Alert


class TheTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        # self.driver.maximize_window()
        self.driver.get(url="https://www.demoblaze.com/")

    def tearDown(self):
        self.driver.close()


    def test_close_form_with_close_button(self):
        contact_link = self.driver.find_element(By.XPATH, '//a[@class="nav-link" and text()="Contact"]')
        close_btn = self.driver.find_element(By.XPATH, '//*[text()="Close"]')
        modal_open = self.driver.find_element(By.XPATH, '//div[@class="modal fade"] [@id="exampleModal"]')
        

        contact_link.click()
        sleep(1)
        self.assertTrue(modal_open.get_attribute("class").split().__contains__("show"))

        close_btn.click()
        sleep(1)
        self.assertFalse(modal_open.get_attribute("class").split().__contains__("show"))


    def test_close_form_with_X_button(self):
        contact_link = self.driver.find_element(By.XPATH, '//a[@class="nav-link" and text()="Contact"]')
        modal_open = self.driver.find_element(By.XPATH, '//div[@class="modal fade"] [@id="exampleModal"]')

        contact_link.click()
        sleep(1)
        self.assertTrue(modal_open.get_attribute("class").split().__contains__("show"))

        x_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="exampleModal"]//div[@class="modal-header"]/button/span[text()="×"]')))

        x_btn.click()
        sleep(1)
        self.assertFalse(modal_open.get_attribute("class").split().__contains__("show"))

    def test_sucefully_send_message(self):
        contact_link = self.driver.find_element(By.XPATH, '//a[@class="nav-link" and text()="Contact"]')
        modal_open = self.driver.find_element(By.XPATH, '//div[@class="modal fade"] [@id="exampleModal"]')

        contact_link.click()
        sleep(1)

        email_field = self.driver.find_element(By.XPATH, '//*[@id="recipient-email"]')
        email_field.send_keys("test@wsb.pl")
        sleep(1)

        name_field = self.driver.find_element(By.XPATH, '//*[@id="recipient-name"]')
        name_field.send_keys("Bob")
        sleep(1)

        message_field = self.driver.find_element(By.XPATH, '//*[@id="message-text"]')
        message_field.send_keys("Uncle Bob testing the form !!!")
        sleep(1)

        send_btn = self.driver.find_element(By.XPATH, '//*[text()="Send message"]')
        send_btn.click()
        sleep(1)

        alert = Alert(self.driver)

        # alert2 = self.driver.switch_to.alert  ????????

        self.assertTrue(alert)
        alert.accept()







        # consent = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(HomePageSelectors.accept_consent_btn))
        # consent.click()
        # sleep(1) # TODO - change this
        # # WebDriverWait(self.driver, 10).until_not(EC.staleness_of(self.driver.find_element(By.CLASS_NAME, "dupa")))

        # top_nav_list = self.driver.find_elements(By.XPATH, HomePageSelectors.top_nav_list)
        # print(len(top_nav_list))

        # scores_btn = self.driver.find_element(By.XPATH, HomePageSelectors.scores_btn)
        # scores_btn.click()

        # scores_header = self.driver.find_element(By.XPATH, HomePageSelectors.scores_header)
        # self.assertTrue(scores_header. is_displayed)

        # # Get scroll height
        # last_height = self.driver.execute_script("return document.body.scrollHeight")

        # while True:
        #     # Scroll down to bottom
        #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #     # Wait to load page
        #     sleep(1)

        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = self.driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height




if __name__ == "__main__":
    unittest.main(verbosity=2)
