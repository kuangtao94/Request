import requests

base = 'http://127.0.0.1:81/'  # 禅道的服务器地址

loginUrl = base+"zentao/user-login-L3plbnRhby8=.html"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "95",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "lang=zh-cn; theme=default; lastProject=4; preProjectID=4; moduleBrowseParam=0; productBrowseParam=0; projectTaskOrder=status%2Cid_desc; windowWidth=1349; windowHeight=263; zentaosid=1pl122hjllud6mfv8lcs2tesa0",
    "Host": "127.0.0.1:81",
    "Origin": "http://127.0.0.1:81",
    "Referer": "http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

form_data = {
    "account": "admin",
    "password": "e10adc3949ba59abbe56e057f20f883e",
    "keepLogin[]": "on",
    "referer": base+"/zentao/my"
}

s = requests.Session()
r = s.post(loginUrl,headers=headers,data=form_data,verify=False)
print(r.content.decode("utf-8"))
print(r.url)

# result = s.get("http://127.0.0.1:81/zentao/qa/",headers=headers)
# print(result.content)

# 上传图片
url1 = "http://127.0.0.1:81/zentao/file-ajaxUpload-5d233ddbe3d17.html?dir=image"

f ={
    "localUrl": (None,"11.png"),
    "imgFile": ("1.png", open("F:\\软件测试资料\\松勤课程图片截图\\11.png", "rb"), "image/png")
  }
r = s.post(url1, files=f)
try:
    jpgurl = base+r.json()["url"]
    print(u"上传图片后的url地址：%s"%jpgurl)
except Exception as msg:
    print(u"返回值不是json格式：%s"%str(msg))
    print(r.content)