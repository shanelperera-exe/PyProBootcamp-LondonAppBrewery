import requests
import datetime as dt
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "http://api.marketstack.com/v1/eod"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "963bf20d1776e88e0f3d417ef15c8c1e"
NEWS_API_KEY = "32f9de607d284e50a7f80736894388f3"

ACCOUNT_SID = "ACbbef7f076edb70b892fe25e14ee4ec6a"
AUTH_TOKEN = "66ee41c587467a74c42e957f539b2cd7"

def main():
    yesterday, seven_days_ago = get_dates()
    stock_data = get_stock_data(yesterday, seven_days_ago)
    value_diff_percentage, up_down = calc_value_diff_percentage(stock_data)

    if abs(value_diff_percentage) > 5:
        articles = get_news()
        send_news(articles, value_diff_percentage, up_down)

def get_dates():
    yesterday = dt.date.today() - dt.timedelta(days=1)
    seven_days_ago = yesterday - dt.timedelta(days=7)
    return yesterday, seven_days_ago

def get_stock_data(yesterday, seven_days_ago):
    stock_params = {
        "access_key": STOCK_API_KEY,
        "symbols": STOCK_NAME,
        "date_from": seven_days_ago,
        "date_to": yesterday
    }

    stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
    stock_response.raise_for_status()
    stock_data = stock_response.json()["data"]
    return stock_data

def calc_value_diff_percentage(stock_data):
    yesterday_close = float(stock_data[0]["close"])
    day_before_yesterday_close = float(stock_data[1]["close"])

    value_diff = yesterday_close - day_before_yesterday_close
    if value_diff > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    value_diff_percentage = round((value_diff / yesterday_close) * 100)
    return value_diff_percentage, up_down

def get_news():
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    latest_articles = news_data[:3]
    return latest_articles

def send_news(articles, value_diff_percentage, up_down):
    article_list = [f"{STOCK_NAME}: {up_down}{value_diff_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in articles]
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in article_list:
        message = client.messages.create(
            body=article,
            from_="+1 775 458 9306",
            to="+94 77 637 9650"
        )
        print(message.status)


#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

if __name__ == "__main__":
    main()
