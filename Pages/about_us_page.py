from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AboutUsPage(BasePage):
    video_modal = (By.XPATH, '//div[@id="videoModal"]')
    about_us_close_btn = (By.XPATH, '//div[@id="videoModal"]//button[text()="Close"]')
    about_us_x_btn = (By.XPATH, '//div[@id="videoModal"]//div[@class="modal-header"]/button/span[text()="×"]')
    play_btn = (By.XPATH, '//button[@title="Play Video"]')
    video_player = (By.XPATH, '//*[@id="example-video"]')

    def click_close_button(self):
        located_by, locator_value = self.about_us_close_btn
        self.driver.find_element(located_by, locator_value).click()

    def click_x_icon(self):
        located_by, locator_value = self.about_us_x_btn
        self.driver.find_element(located_by, locator_value).click()

    def play_video(self):
        located_by, locator_value = self.play_btn
        self.driver.find_element(located_by, locator_value).click()

    def assert_modal_is_displayed(self):
        located_by, locator_value = self.video_modal
        modal = self.driver.find_element(located_by, locator_value)
        return self.assertTrue(modal.get_attribute("class").split().__contains__("show"))

    def assert_modal_is_not_displayed(self):
        located_by, locator_value = self.video_modal
        modal = self.driver.find_element(located_by, locator_value)
        return self.assertFalse(modal.get_attribute("class").split().__contains__("show"))

    def assert_video_is_paused(self):
        located_by, locator_value = self.video_player
        player = self.driver.find_element(located_by, locator_value)
        return self.assertTrue(player.get_attribute("class").split().__contains__("vjs-paused"))

    def assert_video_is_playing(self):
        located_by, locator_value = self.video_player
        player = self.driver.find_element(located_by, locator_value)
        return self.assertTrue(player.get_attribute("class").split().__contains__("vjs-playing"))

