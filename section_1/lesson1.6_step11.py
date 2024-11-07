from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fake = Faker()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_email = fake.email()

    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
    input_first_name.send_keys(fake_first_name)

    input_last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group input.second")
    input_last_name.send_keys(fake_last_name)

    input_email = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.third_class input.form-control.third")
    input_email.send_keys(fake_email)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()