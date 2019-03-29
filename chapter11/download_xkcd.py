#! python3
# download_xkcd.py -- Downloads every single XKCD comic.

import os
import requests
import bs4


URL = "https://xkcd.com"  # Starting URL.
os.makedirs("./chapter11/xkcd", exist_ok=True)  # Store comics in ./xkcd.

while not URL.endswith("#"):

    # Download the page.
    print("Downloading page %s..." % URL)
    RES = requests.get(URL)
    RES.raise_for_status()

    SOUP = bs4.BeautifulSoup(RES.text)

    # Find the URL of the comic image.
    COMIC_ELEMENT = SOUP.select("#comic img")

    if COMIC_ELEMENT == []:

        print("Could not find comic image.")

    else:

        try:

            COMIC_URL = "https:" + COMIC_ELEMENT[0].get("src")
            # Download the image.
            print("Downloading image %s..." % COMIC_URL)
            RES = requests.get(COMIC_URL)
            RES.raise_for_status()

        except requests.exceptions.MissingSchema:

            # Skip this comic.
            PREV_LINK = SOUP.select("a[rel='prev']")[0]
            URL = "https://xkcd.com" + PREV_LINK.get("href")

            continue

        # Save the image to ./xkcd.
        IMAGE_FILE = open(os.path.join("./chapter11/xkcd", os.path.basename(COMIC_URL)), "wb")

        for chunk in RES.iter_content(100000):

            IMAGE_FILE.write(chunk)

        IMAGE_FILE.close()

    # Get the Prev button's URL.
    PREV_LINK = SOUP.select("a[rel='prev']")[0]
    URL = "https://xkcd.com" + PREV_LINK.get("href")

print("Done.")
