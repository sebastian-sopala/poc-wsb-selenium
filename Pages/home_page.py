import unittest
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    # top navigation selectors
    HOME_LINK = (By.XPATH, '//a[text()="Home "]')
    ABOUT_US_LINK = (By.XPATH, '//a[text()="About us"]')
    CONTACT_LINK = (By.XPATH, '//a[text()="Contact"]')
    CART_LINK = (By.XPATH, '//a[text()="Cart"]')

    def open_contact(self):
        self.driver.find_element(self.CONTACT_LINK).click()

    def open_about_us(self, about_us_link):
        self.driver.find_element(self.ABOUT_US_LINK).click()

    def open_cart(self, about_us_link):
        self.driver.find_element(self.CART_LINK).click()

    # contact form selectors
    contact_close_btn = (By.XPATH, '//div[@id="exampleModal"]//button[text()="Close"]')
    contact_modal = (By.XPATH, '//div[@class="modal fade"] [@id="exampleModal"]')
    contact_x_btn = (By.XPATH, '//div[@id="exampleModal"]//div[@class="modal-header"]/button/span[text()="×"]')
    contact_email_field = (By.XPATH, '//*[@id="recipient-email"]')
    contact_name_field = (By.XPATH, '//*[@id="recipient-name"]')
    contact_message_field = (By.XPATH, '//*[@id="message-text"]')
    contact_send_btn = (By.XPATH, '//*[text()="Send message"]')

    # about us form selectors
    video_modal = (By.XPATH, '//div[@class="modal fade"] [@id="videoModal"]')
    about_us_close_btn = (By.XPATH, '//div[@id="videoModal"]//button[text()="Close"]')
    about_us_x_btn = (By.XPATH, '//div[@id="videoModal"]//div[@class="modal-header"]/button/span[text()="×"]')
    play_btn = (By.XPATH, '//button[@title="Play Video"]')

