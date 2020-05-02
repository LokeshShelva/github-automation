import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


for x in sys.argv:
    arg = x

# WEB SCRAPING
PATH = 'C:\Program Files (x86)\chromedriver'

driver = webdriver.Chrome(executable_path= PATH)

driver.get('http://www.github.com/login')

try:
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_field"))
    )
    username.send_keys('###Enter your github email here###')

    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password.send_keys('###Enter your github password here###')
    password.send_keys(Keys.RETURN)

    driver.get('https://github.com/new')

    repo_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "repository_name"))
    )
    repo_name.send_keys(str(arg))

    time.sleep(3)

    readMe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "repository_auto_init"))
    )
    readMe.click()

    repo_name.send_keys(Keys.RETURN)
    time.sleep(5)
    url = driver.current_url
# END OF WEB SCRAPING

    repo = 'git clone ' + str(url) +'.git'
    print(repo)
    os.popen(repo)
    os.popen('code .')

except:
    driver.quit()
