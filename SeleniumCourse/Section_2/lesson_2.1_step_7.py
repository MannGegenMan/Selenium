from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x_value):
    return str(math.log(abs(12*math.sin(int(x_value)))))

browser = webdriver.Chrome()


try:
    browser.get("https://suninjuly.github.io/get_attribute.html")

    x_element = browser.find_element(By.ID, "treasure")
    x_value = x_element.get_attribute("valuex")

    y = calc(x_value)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    robot_check = browser.find_element(By.ID, "robotCheckbox")
    robot_check.click()

    robots_rule = browser.find_element(By.ID, "robotsRule")
    robots_rule.click()

    submit_btn = browser.find_element(By.CLASS_NAME, "btn-default")
    submit_btn.click()

    time.sleep(10)

finally:
    browser.quit()
