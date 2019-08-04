import requests
import json
url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-75159101289910-zhongtong.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate/",
    "Referer": "http://www.kuaidi.com/",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "160",
    "Connection": "keep-alive",
    "Cookie": "lang=zh-cn; theme=default; sid=av73hleipg3ulnonfbpuqn98t7; UM_distinctid=16bcb288f061ac-08b943a81b5e15-39395704-100200-16bcb288f071c8; CNZZDATA1254194234=102758647-1562478423-%7C1562478423"

}

data = {
    "geetest_challenge":"16f109344848e9d0295edaae8465f91acy",
    "geetest_validate":'1a44a8b1c729d3caa78588038410c02e',
    "geetest_seccode":"1a44a8b1c729d3caa78588038410c02e%7Cjordan"
}
# data1=json.dumps(data)
# print(type(data1))
# print(data1)
s = requests.Session()
r = s.post(url,headers=headers,data=data,verify=False)
# print(r.cookies)
# print(r.text)
print(r.json()["companytype"])
# print(r.status_code)