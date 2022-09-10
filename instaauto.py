from selenium import webdriver
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_argument(f'user-agent={user_agent}')
browser = webdriver.Chrome (chrome_options=option)





browser.get("https://www.wikipedia.org/")
browser.implicitly_wait(10)
