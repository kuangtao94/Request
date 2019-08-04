# import requests
#
# headers = {
#     'Referer': 'https://www.cnblogs.com/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
# }
#
# params = (
#     ('callback', 'jQuery2200413004729094411_1561990046451^'),
#     ('_', '1561990046452'),
# )
#
# response = requests.get('https://passport.cnblogs.com/user/LoginInfo', headers=headers, params=params)
#
# #NB. Original query string below. It seems impossible to parse and
# #reproduce query strings 100% accurately so the one below is given
# #in case the reproduced version is not "correct".
# # response = requests.get('https://passport.cnblogs.com/user/LoginInfo?callback=jQuery2200413004729094411_1561990046451^&_=1561990046452', headers=headers)
# print(response)


# import requests
# url = "http://apis.juhe.cn/cook/query.php"
# from_data = {"key":" 35c8198cbf59973960f06bd543086003","menu":" 秘制红烧肉"}
# r = requests.post(url,params=from_data)
# print(r.json())
# print(r.url)
#
# import requests
# url1 = "http://apis.juhe.cn/cook/query.php"
# params_data = {"key":" 35c8198cbf59973960f06bd543086003","menu":"豆腐"}
# r1 = requests.get(url1,params=params_data)
# print(r1.text)
# print(r1.status_code)
# print(r1.url)


# import requests
# import json
# #python的字典
# payload = {"yy":True,"gg":False}
# print(type(payload))
# #转化为json格式
# data_json = json.dumps(payload)  # 字典序列化转化用dumps
# print(type(data_json))
# print(data_json)


from requests_html import HTMLSession
s = HTMLSession()
r = s.get("https://www.python.org/")

all_links = r.html.links
print(all_links)

all_abslinks = r.html.absolute_links
print(all_abslinks)