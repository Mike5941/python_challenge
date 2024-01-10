import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.use_chromium = True
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search?keywords=Python%20Engineer&location=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%20%EC%84%9C%EC%9A%B8%20%EC%84%9C%EC%9A%B8&geoId=104867736&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

login_element = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
login_element.click()

email_element = driver.find_element(By.ID, "username")
email_element.send_keys("enjoy5941@gmail.com")


password_element = driver.find_element(By.ID, "password")
password_element.click()
password_element.send_keys('dnjs202122')
password_element.send_keys(Keys.ENTER)


# Todo 1 - scroll elements

footer_element = driver.find_element(By.CLASS_NAME, 'artdeco-pagination__indicator--number button span')
webdriver.ActionChains(driver).scroll_to_element(footer_element).perform()

job_elements = driver.find_elements(By.CLASS_NAME, "ember-view .job-card-list__title")
for job in job_elements:
    print(job.text)




# driver.execute_script("arguments[0].scrollIntoView(true);", job_elements)

# job_elements[-1].send_keys(Keys.PAGE_DOWN)
# job_elements = driver.find_elements(By.CLASS_NAME, "ember-view a")
#
# wish_list = []
# for element in job_elements:

#     if "Backend" in element.text:
#         element.click()
#         save_element = driver.find_element(By.CLASS_NAME, "jobs-save-button")
#         save_element.click()
#         message_element = driver.find_element(By.ID, "ember129")
#         message_element.click()
#         for n in range(4):
#             job_details_element = driver.find_element(By.ID, "job-details")
#             job_details_element.send_keys(Keys.PAGE_DOWN)
#         time.sleep(1)
#         follow_element = driver.find_element(By.CLASS_NAME, "follow")
#         follow_element.click()