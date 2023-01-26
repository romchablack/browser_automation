from selenium import webdriver

from pages.training_ground_page import TrainingGroundPage
from pages.trial_page import TrialPage

broswer = webdriver.Chrome()

test_value = 'Test passed.'

# Trial Page
trl_page = TrialPage(driver=broswer)
trl_page.go()
trl_page.stone_input.input_text("rock")
trl_page.stone_button.click()

# Training Grounds
trng_page = TrainingGroundPage(driver=broswer)
trng_page.go()
assert trng_page.button1.text == 'Button1', "Unexpected button name"
print('Test passed')

broswer.quit()