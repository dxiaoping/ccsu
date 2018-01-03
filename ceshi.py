from bs4 import BeautifulSoup
import requests
import time
import pymongo

wb_data = requests.get("http://news.ccsu.cn/zdyw/201.htm")
wb_data.encoding = 'utf-8'
soup = BeautifulSoup(wb_data.text, 'lxml')
print(soup)