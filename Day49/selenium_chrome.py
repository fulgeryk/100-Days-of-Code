from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.wait import WebDriverWait

ACCOUNT_EMAIL = "fulger@test.com"
ACCOUNT_PASSWORD = "Logitech123"
GYM_URL = "https://appbrewery.github.io/gym/"

class SeleniunConfigure:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        self.chrome_options.add_argument(f"--user-data-dir={self.user_data_dir}")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(GYM_URL)

    def login(self):
        wait = WebDriverWait(self.driver, timeout=5)
        logging_button = wait.until(lambda _: self.driver.find_element(By.ID, value = "login-button"))
        logging_button.click()
        email_input = wait.until(lambda _: self.driver.find_element(By.ID, value = "email-input"))
        email_input.send_keys(ACCOUNT_EMAIL)
        password_input = wait.until(lambda _: self.driver.find_element(By.ID, value = "password-input"))
        password_input.send_keys(ACCOUNT_PASSWORD)
        press_login = wait.until(lambda _: self.driver.find_element(By.ID, value="submit-button"))
        press_login.click()

