import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/wonsoong/Downloads/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#Get cookie to click on.
cookie = driver.find_element(By.ID, "cookie")

#Get upgrade item ids
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 1
five_min = time.time() + 60 * 5

while True:

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        #Get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()


        #Add another 5 seconds until the next check
        timeout = time.time() + 1

    #After 5minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break



























# buy_cursor = driver.find_element(By.ID, "buyCursor")
# store = driver.find_elements(By.CSS_SELECTOR, "#store div")[:-1]
#
#
# def count_sec(current_time):
#     global standard_time
#     if current_time == standard_time + COUNT_TIME:
#         standard_time = current_time
#         return True
#
#
# standard_time = floor(time.time())
#
# while True:
#     now = floor(time.time())
#     cookie.click()
#     if count_sec(now):
#         grayed = driver.find_element(By.CSS_SELECTOR, "div .grayed")
#         if grayed == 0:
#             pass
#         else:
#             not_available = store.index(grayed)
#             print(store)
#             print(grayed)
#             print(store[not_available - 1].text)
#             store[not_available - 1].click()


