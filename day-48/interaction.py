from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/mac/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
wait = WebDriverWait(driver, 5)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, "Homo antecessor")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()
