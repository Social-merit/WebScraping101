
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def initialize_webdriver(path, web):
    driver = webdriver.Chrome(path)
    driver.get(web)
    driver.maximize_window()
    return driver

def fill_field(driver, xpath, value):
    field = driver.find_element(By.XPATH, xpath)
    field.send_keys(value)

def click_button(driver, xpath):
    button = driver.find_element(By.XPATH, xpath)
    button.click()

def main():
    web = "https://twitter.com/i/flow/login"
    path = "/Users/frankandrade/Downloads/chromedriver"
    driver = initialize_webdriver(path, web)

    # Let the page load the content
    time.sleep(6)

    # Fill in the username and click "Next"
    fill_field(driver, '//input[@autocomplete="username"]', "my_username")
    click_button(driver, '//div[@role="button"]//span[text()="Next"]')

    # Wait a bit for the next page to load
    time.sleep(2)

    # Fill in the password and click "Log in"
    fill_field(driver, '//input[@autocomplete="current-password"]', "my_password")
    click_button(driver, '//div[@role="button"]//span[text()="Log in"]')

    # Add any post-login actions here (if needed)

    # Close the driver when done
    # Uncomment the next line to close the driver after execution
    # driver.quit()

if __name__ == "__main__":
    main()



"""
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def read_login_info(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def initialize_webdriver(path, web):
    driver = webdriver.Chrome(path)
    driver.get(web)
    driver.maximize_window()
    return driver

def fill_field(driver, xpath, value):
    field = driver.find_element(By.XPATH, xpath)
    field.send_keys(value)

def click_button(driver, xpath):
    button = driver.find_element(By.XPATH, xpath)
    button.click()

def main():
    login_info = read_login_info('login_info.json')
    web = "https://twitter.com/i/flow/login"
    path = "/Users/frankandrade/Downloads/chromedriver"
    
    driver = initialize_webdriver(path, web)

    # Let the page load the content
    time.sleep(6)

    # Fill in the username and click "Next"
    fill_field(driver, '//input[@autocomplete="username"]', login_info['username'])
    click_button(driver, '//div[@role="button"]//span[text()="Next"]')

    # Wait a bit for the next page to load
    time.sleep(2)

    # Fill in the password and click "Log in"
    fill_field(driver, '//input[@autocomplete="current-password"]', login_info['password'])
    click_button(driver, '//div[@role="button"]//span[text()="Log in"]')

    # Add any post-login actions here (if needed)

    # Close the driver when done
    # Uncomment the next line to close the driver after execution
    # driver.quit()

if __name__ == "__main__":
    main()

"""