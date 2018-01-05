from multiprocessing import Pool
from ccsu1 import ccsu_list,url_list1
from ccsu2 import get_links_from,url_list,item_info,get_item_info
index_url = [item["url"]for item in url_list1.find()]
document_list_url = [item["url"]for item in url_list.find()]
exist_url = [item["url"]for item in item_info.find()]
x = set(document_list_url)
y = set(exist_url)
rest_of_url = x-y
def get_all_links_from(channel):
    for i in range(1,180):
        get_links_from(channel,i)
#get_all_links_from('http://news.ccsu.cn/zdyw.htm')
def get_all_info_from(url):
        get_item_info(url)
if __name__ == '__main__':
    pool = Pool()
    pool = Pool(processes=5)
    # try:
    #     pool.map(get_all_links_from,index_url)
    #     pool.close()
    #     pool.join()
    # except :
    #     pass
    try:
        pool.map(get_all_info_from,rest_of_url)
        pool.close()
        pool.join()
    except (AttributeError,IndexError):
        pass

