from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from faker import Faker
import time

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture
def faker():
    return Faker()

class TestRegistration:
    def fill_registration_form(self, browser, faker, link):
        browser.get(link)

        fake_first_name = faker.first_name()
        fake_last_name = faker.last_name()
        fake_email = faker.email()

        input_first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        input_first_name.send_keys(fake_first_name)

        input_last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group input.second")
        input_last_name.send_keys(fake_last_name)

        input_email = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.third_class input.form-control.third")
        input_email.send_keys(fake_email)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(10)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        
        return welcome_text
    
    def test_registration1(self, browser, faker):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.fill_registration_form(browser, faker, link)
        assert welcome_text == "Congratulations! You have successfully registered!"

    def test_registration2(self, browser, faker):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.fill_registration_form(browser, faker, link)
        assert welcome_text == "Congratulations! You have successfully registered!"

    def tearDown(self):
        self.browser.quit()

if __name__=="__main__":
    pytest.main()