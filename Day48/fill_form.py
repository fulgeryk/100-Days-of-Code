from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Daria")
second_name = driver.find_element(By.NAME, value="lName")
second_name.send_keys("Maria")
email = driver.find_element(By.NAME, value="email")
email.send_keys("dariamaria@yahoo.com", Keys.ENTER)