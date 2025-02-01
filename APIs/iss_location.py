import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = (response.json()["iss_position"]["latitude"], response.json()["iss_position"]["longitude"])
print(data)

# if response.status_code == 404:
#     raise Exception("That resources does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data")

# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code) # 200

# response = requests.get(url="http://api.open-notify.org/is-now.json") #invalid endpoint- changed iss to is
# print(response) # 404

"""
Status Codes
# 1XX: Hold On. Not finished yet
# 2XX: Here you go. You'll get your data
# 3XX: Go Away. You don't have permission
# 4XX: You Screwed up. Error from your end
# 5XX: I screwed up. Error from server side

More: https://www.webfx.com/web-development/glossary/http-status-codes/
"""