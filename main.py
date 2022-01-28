from email import header
from gettext import gettext
from operator import index
from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.com/s?k=ps5&crid=1LAAS88RX1S1K&sprefix=%2Caps%2C311&ref=nb_sb_noss"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-61ea22cf-21c763f774e060da22af46cb"}
page = requests.get(url,headers=headers).text
soup = BeautifulSoup(page, "lxml") #extract content on page

titles = soup.find_all('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
prices = soup.find_all('span', attrs={'class':'a-offscreen'})
def getTitles():
    for title in titles:
        print(title.get_text().strip())
        print("\n")
   
def getPrices():
      for price in prices:
            print(price.get_text().strip())  
            print("\n")        

getTitles()
getPrices()