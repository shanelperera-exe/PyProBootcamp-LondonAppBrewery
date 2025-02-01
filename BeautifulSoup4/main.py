from bs4 import BeautifulSoup

with open("website.html", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)    # The first item in a   ex: li or p

# Find all
# all_anchor_tags = soup.find_all(name="a")

# Get the text in anchor tags
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

headings = soup.select(".heading")
print(headings)
