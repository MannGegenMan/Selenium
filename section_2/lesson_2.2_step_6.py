from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"

def calc(x):
    return math.log(abs(12*math.sin(int(x))))

try:
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    robot_check = browser.find_element(By.ID, "robotCheckbox")
    robot_check.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_radio.click()

    button.click()

    time.sleep(10)

finally:
    browser.quit()