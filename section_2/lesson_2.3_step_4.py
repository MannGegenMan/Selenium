from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x_value):
   return math.log(abs(12*math.sin(x_value)))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/alert_accept.html"


try:
    browser.get(link)

    magical_journey_btn = browser.find_element(By.CLASS_NAME, "btn-primary")
    magical_journey_btn.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x_value = int(x_element.text)
    y_element = calc(x_value)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(str(y_element))

    submit_btn = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_btn.click()

    time.sleep(10)

finally:
    browser.quit()