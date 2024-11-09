from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from faker import Faker
import time

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.faker = Faker()

    def fill_registration_form(self, link):
        self.browser.get(link)

        fake_first_name = self.faker.first_name()
        fake_last_name = self.faker.last_name()
        fake_email = self.faker.email()

        input_first_name = self.browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        input_first_name.send_keys(fake_first_name)

        input_last_name = self.browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group input.second")
        input_last_name.send_keys(fake_last_name)

        input_email = self.browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.third_class input.form-control.third")
        input_email.send_keys(fake_email)

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(10)

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        
        return welcome_text
    
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.fill_registration_form(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration failed")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.fill_registration_form(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration failed")

    def tearDown(self):
        self.browser.quit()

if __name__=="__main__":
    unittest.main()