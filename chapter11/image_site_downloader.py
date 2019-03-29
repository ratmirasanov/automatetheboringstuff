import os
import requests

from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


BROWSER = webdriver.Firefox()
BROWSER.get("https://www.flickr.com")

SEARCH_FIELD = BROWSER.find_element_by_id("search-field")
SEARCH_FIELD.send_keys("Cats")
SEARCH_FIELD.send_keys(Keys.ENTER)

IMAGES = ui.WebDriverWait(BROWSER, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".view.photo-list-photo-view.awake")))

for image in IMAGES:

    image_url = image.value_of_css_property("background-image").split('"')[1]
    # Save the image to ./flickr.
    res = requests.get(image_url)
    res.raise_for_status()

    image_file = open(os.path.join("./chapter11/flickr", os.path.basename(image_url)), "wb")

    for chunk in res.iter_content(100000):

        image_file.write(chunk)

    image_file.close()

BROWSER.quit()
