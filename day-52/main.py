import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


DRVIVER_PATH = "/Users/wonsoong/Downloads/chromedriver"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.use_chromium = True
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(executable_path=DRVIVER_PATH, options=chrome_options)
        self.count = 1


    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        account_elements = self.driver.find_elements(By.CSS_SELECTOR, 'input')
        insta_id = account_elements[0]
        insta_pwd = account_elements[1]
        insta_id.send_keys("soong.e_food")
        insta_id.send_keys(Keys.TAB)
        insta_pwd.send_keys("tystus-gymwy4-kegqoQ")
        insta_pwd.send_keys(Keys.ENTER)

        time.sleep(3)
        later_element = self.driver.find_elements(By.CSS_SELECTOR, "button")
        later_element[1].click()
        time.sleep(3)
        later_element = self.driver.find_elements(By.CLASS_NAME, "_a9-z button")
        later_element[1].click()


    def find_follwers(self):
        time.sleep(2)
        search_icon = self.driver.find_elements(By.CLASS_NAME, "_ab6-")
        search_icon[2].click()
        time.sleep(2)
        search_bar = self.driver.find_element(By.TAG_NAME, "input")
        search_bar.click()
        search_bar.send_keys("mat_thagoras")
        time.sleep(2)
        account_element = self.driver.find_elements(By.CLASS_NAME, "_aacw")
        account_element[1].click()
        time.sleep(2)
        follower_elements = self.driver.find_elements(By.CLASS_NAME, "_ac2a")
        follower_elements[1].click()


    def follow(self):
        while True:
            time.sleep(2)
            all_followers = self.driver.find_elements(By.CLASS_NAME, "_aad6")[30:]
            while True:
                time.sleep(1)
                all_followers[self.count].click()
                webdriver.ActionChains(self.driver).scroll_to_element(element=all_followers[self.count])
                self.count += 1
                all_followers = self.driver.find_elements(By.CLASS_NAME, "_aad6")[30:]


insta = InstaFollower()

insta.login()
insta.find_follwers()
insta.follow()

