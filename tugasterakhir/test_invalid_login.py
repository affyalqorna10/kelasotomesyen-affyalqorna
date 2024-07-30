from selenium import webdriver
from tugasterakhir.login_page import LoginPage

def test_invalid_login():
    sauce_options = {
        'username': 'YSAUCE_USERNAME',
        'accessKey': 'SAUCE_ACCESS_KEY',
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
        login_page = LoginPage(driver)
        login_page.open('https://example.com/login')
        login_page.login('invalid_user', 'invalid_password')

        error_message = login_page.get_error_message()
        assert 'Invalid username or password' in error_message

    finally:
        driver.quit()