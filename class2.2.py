import requests
from bs4 import BeautifulSoup

# def getHtmlContent(url):
#     try:
#         r = requests.get(url)
#         r.raise_for_status()  # 如果状态码为200则不抛异常，反之则抛出异常
#         r.encoding = r.apparent_encoding
#         return r.content
#     except:
#         return "ERROR"


def getHtmlText(url, kv=None):
    try:
        if kv == None:
            r = requests.get(url)
        else:
            r = requests.get(url, params=kv)
        r.raise_for_status()  # 如果状态码为200则不抛异常，反之则抛出异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "ERROR"


# url = "https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=549569209,1741769597&fm=173&app=25&f=JPEG?w=587&h=395&s=E1321FD1DC8BBACC76B8892403008081"
# with open("D://1.jpeg", "wb") as f:
#     f.write(getHtmlContent(url))
url2 = "http://python123.io/ws/demo.html"
htmlText = getHtmlText(url2)
soup = BeautifulSoup(htmlText, "html.parser")
# print(soup.prettify)
print(soup.p.string)
s="<p><b>a</b>b<b>c</b></p>"
soup2 = BeautifulSoup(s,"html.parser")
print(soup2.p.contents)
for parent in soup2.p.parents:
    print(parent)
