from urllib import request,parse
from http.cookiejar import CookieJar

headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }

def get_opener():
    # 1.登录
    # 1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPCookieProcessor对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步的handler创建一个opener
    opener = request.build_opener(handler)
    return opener

def login_renern(opener):
    # 1.4 使用opener发送登录的请求(输入账号和密码)
    data = {
        "email":"970138074@qq.com",
        "password":"pythonspider"
    }
    login_url = "http://www.renren.com/PLogin.do"
    req = request.Request(login_url,data=parse.urlencode(data).encode("utf-8"),headers=headers)
    opener.open(req)

def visit_profile(opener):
    # 2.访问主页
    pro_url = "http://www.renren.com/452057374/profile?ref=page"
    #获取个人主页的页面的时候，不要新建一个opener
    #而应该使用之前的那个opener，因为之前的那个opener已经包含了登录所需要的cookie信息
    resp = opener.open(pro_url)
    with open("renren.html","w",encoding="utf-8") as file:
        file.write(resp.read().decode("utf-8"))

if __name__ == '__main__':
    opener = get_opener()
    login_renern(opener)
    visit_profile(opener)
