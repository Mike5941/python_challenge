from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/mac/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.appbrewery.co/p/newsletter")

email_blank = driver.find_element(By.NAME, "email")
email_blank.send_keys("mike9159@naver.com")
email_blank.send_keys(Keys.ENTER)