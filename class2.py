import requests
def getHtmlText(url,keyword):
    try:
        kv={"wd":keyword}
        r=requests.get(url,params=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "ERROR"
url="http://www.baidu.com/s"
text= getHtmlText(url,"Python")
print(text)