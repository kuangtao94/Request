import requests,re,urllib3,hashlib
from bs4 import BeautifulSoup

# def encryptPwd(passwd):
#     # 对密码进行了md5双重加密
#     passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()
#     # veennike 这个值是在js文件找到的一个写死的值
#     passwd = 'veenike' + passwd + 'veenike'
#     passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()
#     return passwd


# def getTokenCode(s):
#     """
#      要从登录页面提取token，code， 然后在头信息里面添加
#      <!-- 页面样式 -->    <!-- 动态token，防御伪造请求，重复提交 -->
#     <script>
#     window.X_Anti_Forge_Token = 'b792db29-d4d3-484e-98b4-04bbe0f628fe';
#     window.X_Anti_Forge_Code = '36611432';
# </script>
#  """
#     url = "https://passport.lagou.com/login/login.html"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
#     }
#     # 更新session的headers
#
#     s.headers.update(headers)
#     data = s.get(url, verify=False)
#     # print(data.content.decode("utf-8"))
#     soup = BeautifulSoup(data.content, "html.parser")
#     token = soup.find_all("script")[1].get_text()
#     # print(token)
#
# if __name__ == '__main__':
#     s = requests.Session()
#     getTokenCode(s)


import os

print(os.path.join(os.path.dirname(os.path.realpath(__file__)),"F1.py"))