from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time

link = "https://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    fake = Faker()
    fake_name = fake.name()
    fake_city = fake.city()
    fake_country = fake.country()

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys(fake_name)

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys(fake_name)

    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys(fake_city)

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys(fake_country)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
