from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org/")

event_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
dates = [date.text for date in event_dates]

event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul a")
names = [name.text for name in event_names]

events = {}
for n in range(len(event_dates)):
    events[n] = {
        "Date": dates[n],
        "Name": names[n],
    }

# Dict Comprehension
# events = {n: {"Date": dates[n], "Name": names[n]} for n in range(len(dates))}

print(events)

driver.close()