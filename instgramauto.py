from selenium import webdriver
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait

# from selenium.webdriver.common.action_chains import ActionChains
# from random import randint
# import time
# import random
# from selenium.common.exceptions import NoSuchElementException
option = webdriver.ChromeOptions()
option.add_argument(f'user-agent={user_agent}')
browser = webdriver.Chrome (chrome_options=option)




browser.get("https://www.instagram.com/accounts/login/?hl=en")
print("Loading Instagram Login Page..")
browser.implicitly_wait(10)
username=browser.find_element(By.XPATH,'//input[@name="username"]')
username.send_keys("malludrummer")
password=browser.find_element(By.XPATH,'//input[contains(@name,"passwo")]')
password.send_keys("Olassaaass")
loginbutton=browser.find_element(By.XPATH,'//button[@type="submit"]')
password.send_keys(Keys.RETURN)

