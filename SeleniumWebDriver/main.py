from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/PlayStation-5-Console-CFI-1215A01X/dp/B0BCNKKZ91/ref=sr_1_3?crid=EG2EHJ18BKT0&dib=eyJ2IjoiMSJ9.adTLSjc5UBO6lTJiDvl_IXU5Hx02Z_CWzlhx9M2nGkQIQcghMbB9-dfhdFaUSViy5rgEWvxbZTcf8nCJnstwLGkV3xxyckNC0-Af5SMRLfY8w-Vetl_C902GoF_8OtXelRgJTwg8aYKsGBeflgnGregHOfpRBneW96BkmS4G_oQAS47wzE5zQvvCl63XOyhN6tfI31Ia7_iFTX3BLtd4M2NuxBD3yXjZ-lykykS5bUU.bprkteNXKRsnyzStz5gk_yNPDj8s2Qapb0wCqXyinDQ&dib_tag=se&keywords=playstation%2B5&qid=1734955992&sprefix=play%2Caps%2C714&sr=8-3&th=1")

# price = driver.find_element(By.CSS_SELECTOR, value="span.aok-offscreen+span").text
# price = " ".join(price.split()).replace(" ", ".")
# print(f"PlayStation 5 price: {price}")

# XPATH will always work (Just right click the required element and copy XPATH)
model_num = driver.find_element(By.XPATH, value="//*[@id='feature-bullets']/ul/li[1]/span").text.strip(".").split(" ", maxsplit=2)[2]
print(f"Model Number: {model_num}")

# driver.find_elements()

driver.close() # Close the active tab
# driver.quit() # Close the entire browser window
