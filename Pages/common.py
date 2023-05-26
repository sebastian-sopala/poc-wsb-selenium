from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Common(object):
    pass
    # def __init__(self, driver):
    #     self.driver = driver
    #     self._wait = WebDriverWait(self.driver, 10)
    #
    # def wait_for(self, locator):
    #     return self._wait.until(EC.presence_of_element_located(locator))
    #
    # def find(self, locator):
    #     return self.driver.find_element(locator)
