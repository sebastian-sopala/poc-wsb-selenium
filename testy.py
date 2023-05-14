import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from HomePageSelectors import HomePageSelectors


class TheTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver.implicitly_wait(3)
        # self.driver.maximize_window()
        self.driver.get(url="https://www.goal.com/")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


    def test(self):
        consent = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(HomePageSelectors.accept_consent_btn))
        consent.click()
        sleep(1) # TODO - change this
        # WebDriverWait(self.driver, 10).until_not(EC.staleness_of(self.driver.find_element(By.CLASS_NAME, "dupa")))


        top_nav_list = self.driver.find_elements(By.XPATH, HomePageSelectors.top_nav_list)
        print(len(top_nav_list))


        scores_btn = self.driver.find_element(By.XPATH, HomePageSelectors.scores_btn)
        scores_btn.click()

        scores_header = self.driver.find_element(By.XPATH, HomePageSelectors.scores_header)
        self.assertTrue(scores_header. is_displayed)



        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            sleep(1)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height





if __name__ == "__main__":
    unittest.main(verbosity=2)
