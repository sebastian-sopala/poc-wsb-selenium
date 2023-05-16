import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def wait_for(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(locator)

    # top navigation selectors
    home_link = (By.XPATH, '//a[text()="Home"]')
    about_us_link = (By.XPATH, '//a[text()="About us"]')
    contact_link = By.XPATH, '//a[text()="Contact"]'

    # contact form selectrors
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

    def open_contact(self):
        self.wait_for(self.contact_link).click()

    def assert_element_class_contains(self, element, value):
        return self.assertTrue(element.get_attribute("class").split().__contains__(value))

    def assert_element_class_not_contains(self, element, value):
        return self.assertFalse(element.get_attribute("class").split().__contains__(value))
