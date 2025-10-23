from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number_of_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
number_of_articles.click()

all_portals = driver.find_element(By.LINK_TEXT, value = "Gibraltar Mountain")
# all_portals.click()
icon_search = driver.find_element(By.XPATH, value ='//*[@id="p-search"]/a/span[1]')
icon_search.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)
driver.quit()