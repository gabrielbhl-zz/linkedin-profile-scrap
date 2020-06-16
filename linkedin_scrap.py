import requirements
import parameters
from time import sleep
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
from urllib.parse import urlencode, urlparse, parse_qs
from lxml.html import fromstring
import parsel
from parsel import Selector
import unicodedata
import requests
from bs4 import BeautifulSoup
import csv
import re


#faz login no linkedin
driver = webdriver.Chrome(r"C:\Users\Gabriel\AppData\Local\Programs\Python\Python38\Lib\site-packages\seleniumwire\webdriver\chromedriver.exe")     #change to your path\to\chromedriver.exe or geckodriver.exe
driver.get('https://www.linkedin.com')
sleep(1)

username = driver.find_element_by_name("session_key")
username.send_keys(parameters.linkedin_username)
sleep(0.5)

password = driver.find_element_by_name("session_password")
password.send_keys(parameters.linkedin_password)
sleep(0.5)

log_in_button = driver.find_element_by_class_name("sign-in-form__submit-btn")
log_in_button.click()
sleep(0.5)


#entra no google para fazer a pesquisa
driver.get('https://google.com')
sleep(2)

search_query = driver.find_element_by_name('q')
search_query.send_keys(parameters.search_query)
sleep(1)

search_query.submit()
sleep(2.5)

writer = csv.writer(open(parameters.file_name, 'w', encoding='utf-8-sig', newline=''))
writer.writerow(['Name','Position','Company','Education', 'Location','URL'])

urls = driver.find_elements_by_xpath('//*[@class = "r"]/a[@href]')
urls = [url.get_attribute('href') for url in urls]
sleep(1)

for url in urls:

    driver.get(url)
    sleep(3)

    sel = Selector(text = driver.page_source)
    sleep(0.5)

    name = sel.xpath('//*[@class = "inline t-24 t-black t-normal break-words"]/text()').extract_first()
    name = ' '.join(name.split()) if name else None
    sleep(0.5)

    position = sel.xpath('//*[@class = "mt1 t-18 t-black t-normal"]/text()').extract_first()
    position = ' '.join(position.split()) if position else None
    sleep(0.5)

    company = sel.xpath('//*[@class = "pv-entity__secondary-title t-14 t-black t-normal"]/text()').extract_first()
    company = ' '.join(company.split()) if company else None
    sleep(0.5)
 
    education = sel.xpath('//*[@class="pv-entity__description t-14 t-normal mt4"]/text()').extract_first()
    education = ' '.join(education.split()) if education else None
    sleep(0.5)

    location = sel.xpath('//*[@class = "t-16 t-black t-normal inline-block"]/text()').extract_first()
    location = ' '.join(location.split()) if location else None
    sleep(0.5)

    print('\n')
    print('Name: ', name)
    print('Position: ', position)
    print('Company: ', company)
    print('Education: ', education)
    print('Location: ', location)
    print('URL: ', url)
    print('\n')

    sleep(0.5)

    writer.writerow([name,
    position,
    company,
    education,
    location,
    url])
    
    sleep(0.5)


driver.quit()