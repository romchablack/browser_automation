from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/training-ground')

# CSS_SELECTOR: $$("input[id='ipt1']")
input1Path = "input[id='ipt1']"
input1Element = browser.find_element(By.CSS_SELECTOR, input1Path)
input1Element.send_keys('Number 1')

# XPATH: $x("//input[@id='ipt1']")
input2Path = "//input[@id='ipt1']"
input2Element = browser.find_element(By.XPATH, input2Path)