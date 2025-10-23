from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(2)
language_select = driver.find_element(By.ID, value="langSelect-EN")
language_select.click()

game_over = False
time.sleep(2)
button_cookie = driver.find_element(By.ID, value="bigCookie")
button_cookie.click()

check_time = time.time() + 5
start_time = time.time()

first_button = driver.find_element(By.XPATH, value ='//*[@id="product0"]')
second_button = driver.find_element(By.XPATH, value ='//*[@id="product1"]')
third_button = driver.find_element(By.XPATH, value ='//*[@id="product2"]')
while time.time() < start_time + 300:
    button_cookie.click()
    if time.time() > check_time:
        check_time = time.time() + 5
        number_of_cookies = driver.find_element(By.ID, value ='cookies').text
        cookies_line = number_of_cookies.split("\n")[0]
        cookies_number = int(cookies_line.split(" ")[0].replace(",", ""))
        first_price = driver.find_element(By.XPATH, value ='//*[@id="productPrice0"]').text
        price_first = int(first_price.replace(",", "")) if first_price else 0
        second_price = driver.find_element(By.XPATH, value='//*[@id="productPrice1"]').text
        price_second = int(second_price.replace(",", "")) if second_price else 0
        third_price = driver.find_element(By.XPATH, value='//*[@id="productPrice2"]').text
        price_third = int(third_price.replace(",", "")) if third_price else 0
        if cookies_number >= price_third:
            third_button.click()
        elif cookies_number >= price_second:
            second_button.click()
        else:
            first_button.click()





