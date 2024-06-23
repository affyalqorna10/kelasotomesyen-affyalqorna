from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.minimize_window()

urls = [
    'https://tiket.com',
    'https://tokopedia.com',
    'https://orangsiber.com',
    'https://demoqa.com',
    'https://automatetheboringstuff.com'
]

for url in urls:
    driver.get(url)
    print(f"{url} - {driver.title}")

time.sleep(5)

driver.quit()