from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
load_dotenv()
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PROMISED_DOWN = 500
PROMISED_UP = 15
TWITTER_EMAIL = os.environ.get("X_EMAIL")
TWITTER_PASSWORD = os.environ.get("X_PASSWORD")
SPEED_URL = "https://www.speedtest.net/"
X_URL = "https://x.com/"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(SPEED_URL)
        self.down = 0
        self.up = 0

    def accept_cookies(self):
        wait = WebDriverWait(self.driver, timeout=5)
        try:
            accept_btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            accept_btn.click()
            print("✅ Accept.")
        except "TimeoutException":
            print("⚠️ No popup detected.")

    def start_internet_speed(self):
        wait = WebDriverWait(self.driver, timeout=80)
        try:
            go = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]')))
            go.click()
            close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[8]/div/div/div[2]/a')))
            close_btn.click()
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.result-data-large.download-speed")))
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.result-data-large.upload-speed")))
            self.down = float(self.driver.find_element(By.CSS_SELECTOR, value = "span.result-data-large.download-speed").text)
            self.up = float(self.driver.find_element(By.CSS_SELECTOR, value = "span.result-data-large.upload-speed").text)
            self.driver.quit()
            print(self.down)
            print(self.up)
            print("✅ All good.")
        except "TimeoutException":
            print("⚠️ Item doesn't exist")

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.driver = webdriver.Chrome(options=self.chrome_options)
            self.driver.get(X_URL)
            wait = WebDriverWait(self.driver, timeout=80)
            try:
                accept_cookies = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/button[1]/div/span/span')))
                accept_cookies.click()
                sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a/div/span/span')))
                sign_in.click()
                email_input = wait.until(lambda _: self.driver.find_element(By.NAME, value='text'))
                email_input.send_keys(TWITTER_EMAIL)
                next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')))
                next_button.click()
                password_input = wait.until(lambda _: self.driver.find_element(By.NAME, value='password'))
                password_input.send_keys(TWITTER_PASSWORD)
                tweet = wait.until(lambda _: self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div'))
                tweet.click()
                tweet.send_keys(f"Hey internet provider my download speed is {self.down}, and you promise {PROMISED_DOWN}")
                post_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')))
                post_button.click()
            except "TimeoutException":
                print("⚠️ Item doesn't exist")
