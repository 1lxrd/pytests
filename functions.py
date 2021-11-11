import requests
import json
from selenium import webdriver
import pytest

def getting(link): #http request func

    get = requests.get(link)  # GET
    status = get.status_code  # Status code, 200 if ok
    print(status)
    answer = get.json()  # returns json.loads(get.text), converting to python dict
    return answer

def element_is_present(browser, selector):

    element = None
    element = browser.find_element_by_css_selector(selector)
    assert element != None, "No such element"
    
def search(browser):
    expected_link = "www.google.com/search?q=Testing+google+search"
    search_result = None
    search_input = browser.find_element_by_css_selector(".gLFyf.gsfi")
    search_input.send_keys("Testing google search")
    search_btn = browser.find_element_by_css_selector("div.FPdoLc > center > input.gNO89b")
    search_btn.click()
    link = browser.current_url
    assert expected_link in link, "Search doesn't work"
    search_result = browser.find_element_by_css_selector("div.yuRUbf > a > h3[class = 'LC20lb DKV0Md']")
    assert search_result != None, "Search doesn't work or no search result was found"
