from bs4 import BeautifulSoup
import requests
import time
import pymongo
url_host="http://news.ccsu.cn"
client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ceshi']
url_list = ceshi['url_list4']
item_info = ceshi['item_info4']


# 在最左边是在python 中对象的名称，后面的是在数据库中的名称
# spider 1
def get_links_from(channel,pages):
    # http: // news.ccsu.cn / zdyw / 179.htm
    channel = channel.split(".h")[0]
    list_view = '{}/{}.htm'.format(channel,str(pages))
    wb_data = requests.get(list_view)
    wb_data.encoding = 'utf-8'

    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('a'):
        time.sleep(1)
        for link in soup.select('div.main_conRCb > ul > li > a '):
            item_link = url_host+link.get('href').split("..")[1]
            put =0
            for item in url_list.find():
                if item_link ==item["url"]:
                    put = 1
            if put == 1:
                pass
            else:
                url_list.insert_one({'url': item_link}) # 数据库插入链接
                print(item_link)
                print(link.text)
                #get_item_info(item_link)
    else:
        pass
#get_links_from("http://news.ccsu.cn/zdyw.htm",180)
# spider 2
def get_item_info(url):
    wb_data = requests.get(url)
    wb_data.encoding = 'utf-8'
    # time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    no_longer_exist = '404' in soup.find('script', type="text/javascript").get('src').split('/')
    if no_longer_exist:
        pass
    else:
        title = soup.title.text
        times = soup.select('p')[0].text
        data = soup.select('#vsb_content > div')[0].text
        url = url
        item_info.insert_one({"title":title,"time":times,"data":data,"url":url})
        print(title,"\n",times,"\n",data)
#get_item_info("http://news.ccsu.cn/info/1121/17318.htm")