from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://techstepacademy.com/trial-of-the-stones'

browser.get(url)

# Riddle of Stone
stone_input = browser.find_element(By.ID, "r1Input")
stone_answer_button = browser.find_element(By.CSS_SELECTOR, "button[id='r1Btn']")
stone_input.send_keys('Rock')
stone_answer_button.click()
# div[@id='passwordBanner'] is the same as div#passwordBanner
stone_answer = (browser.find_element(By.CSS_SELECTOR, "div#passwordBanner > h4")).text
print(stone_answer)

# Riddle of Secrets
secrets_input = browser.find_element(By.XPATH, "//input[@id='r2Input']")
secrets_answer_button = browser.find_element(By.XPATH, "//button[@id='r2Butn']")
secrets_input.send_keys(stone_answer)
secrets_answer_button.click()
secrets_answer = browser.find_element(By.XPATH, "//div[@id='successBanner1']/h4").text
print(secrets_answer)

assert secrets_answer == "Success!"

# Two Merchants
value1 = browser.find_element(By.XPATH, "//input[@id='r1Input']/../div[3]/p")
name1 = browser.find_element(By.XPATH, "//input[@id='r1Input']/../div[3]/span")
print("First merchant:", name1.text, ",", value1.text)

value2 = browser.find_element(By.XPATH, "//input[@id='r1Input']/../div[4]/p")
name2 = browser.find_element(By.XPATH, "//input[@id='r1Input']/../div[4]/span/b")
print("Second merchant:", name2.text, ",", value2.text)

if int(value1.text) > int(value2.text):
    richest_merchant = name1.text
else:
    richest_merchant = name2.text

richest_merchant_input = browser.find_element(By.ID, "r3Input")
richest_merchant_answer_button = browser.find_element(By.ID, "r3Butn")
richest_merchant_input.send_keys(richest_merchant)
richest_merchant_answer_button.click()

richest_merchant_answer = browser.find_element(By.XPATH, "//div[@id='successBanner2']/h4")
assert richest_merchant_answer.text == "Success!"

check_answers_button = browser.find_element(By.ID, "checkButn")
check_answers_button.click()
final_answer = browser.find_element(By.XPATH, "//div[@id='trialCompleteBanner']/h4")
assert final_answer.text == "Trial Complete"
print(final_answer.text)