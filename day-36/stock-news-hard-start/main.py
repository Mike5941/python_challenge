import requests
import os
import itertools
from twilio.rest import Client



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yesterday's closing stock price.

STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": "CEK4PHJZFRPF4FNG"
}


stock_res = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMETERS)
stock_res.raise_for_status()
stock_data = stock_res.json()["Time Series (Daily)"]

# last_two_days_info = list(itertools.islice(stock_data['Time Series (Daily)'].items(), 0, 2))


stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator

if abs(diff_percent) > 5:
    NEWS_PARAMETERS = {
        "qInTitle": COMPANY_NAME,
        "apiKey": "f8fa46f03325495f862130a9a0806efc",
    }

    news_res = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    news_res.raise_for_status()
    articles = news_res.json()["articles"]
    three_articles = articles[:3]


    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}% \nHeadline: {article['title']}.'"
                          f" \nBrief: {article['description']}" for article in three_articles]

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.
    TWILIO_SID = "ACefd86674a6dfcda85e0080f6576674cb"
    TWILIO_TOKEN = "40f93e2540f3a090b0554f8bd727697a"

    client = Client(TWILIO_SID, TWILIO_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            to="+821074439500",
            from_="+13609269052",
            body=article,
        )
