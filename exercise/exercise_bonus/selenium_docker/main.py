import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

games = {
    "Witcher": "292030",
    "Factorio": "427520"
}

game = "Witcher"

service = Service(executable_path="./geckodriver")
options = Options()
options.headless = True
# noinspection PyArgumentList
driver = webdriver.Firefox(service=service, options=options)

driver.get(f"https://store.steampowered.com/app/{games.get(game, '')}")

search = driver.find_element(By.ID, "store_nav_search_term")
elements = driver.find_elements(By.CLASS_NAME, "game_purchase_action")

price = ""

for element in elements:
    if "Add to Cart" in element.text:
        price = element.text.split("\n")[-2]
        break
driver.close()

with open("/home/tom/volume/prices.txt", "r+") as f:
    print(f.read())
    f.write(price)

