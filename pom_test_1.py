from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://techstepacademy.com/training-ground"

    def go(self):
        self.driver.get(self.url)

    def type_into_input(self, text):
        inpt = self.driver.find_element(By.ID, "ipt1")
        inpt.clear()
        inpt.send_keys(text)
        return None

    def get_input_text(self):
        inpt = self.driver.find_element(By.ID, "ipt1")
        elem_text = inpt.get_attribute('value')
        return elem_text

    def click_button_1(self):
        bttn1 = self.driver.find_element(By.ID, "b1")
        bttn1.click()
        return None

    def close_alert(self):
        try:
            self.driver.switch_to.alert.accept()
        except NoAlertPresentException:
            return False

    def close_browser(self):
        self.driver.quit()

# Our Test
from selenium import webdriver

# Test Setup
browser = webdriver.Chrome()
test_value = 'it works'

# Test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
trng_page.type_into_input(test_value)
trng_page.click_button_1()
trng_page.close_alert()
text_from_input = trng_page.get_input_text()
assert text_from_input == test_value, f"Test Failed: Input didn't match expected ({test_value})."

print("Test Passed")
trng_page.close_browser()
