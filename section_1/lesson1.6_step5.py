import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_link_text"
result = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_int = browser.find_element(By.LINK_TEXT, result)
    find_int.click()

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.NAME, "firstname")
    input3.send_keys("Smolensk")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

