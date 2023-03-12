from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locator import Locator


class TrialPage(BasePage):
    url = 'https://techstepacademy.com/trial-of-the-stones'

    # Stone elements
    @property
    def stone_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r1Input')
        # return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def stone_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r1Btn')
        # return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def stone_answer(self):
        locator = Locator(By.CSS_SELECTOR, 'div#passwordBanner')
        # return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
        return BaseElement(driver=self.driver, locator=locator)

    # Secrets elements
    @property
    def secrets_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r2Input')
        # return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def secrets_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r2Butn')
        # return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def secrets_answer(self):
        locator = Locator(By.CSS_SELECTOR, 'div#successBanner1')
        # return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
        return BaseElement(driver=self.driver, locator=locator)

    # Merchants
    @property
    def merchant_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r3Input')
        # return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def merchant_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r3Butn')
        # return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def merchants_answer(self):
        locator = Locator(By.CSS_SELECTOR, 'div#successBanner2')
        # return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
        return BaseElement(driver=self.driver, locator=locator)
