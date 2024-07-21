from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_invalid_login():
    sauce_options = {
        'username': 'YOUR_SAUCE_USERNAME',
        'accessKey': 'YOUR_SAUCE_ACCESS_KEY',
        'name': 'Invalid Login Test',
        'browserName': 'chrome',
        'platformName': 'Windows 10',
        'browserVersion': 'latest'
    }

    driver = webdriver.Remote(
        command_executor='https://ondemand.saucelabs.com/wd/hub',
        desired_capabilities=sauce_options
    )

    try:
        driver.get('https://example.com/login')


        username_field = driver.find_element(By.ID, 'username')
        password_field = driver.find_element(By.ID, 'password')
        username_field.send_keys('invalid_user')
        password_field.send_keys('invalid_password')
        password_field.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'error-message'))
        )

        error_message = driver.find_element(By.ID, 'error-message').text
        assert 'Invalid username or password' in error_message

    finally:
        driver.quit()