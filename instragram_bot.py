from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time, urllib.request
import requests

path = r"C:\DTI\chromedriver_win32\chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://www.instagram.com/")
