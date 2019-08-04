import requests,urllib3,os
from bs4 import BeautifulSoup
urllib3.disable_warnings()
from lxml import etree

def get_execution_it():
    result = {}
    url = "https://account.chsi.com.cn/passport/login?service=https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Fj_spring_cas_security_check"

    # 登录get方法，不用传入cookie
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }

    s = requests.Session()
    s.headers.update(header)
    r = s.get(url,verify=False)
    # print(r.content.decode("utf-8"))
    html = BeautifulSoup(r.content,"html.parser")
    # print(html)
    tag = html.find(class_="cr_top_my")
    print(len(tag))

    try:

        result["lt"] = html.xpath('//*[@id="fm1"]/input[1]')[0].get_text("value")
        result["execution"] = html.xpath('//*[@id="fm1"]/input[2]')[0].get_text("value")
        print(result)

    except:
        print("获取1t/execution失败")
    return result

if __name__ == '__main__':
    result = get_execution_it()



