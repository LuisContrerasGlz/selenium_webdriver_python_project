import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")

# Get locators

# User name field
username_locator = driver.find_element(By.ID, "username")

# Password field
password_locator = driver.find_element(By.NAME, "password")

# Submit button

submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")

# Text from page after login
text_locator = driver.find_element(By.TAG_NAME, "h1")

# Button for log out
log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")