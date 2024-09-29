from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x_element):
    return math.log(abs(12*math.sin(x_element)))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/redirect_accept.html"


try:
    browser.get(link)

    troll_face_btn = browser.find_element(By.CLASS_NAME, "btn-primary")
    troll_face_btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x_value = int(x_element.text)
    y_element = calc(x_value)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y_element)

    submit_btn = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_btn.click()

    time.sleep(10)

finally:
    browser.quit()
