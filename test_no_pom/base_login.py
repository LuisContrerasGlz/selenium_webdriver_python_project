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


# Steps for Loign

username_locator.send_keys("student")

password_locator.send_keys("Password123")

submit_button_locator.click()

# new page URL 

actual_url = driver.current_url

# Text from page after login
text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text

# Button for log out
log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")