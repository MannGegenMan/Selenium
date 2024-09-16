from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


browser = webdriver.Chrome()

try:
    browser.get("https://suninjuly.github.io/selects1.html")

    num_element_1 = browser.find_element(By.ID, "num1")
    num_element_2 = browser.find_element(By.ID, "num2")
    num_1 = int(num_element_1.text)
    num_2 = int(num_element_2.text)
    sum_numbers = num_1 + num_2

    select_num = Select(browser.find_element(By.TAG_NAME, "select"))
    select_num.select_by_value(str(sum_numbers))

    submit_btn = browser.find_element(By.CLASS_NAME, "btn-default")
    submit_btn.click()

    time.sleep(10)

finally:
    browser.quit()