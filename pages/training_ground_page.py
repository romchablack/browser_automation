from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locator import Locator

class TrainingGroundPage(BasePage):

    url = "https://techstepacademy.com/training-ground"

    # moved to base_page.py
    # def __init__(self, driver):
    #     self.driver = driver
    #     self.url = "https://techstepacademy.com/training-ground"

    # moved to base_page.py
    # def go(self):
    #     self.driver.get(self.url)

    @property # Added "@property" to allow using "trng_page.button1.click()" instead of "trng_page.button1().click()"
    def button1(self):
        # locator = (By.ID, 'b1')
        locator = Locator(by=By.ID, value='b1')
        return BaseElement(
            driver=self.driver,
            # by=locator[0],
            # value=locator[1]
            locator=locator
        )

    def close_alert(self):
        try:
            self.driver.switch_to.alert.accept()
        except NoAlertPresentException:
            return False
