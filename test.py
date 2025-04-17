from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")

num1_input = driver.find_element(By.ID, "num1")
num2_input = driver.find_element(By.ID, "num2")
add_button = driver.find_element(By.TAG_NAME, "button")

num1_input.send_keys("12")
num2_input.send_keys("44")
add_button.click()

time.sleep(3)
    
driver.quit()
