from selenium import webdriver

from pages.training_ground_page import TrainingGroundPage

# Test Setup
browser = webdriver.Chrome()
test_value = 'it works'

# Test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == "Button1"
trng_page.button1.click()
trng_page.close_alert()

print("Test Passed")
browser.quit()