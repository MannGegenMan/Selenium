from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.NAME, "e-mail")
    input3.send_keys("example@gmail.com")

    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"][maxlength="32"]')
    for element in elements:
        element.send_keys("text")

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()