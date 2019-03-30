import requests


def getHtmlText(url, kv):
    try:
        r = requests.get(url, params=kv)
        r.raise_for_status()  # 如果状态码为200则不抛异常，反之则抛出异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "ERROR"


# kv = {"wd": keyword}
# url = "http://www.baidu.com/s"
# text = getHtmlText(url, kv)
# print(text)
url2 = "http://www.so.com/s"
kv = {"q": "python"}
text = getHtmlText(url2, kv)
print(text)
