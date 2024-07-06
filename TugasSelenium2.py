from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


driver = webdriver.Chrome()


driver.get("https://demoqa.com/alerts")


def handle_alert():
    alert = Alert(driver)
    print(f"Alert text: {alert.text}")
    alert.accept()


button1 = driver.find_element(By.ID, "alertButton")
button1.click()
time.sleep(2)  
handle_alert()


button2 = driver.find_element(By.ID, "timerAlertButton")
button2.click()
time.sleep(6) 
handle_alert()


button3 = driver.find_element(By.ID, "confirmButton")
button3.click()
time.sleep(2) 
handle_alert()


button4 = driver.find_element(By.ID, "promtButton")
button4.click()
time.sleep(2)
alert = Alert(driver)
alert.send_keys("Test input")
alert.accept()


driver.quit()