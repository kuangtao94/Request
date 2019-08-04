import requests
#禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 1.由于登录时候是多加 2 个 cookie，我们可以先用 get 方法打开登录首页，获取部分 cookie
# 2.再把登录需要的 cookie 添加到 session 里
# 3.添加成功后，随便编辑正文和标题保存到草稿箱

#博客园账号登录请求实例
url = "https://account.cnblogs.com/signin?returnurl=https%3A%2F%2Fwww.cnblogs.com%2F"
headers = {
    "Connection": "keep-alive",
    "Content-Length": "1054",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "https://account.cnblogs.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "_ga=GA1.2.309422837.1547046866; __gads=ID=fda98058cc409734:T=1547046870:S=ALNI_MZyZa4iJ53G-i7vMO8VplOItZ2oNw; UM_distinctid=168f9db4983533-0dd7abeb8ec9cd-5d1f3b1c-100200-168f9db49841e4; _gid=GA1.2.95674778.1562082991; .Cnblogs.Account.Antiforgery=CfDJ8D8Q4oM3DPZMgpKI1MnYlrkS_Cwkf_aCwOteUwJxddP-gTzD2D9-teYwdbKn0OoSj5rXiKTngS4gccbobLDyv7pUoPqN6S4NmNR1k-S-9rM8KNl5Rm8_b2QnUyIUtvn0LKSY_9ONIBaX3560-VJbP8w; .Cnblogs.Account.Session=CfDJ8D8Q4oM3DPZMgpKI1MnYlrnKDMrAv%2Fy7I1ep0xY4Ao1M1TzXwbju4u1o5aaRpknkkPPAs3XYbrnX%2BMB80RuT%2B6usTNTZlhIBPOrUk%2B0QiYFNn8NQyDtDQx0MKiZ2mlVoCi4mUyS0ioK7mdKodjlEpHQlaU9pn3eZlqJ07jmCKjLG; SyntaxHighlighter=csharp; _gat=1; SERVERID=d0724c395727ce8eb048bea7fa14fd42|1562419203|1562415470",
}

payload = {
    "LoginName":"oHXdKngna9lRN4%2B2Gz1QnHDt%2F79wLlVea99Fb8qOnubdLSQ6%2BOeOAEzCmVELUloQndOdyu5U2XyI8%2B8cMfypR6WLzYfHg4F2BZHShXhyA2s15%2Ftq1%2BXFwakEZeaQqgPl13TN3uClLg7a1HA2SFZY%2BKaSWacuzGCnPOjLKwvxWj0%3D",
    "Password":"erxZIl1XsOUMbCKZN3pOSLeyFhs9OYR1Sc38SshlAhAi6yYwnulU2W8QjrpBwgbV6eWhq4nlH97OlywwsHj1XSnvOAAToUmPLADheo%2BTtxWYNUX%2BFNczertn0vW1rdaFfST0fmDUqzB9EHQEBD%2FznOIyd%2FBtbJr93n9crrLKmpo%3D",
    "IsRemember":"true",
    "PublicKey":"MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCp0wHYbg%2FNOPO3nzMD3dndwS0MccuMeXCHgVlGOoYyFwLdS24Im2e7YyhB0wrUsyYf0%2FnhzCzBK8ZC9eCWqd0aHbdgOQT6CuFQBMjbyGYvlVYU2ZP7kG9Ft6YV6oc9ambuO7nPZh%2BbvXH0zDKfi02prknrScAKC0XhadTHT3Al0QIDAQAB",
    "EnableCaptcha":"true",
    "__RequestVerificationToken":"CfDJ8D8Q4oM3DPZMgpKI1MnYlrn7D18H3YXmkg89UN8NEh5cJ9GkpFNb1jSeQCXyOilUD1DftbrqQAvcukCkmQGeUVqrKjPoT289rSs8M1DNxu5BEMYndOf8Wn4bXQTNPVxf6lYFa0GgKQBLzeaX4FKI7ZM",
    "IsRemember":"false",
    "EnableCaptcha":"false",
    "isEncrypted":"true",
    "geetest_challenge":"b1fc6c4b9c986a45725d85674897bb59",
    "geetest_validate":"835a3c81f8a2876b26681849ab45eeb7",
    "geetest_seccode":"835a3c81f8a2876b26681849ab45eeb7%7Cjordan"
}

