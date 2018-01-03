import requests
import os
def save(url):
    root = "D://ping/file//"
    path = root + url.split("/")[-1]
    print(path)
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件存在")
    except:
        print("文件爬取失败")
save("http://news.ccsu.cn/info/1121/20184.htm")