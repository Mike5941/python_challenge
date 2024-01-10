from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/mac/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price_data = driver.find_element(By.CLASS_NAME, "searchInput_search_input__vLBeq")
# time_data = driver.find_elements(By.CLASS_NAME, "menu li time")
# title_data = driver.find_elements(By.CLASS_NAME, "shrubbery ul li a")
#
#
# time_list = [time.text for time in time_data]
# time_table = time_list[5:]
#
# title_list = [title.text for title in title_data]
# title_list = title_list[5:10]

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for x in range(len(event_times)):
    events[x] = {
        'time': event_times[x].text,
        'title': event_names[x].text,
    }
print(events)
driver.quit()