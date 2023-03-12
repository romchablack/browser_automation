from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url = "https://techstepacademy.com/iframe-training"

browser.get(url)

# define iFrame
iframe = browser.find_element(By.CSS_SELECTOR, 'iframe')

# switch to iFrame
browser.switch_to.frame(iframe)

# find text in iFrame
frame_text = browser.find_element(By.CSS_SELECTOR, "div#block-ec928cee802cf918d26c")
print(frame_text.text)

# quit iFrame and switch to Default Content on the page
browser.switch_to.default_content()

# find text on the main page
page_text = browser.find_element(By.CSS_SELECTOR, "div#block-5d3de848045889000188d389")

print("Test Passed")
browser.quit()
