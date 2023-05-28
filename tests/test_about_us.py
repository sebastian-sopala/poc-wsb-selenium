import unittest
from selenium import webdriver
from time import sleep
from Pages.home_page import HomePage
from Pages.about_us_page import AboutUsPage


class AboutUs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url="https://www.demoblaze.com/")

    def tearDown(self):
        self.driver.close()

    def test_close_form_with_close_button(self):
        # TODO can i refactor this boilerplate
        about_us_page = AboutUsPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_about_us()
        sleep(1)
        about_us_page.assert_modal_is_displayed()

        about_us_page.click_close_button()
        sleep(1)
        about_us_page.assert_modal_is_not_displayed()

    def test_close_form_with_X_button(self):
        about_us_page = AboutUsPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_about_us()
        sleep(1)
        about_us_page.assert_modal_is_displayed()

        about_us_page.click_x_icon()
        sleep(1)
        about_us_page.assert_modal_is_not_displayed()

    def test_video_is_playing(self):
        about_us_page = AboutUsPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.open_about_us()
        sleep(1)
        about_us_page.assert_video_is_paused()

        about_us_page.play_video()
        sleep(1)
        about_us_page.assert_video_is_playing()
