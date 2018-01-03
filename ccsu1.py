from bs4 import BeautifulSoup
import requests
import pymongo
client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ceshi']
url_list1 = ceshi['url_list_index']
start_url="http://news.ccsu.cn/index.htm"
url_host="http://news.ccsu.cn/"
def get_channel_urls(url):
    wb_data = requests.get(url)
    wb_data.encoding = 'utf-8'
    soup = BeautifulSoup(wb_data.text, "lxml")
    links= soup.select("body > div.navWrap.clearfix > div > ul > li > a")
    #print(links)
    for link in links:
        page_url =url_host + link.get("href")
        url_list1.insert_one({'url': page_url})
        print(page_url)
        #print(link.text)

# get_channel_urls(start_url)

ccsu_list = '''
http://news.ccsu.cn/index.htm
http://news.ccsu.cn/zdyw.htm
http://news.ccsu.cn/xysx.htm
http://news.ccsu.cn/mtjj.htm
http://news.ccsu.cn/xywh.htm
http://news.ccsu.cn/hdzt.htm
http://news.ccsu.cn/zdrw.htm
http://news.ccsu.cn/xbzx.htm
http://news.ccsu.cn/tzgg.htm
http://news.ccsu.cn/zlxz.htm
http://news.ccsu.cn/jxzd.htm

'''