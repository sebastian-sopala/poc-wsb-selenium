import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert
from Pages.home_page import HomePage

from Pages.contact_page import ContactPage


class Contact(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url="https://www.demoblaze.com/")

    def tearDown(self):
        self.driver.close()

    def test_close_form_with_close_button(self):
        # TODO can i refactor this boilerplate
        contact_page = ContactPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_contact()
        sleep(1)  # TODO remove this
        contact_page.assert_modal_is_displayed()

        contact_page.click_close_button()
        sleep(1)
        contact_page.assert_modal_is_not_displayed()

    def test_close_form_with_X_button(self):
        contact_page = ContactPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_contact()
        sleep(1)
        contact_page.assert_modal_is_displayed()

        contact_page.click_x_icon()
        sleep(1)
        contact_page.assert_modal_is_not_displayed()

    def test_successfully_send_message(self):
        contact_page = ContactPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_contact()
        sleep(1)

        text_email = "test@wsb.pl"
        contact_page.input_text(text_email, contact_page.contact_email_field)
        sleep(1)

        text_name = "Bob"
        contact_page.input_text(text_name, contact_page.contact_name_field)
        sleep(1)

        text_message = "Uncle Bob testing the form !!!"
        contact_page.input_text(text_message, contact_page.contact_message_field)
        sleep(1)

        contact_page.click_send_button()
        sleep(1)

        alert = Alert(self.driver)

        # TODO assertTrue ??
        self.assertTrue(alert)
        self.assertEquals(alert.text, "Thanks for the message!!")
        alert.accept()


if __name__ == "__main__":
    unittest.main(verbosity=2)