s = requests.Session()
r = requests.post(url=url,headers=headers,data=payload,verify=False)
#以content字节输出为例
result = r.content
print(type(result))
print(result.decode("utf-8"))
#json是经过encode成对应的python数据类型
result1 = r.json()
print(type(result1))
print(result1)
print(result1["success"]) # json 解码后，返回的就是一个字典

# 添加登录需要的两个 cookie
# c = requests.cookies.RequestsCookieJar()
# c.set(".CNBlogsCookie","F5FA59F286056634C88871863B1A3D6A8C08B07C1C09598196CBFC5C1E65133722DBC12776A4ABCDA34CAF35A6F857CF2F6BD626A4E1909885855549D041F0F4045AD1A8C3E8D4EC08E84FF4EB1ED2B65AB290D9")
# c.set(".Cnblogs.AspNetCore.Cookies","CfDJ8KlpyPucjmhMuZTmH8oiYTOWwe4-M6UcBrvO86OpKg2qDIJ1VFE5h-mBx7LtvXzUBVnFMSObn2JFeNTpk2siX2YRVYSmrpGFq8RgARvnocc-ETEDvMOLXyMAKwDMQcsWtPXuJsNJvghkLzWDtv42qLcUI6LulcQ3XNGBlxoxEIuwMMMZO_wKc-Rs1ZKkW23YZw2sPnSu5gUIhKeEtuG7YZLpyFJSE3ghEP8xWrr24cWaoBjwmN4nybPTvKqjizLpDeI1HqjdQhjlwRyz0OfHuxCocN5OrFraKB3DMLfJLr2wr3x97OCusm3k2N9GFde6ew")
# c.set('AlwaysCreateItemsAsActive',"True")
# c.set('AdminCookieAlwaysExpandAdvanced',"True")
# s.cookies.update(c)
# print (s.cookies)
#
# url1 = "https://home.cnblogs.com/"
# r1 = s.get(url=url1,headers=headers,verify=False)

#登录成功后保存编辑内容
# headers1 = {
#     "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",
#     "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "accept-language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#     "accept-encoding":"gzip, deflate, br",
#     "referer": "https://i.cnblogs.com/",
#     "content-type": "application/x-www-form-urlencoded",
# }

# 保存草稿箱
url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {
    "__VIEWSTATE":"",
    "__VIEWSTATEGENERATOR":"FE27D343",
    "Editor$Edit$txbTitle":"Hi,nnnnnnn",
    "Editor$Edit$EditorBody":"<p>你们好吗 ?</p><p>Are you ok ?</p>",
    "Editor$Edit$Advanced$ckbPublished":"on",
    "Editor$Edit$Advanced$chkDisplayHomePage":"on",
    "Editor$Edit$Advanced$chkComments":"on",
    "Editor$Edit$Advanced$chkMainSyndication":"on",
    "Editor$Edit$Advanced$txbEntryName":"",
    "Editor$Edit$Advanced$txbExcerpt":"",
    "Editor$Edit$Advanced$txbTag":"",
    "Editor$Edit$Advanced$tbEnryPassword":"",
    "Editor$Edit$lkbDraft":"存为草稿",
}

# r2 = s.post(url2,data=body,verify=False)
# print(r.content.decode("utf-8"))

#打开我的随笔记
# url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
# r2 = s.post(url2,headers=headers1,allow_redirects=False,verify=False)

#打印出状态码，自动处理重定向请求
# print(r2.status_code)
# new_url = r.headers1[location]
# print(new_url)
# # r3 = requests.post(url2,data=body,verify=False)
# #print(r.cookies)
# # print(r.content)





