from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/file_input.html"


try:
    browser.get(link)

    first_name_text = "Maxim"
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys(first_name_text)

    last_name_text = "Maximov"
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys(last_name_text)

    email_text = "maxim@mail.ru"
    email = browser.find_element(By.NAME, "email")
    email.send_keys(email_text)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "lesson_2.2_step_8.txt")

    upload_file_btn = browser.find_element(By.ID, "file")
    upload_file_btn.send_keys(file_path)

    submit_btn = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_btn.click()

    time.sleep(10)

finally:
    browser.quit()
