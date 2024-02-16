# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

import sys
import json
import ast

inputt = ast.literal_eval(sys.argv[0])
print(inputt)

# # Configuring Chrome options to detach the browser window
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# # options.add_argument("--headless")

# # Target URL for Instagram login page
# url = "https://www.instagram.com/accounts/login/"

# # Creating a Chrome webdriver instance with the configured options
# browser = webdriver.Chrome(options=options)
# browser.get(url)
# browser.minimize_window()


# # Waiting for the 'Cookies' button to be clickable and then clicking it
# WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]'))).click()

# # Pausing execution to allow time for the Instagram login page to load
# time.sleep(4)

# file = ""

# # To store username and password 
# username = "somethingidk8225"
# password = "1234567Katya"

# # Locating the username and password input fields
# browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(username)
# browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(password)
# # Clicking the 'Log In' button to submit the credentials
# browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button").click()

# browser.maximize_window()

# Cookies, echazar opcionales
# /html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]

# Username
# /html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input

# Password
# /html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input

# Log in
# /html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button

# time.sleep(100000)
# browser.close()