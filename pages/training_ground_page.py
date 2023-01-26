from selenium.webdriver.common.by import By

from pages.base_element import BaseElement

class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://techstepacademy.com/training-ground"

    def go(self):
        self.driver.get(self.url)

    @property # Added "@property" to allow using "trng_page.button1.click()" instead of "trng_page.button1().click()"
    def button1(self):
        locator = (By.ID, 'b1')
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )

    def close_alert(self):
        try:
            self.driver.switch_to.alert.accept()
        except NoAlertPresentException:
            return False