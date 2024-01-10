from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/mac/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Soong")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Won")

email = driver.find_element(By.NAME, "email")
email.send_keys("meis@naver.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()





