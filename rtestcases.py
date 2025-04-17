from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000")

test_cases = [
    "hjb",
    "jhvj",
    "",
    "gjbjb"
]

for test in test_cases:
    driver.find_element(By.NAME, "username").send_keys(test)
    time.sleep(2)
    driver.find_element(By.TAG_NAME, "button").click()
    
driver.quit()
