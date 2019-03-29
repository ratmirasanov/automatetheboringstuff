#! python3
# lucky.py -- Opens several Google search results.

import sys
import webbrowser
import requests
import bs4


print("Googling...")  # Display text while downloading the Google page.
RES = requests.get("http://google.com/search?q=" + " ".join(sys.argv[1:]))
RES.raise_for_status()

# Retrieve top search result links.
SOUP = bs4.BeautifulSoup(RES.text, "html.parser")

# Open a browser tab for each result.
LINKS = SOUP.select(".r a")
NUM_OPEN = min(5, len(LINKS))
print(NUM_OPEN)

for i in range(NUM_OPEN):

    webbrowser.open("https://www.google.com" + LINKS[i].get("href"))
