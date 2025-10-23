from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

#Hard way

# first_date = f"2025-{driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time').text}"
# first_name = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a').text
#
# second_date = f"2025-{driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time').text}"
# second_name = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/a').text
#
# third_date = f"2025-{driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]/time').text}"
# third_name = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]/a').text
#
# fourth_date = f"2025-{driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[4]/time').text}"
# fourth_name = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[4]/a').text
#
# five_date = f"2025-{driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]/time').text}"
# five_name = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]/a').text

# calendar = {
#     "0" : {
#         "date" : first_date,
#         "name" : first_name
#     },
#     "1" : {
#         "date" : second_date,
#         "name" : second_name
#     },
#     "2": {
#         "date": third_date,
#         "name": third_name
#     },
#     "3": {
#         "date": fourth_date,
#         "name": fourth_name
#     },
#     "4": {
#         "date": five_date,
#         "name": five_name
#     },
# }

#Easy way

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")

calendar = {}
for i in range(5):
    date = events[i].find_element(By.TAG_NAME, "time").text
    name = events[i].find_element(By.TAG_NAME, "a").text
    calendar[i] = {"date": f"2025-{date}", "name": name}


print(calendar)
driver.quit()