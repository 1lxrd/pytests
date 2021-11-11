import functions
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.google.com/")

def test_elements():
    functions.element_is_present(browser, "[alt='Google'].lnXdpd")
    functions.element_is_present(browser, ".gLFyf.gsfi")
    functions.element_is_present(browser, "div.FPdoLc > center > input.gNO89b")

def test_search():
    functions.search(browser)
    browser.quit()