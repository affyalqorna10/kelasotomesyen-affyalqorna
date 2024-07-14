from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(3)
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys("Admin")
    password_input.send_keys("admin123")

 
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    time.sleep(5)

    try:
        dashboard_element = driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
        print("Login berhasil!")
    except:
        print("Login gagal!")

finally:
    driver.quit()