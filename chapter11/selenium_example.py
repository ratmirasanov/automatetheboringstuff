from selenium import webdriver


BROWSER = webdriver.Firefox()
BROWSER.get("https://inventwithpython.com")

try:

    ELEMENTS = BROWSER.find_elements_by_css_selector(".card-img-top.cover-thumb")

    for element in ELEMENTS:

        print("Found <%s> element with that class name!" % element.tag_name)

except:

    print("Was not able to find an element with that name.")
