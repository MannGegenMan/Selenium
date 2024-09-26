from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get("https://suninjuly.github.io/math.html")

    x_element = browser.find_element(By.ID, "input_value")

    x = x_element.text

    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    submit_button = browser.find_element(By.CLASS_NAME, "btn-default")
    submit_button.click()


    time.sleep(10)

finally:
    browser.quit()