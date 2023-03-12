from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present

from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
url = 'https://techstepacademy.com/training-ground'
browser.get(url)
print("I have arrived")

# Wait Until
WebDriverWait(browser, 10).until(alert_is_present())
print("An alert appeared")

# Alert
alert = Alert(browser)
print(alert.text)
alert.accept()

# Select
sel = browser.find_element(By.ID, "sel1")
my_select = Select(sel)
my_select_options = [elem.text for elem in my_select.options]
my_select.select_by_visible_text('Battlestar Galactica')
my_select.select_by_index(0)
my_select.select_by_value('second')
print(my_select.first_selected_option.text)
