import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")

# Get locators

username_locator = driver.find_element(By.ID, "username")

password_locator = driver.find_element(By.NAME, "password")

submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
