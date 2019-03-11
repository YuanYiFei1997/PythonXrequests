import requests
url = "http://www.baidu.com"
# def getHTMLText(url):
#     try:
#         r=requests.get(url,timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "产生异常"
# if __name__ == "__main__":
#     url = "http://item.jd.com/2967929.html"
#     print(getHTMLText(url))
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")