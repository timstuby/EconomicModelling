from bs4 import BeautifulSoup
from selenium import webdriver
import time


PATH = '/Applications/Google Chrome Canary.app'



l=list()
o={}

target_url = "https://www.idealista.com/en/inmueble/101197712/"


driver=webdriver.Chrome(PATH)

driver.get(target_url)


time.sleep(5)
resp = driver.page_source
driver.close()