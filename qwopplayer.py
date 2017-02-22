from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

def get_random(list):
    return random.choice(list)


browser = webdriver.Firefox()

browser.get('http://foddy.net/Athletics.html')
htmlElem = browser.find_element_by_tag_name('html')
movekeys=['q','w','o','p']

while(True):
    htmlElem.send_keys(get_random(movekeys))
