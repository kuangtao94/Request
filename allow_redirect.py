import requests
#禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}
s = requests.Session()
#打开我的随笔
r = s.get(url,headers=headers,verify=False,allow_redirects=False)
# print(r.content.decode("utf-8"))
#打印状态码，自动处理重定向请求
print(r.status_code)
#获取重定向后的地址
print(r.headers["Location"])