from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
from beautifulsoup_scraping import SiteSrape

EDIT_LINK_FORM = "https://docs.google.com/forms/d/1r2gZLNpbdcgwt4wdk5R7DLyDBkrvLlDGPqoZM6t0biE/edit"
URL_TO_FORM = "https://forms.gle/VmT5yTKtuRhKbbUYA"

class FormManipulate:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("user-data-dir=C:\\Users\\Fulger\\AppData\\Local\\Google\\Chrome\\User Data")
        self.chrome_options.add_argument("profile-directory=Profile 1")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.site = SiteSrape()

    def fill_form(self):
        self.driver.get(URL_TO_FORM)
        self.site.find_requests()
        wait = WebDriverWait(self.driver, timeout=20)
        for i,t in enumerate(self.site.list_prices):
            all_divs = wait.until(lambda _: self.driver.find_elements(By.CSS_SELECTOR, value="div.Qr7Oae"))
            for div in all_divs:
                write_here = div.find_element(By.XPATH, value=".//input[contains(@type, 'text')]")
                if div.find_elements(By.XPATH, value=".//span[contains(text(), 'address of proprety')]"):
                    write_here.click()
                    write_here.send_keys(self.site.list_of_address[i])
                if div.find_elements(By.XPATH, value=".//span[contains(text(), 'price per month')]"):
                    write_here.click()
                    write_here.send_keys(self.site.list_prices[i])
                if div.find_elements(By.XPATH, value=".//span[contains(text(), 'link to the proprery')]"):
                    write_here.click()
                    write_here.send_keys(self.site.list_of_links[i])
            send = wait.until(lambda _: self.driver.find_element(By.XPATH, value="//span[contains(text(), 'Trimite')]"))
            send.click()
            send_another_answear = wait.until(lambda _: self.driver.find_element(By.XPATH, value="//a[contains(text(), 'Trimite alt')]"))
            send_another_answear.click()
            time.sleep(2)
        self.driver.quit()

    def save_answears(self):
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(EDIT_LINK_FORM)
        wait = WebDriverWait(self.driver, timeout=20)
        check_answears = wait.until(lambda _: self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Răspunsuri')]"))
        check_answears.click()
        connect = wait.until(lambda _: self.driver.find_element(By.XPATH, value="//span[contains(text(), 'Foi de calcul')]"))
        connect.click()
        create_form = wait.until(lambda _: self.driver.find_element(By.XPATH, value="//input[contains(@type, 'text')]"))
        create_form.click()
        create_form.send_keys(Keys.CONTROL + "a")
        create_form.send_keys(Keys.DELETE)
        create_form.send_keys("SF Renting Research")
        press_create = wait.until(lambda _: self.driver.find_element(By.XPATH, value="//span[contains(@class, 'Creează')]"))
        press_create.click()


