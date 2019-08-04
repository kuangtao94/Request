import requests

url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-75159101289910-zhongtong.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

s = requests.Session()
r = s.get(url,headers=headers,verify=False)
print(r.json())