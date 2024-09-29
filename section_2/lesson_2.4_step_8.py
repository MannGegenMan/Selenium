from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/explicit_wait2.html"

def calc(x_element):
    return math.log(abs(12*math.sin(x_element)))


try:
    browser.get(link)

    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book_btn = browser.find_element(By.ID, "book")
    book_btn.click()

    x_element = browser.find_element(By.ID, "input_value")
    x_value = int(x_element.text)
    y_element = calc(x_value)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y_element)

    submit_btn = browser.find_element(By.ID, "solve")
    submit_btn.click()

    time.sleep(10)

finally:
    browser.quit()
