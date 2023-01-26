from selenium import webdriver

# helps with recording, not required
opts = webdriver.ChromeOptions()
opts.add_argument('--disable-gpu')

url1 = "https://techstepacademy.com/trial-of-the-stones"
url2 = "https://techstepacademy.com/training-ground"
url3 = "https://google.com"
url4 = "https://amazon.com"
url5 = "https://ebay.com"

browser1 = webdriver.Chrome(options=opts)

# Open multiple tabs
browser1.get("https://techstepacademy.com/training-ground")
browser1.execute_script('window.open("https://google.com", "_blank");')
browser1.execute_script('window.open("https://amazon.com", "_blank");')
browser1.execute_script('window.open("https://ebay.com", "_blank");')

# define how many tabs are opened
handels = browser1.window_handles

# switch between opened tabs

browser1.switch_to.window(handels[1])
print(browser1.title)
browser1.switch_to.window(handels[2])
print(browser1.title)
browser1.switch_to.window(handels[3])
print(browser1.title)

print("Test Passed")
browser1.quit()