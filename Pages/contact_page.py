from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ContactPage(BasePage):

    contact_close_btn = (By.XPATH, '//div[@id="exampleModal"]//button[text()="Close"]')
    contact_modal = (By.XPATH, '//div[@id="exampleModal"]')
    contact_x_btn = (By.XPATH, '//div[@id="exampleModal"]//div[@class="modal-header"]/button/span[text()="×"]')
    contact_email_field = (By.XPATH, '//*[@id="recipient-email"]')
    contact_name_field = (By.XPATH, '//*[@id="recipient-name"]')
    contact_message_field = (By.XPATH, '//*[@id="message-text"]')
    contact_send_btn = (By.XPATH, '//*[text()="Send message"]')

    def click_close_button(self):
        located_by, locator_value = self.contact_close_btn
        self.driver.find_element(located_by, locator_value).click()

    def click_x_icon(self):
        located_by, locator_value = self.contact_x_btn
        self.driver.find_element(located_by, locator_value).click()

    def assert_modal_is_displayed(self):
        located_by, locator_value = self.contact_modal
        modal = self.driver.find_element(located_by, locator_value)
        return self.assertTrue(modal.get_attribute("class").split().__contains__("show"))

    def assert_modal_is_not_displayed(self):
        located_by, locator_value = self.contact_modal
        modal = self.driver.find_element(located_by, locator_value)
        return self.assertFalse(modal.get_attribute("class").split().__contains__("show"))

    def input_text(self, text, input_field):
        located_by, locator_value = input_field
        input_field = self.driver.find_element(located_by, locator_value)
        input_field.send_keys(text)

    def click_send_button(self):
        located_by, locator_value = self.contact_send_btn
        self.driver.find_element(located_by, locator_value).click()
