import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC

DRVIVER_PATH = "/Users/wonsoong/Downloads/chromedriver"
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_ID = "mike6417@naver.com"
TWITTER_PASSWORD = "!dnjs202122"

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.use_chromium = True
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(executable_path=DRVIVER_PATH, options=chrome_options)
        self.down_speed = 0
        self.upload_speed = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_btn = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_btn.click()
        WebDriverWait(self.driver, 190).until(EC.url_changes("https://www.speedtest.net/"))
        self.down_speed = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.upload_speed = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)


    def tweet_at_provider(self):
        if self.down_speed < 1000:
            self.driver.get("https://twitter.com/")
            time.sleep(2)
            login = self.driver.find_element(By.LINK_TEXT, '로그인')
            login.click()
            time.sleep(2)
            email = self.driver.find_element(By.TAG_NAME, 'input')
            email.send_keys(TWITTER_ID)
            email.send_keys(Keys.ENTER)
            time.sleep(2)
            twitter_id = self.driver.find_element(By.TAG_NAME, 'input')
            twitter_id.send_keys("one_1sy")
            twitter_id.send_keys(Keys.ENTER)
            time.sleep(2)
            password = self.driver.find_element(By.NAME, 'password')
            password.send_keys("Ddnjs202122")
            password.send_keys(Keys.ENTER)
            time.sleep(2)
            tweet_element = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
            tweet_element.send_keys(f"Hey Internet Provider, why is my internet speed "
                                    f"{self.down_speed}down/{self.upload_speed}up when I pay for 150down/10up?")
            tweet_element.send_keys(Keys.ENTER)
            time.sleep(2)
            tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
            tweet_btn.click()


speed_test = InternetSpeedTwitterBot()

speed_test.get_internet_speed()
speed_test.tweet_at_provider()
