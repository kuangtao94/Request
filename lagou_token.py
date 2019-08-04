import requests,re,urllib3,hashlib
from bs4 import BeautifulSoup
urllib3.disable_warnings()

class LoginLgw():
    def __init__(self,s):
        self.s = s

    def getTokenCode(self):
        """
         要从登录页面提取token，code， 然后在头信息里面添加
         <!-- 页面样式 -->    <!-- 动态token，防御伪造请求，重复提交 -->
        <script>
        window.X_Anti_Forge_Token = 'b792db29-d4d3-484e-98b4-04bbe0f628fe';
        window.X_Anti_Forge_Code = '36611432';
    </script>
     """
        url = "https://passport.lagou.com/login/login.html"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }
        # 更新session的headers
        self.s.headers.update(headers)
        data = self.s.get(url,verify=False)
        soup = BeautifulSoup(data.content,"html.parser")
        tokenCode = {}
        try:
            token = soup.find_all("script")[1].get_text()
            print(token)
            tokenCode['X_Anti_Forge_Token'] = re.findall(r"Token = '(.+?)'",token)[0]
            tokenCode['X_Anti_Forge_Code'] = re.findall(r"Code = '(.+?)'",token)[0]
            return tokenCode
        except:
            print("获取token和code失败")
            tokenCode['X_Anti_Forge_Token'] = ""
            tokenCode['X_Anti_Forge_Code'] = ""
            return tokenCode

    def encryptPwd(self, passwd):
        # 对密码进行了md5双重加密
        passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()
        # veennike 这个值是在js文件找到的一个写死的值
        passwd = 'veenike' + passwd + 'veenike'
        passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()
        return passwd

    def login(self, user, psw):
        '''
        function:登录拉勾网网站
        :param user: 账号
        :param psw: 密码
        :return: 返回json
        '''
        gtoken = self.getTokenCode()
        print(gtoken)
        print(gtoken['X_Anti_Forge_Token'])
        print(gtoken['X_Anti_Forge_Code'])
        url2 = "https://passport.lagou.com/login/login.json"
        headers2 = {
            "X-Anit-Forge-Code": gtoken['X_Anti_Forge_Code'],
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "X-Anit-Forge-Token": gtoken['X_Anti_Forge_Token'],
            "Referer": "https://passport.lagou.com/login/login.html"
        }
        # 更新s的头部
        self.s.headers.update(headers2)
        passwd = self.encryptPwd(psw)

        body = {
            "isValidate":"true",
            "username":	user,
            "password":	passwd,
            "request_form_verifyCode":"",
            "submit":"",
            "challenge":"8e2eabfd601c8ae65e536c327679d99c"
        }

        r2 = self.s.post(url2,headers=headers2,data=body,verify=False)
        try:
            print(r2.text)
            return r2.json()
        except:
            print("登录异常信息：%s" % r2.text)
            return None

if __name__ == "__main__":
    s = requests.Session()
    lgw = LoginLgw(s)
    lgw.login("账号", "密码")



