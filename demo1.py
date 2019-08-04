from urllib import request

blog_url = "http://www.renren.com/452057374/profile?ref=page"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Cookie":"anonymid=jxnaj8rg5wdnq5; depovince=GW; _r01_=1; ick_login=0c587648-8660-440c-913f-c714b94463af; first_login_flag=1; ln_uact=970138074@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20170428/1700/main_nhiB_aebd0000854a1986.jpg; JSESSIONID=abcXfOMKPeSzK5l9jf4Uw; jebe_key=d6f7059a-7958-4646-b1f9-7c1cd3fd518b%7Ca022c303305d1b2ab6b5089643e4b5de%7C1562161493037%7C1%7C1562161351137; wp_fold=0; XNESSESSIONID=abc0mJDcvhF-r_Xqmh4Uw; jebecookies=b6676396-5192-4dc9-a5d1-5105c2641b28|||||; _de=EA5778F44555C091303554EBBEB4676C696BF75400CE19CC; p=ff0a6aa6cef85429d1ac5813071ed2751; t=f17489916473d3f059c29ecfcc7f67d11; societyguester=f17489916473d3f059c29ecfcc7f67d11; id=443362311; ver=7.0; xnsid=47d09ea3; loginfrom=null; fenqi_promotion_origin=587; fenqi_user_city=36"
}

req = request.Request(url=blog_url,headers=headers)
resp = request.urlopen(req)
with open("renren_file.html","w",encoding="utf-8") as file:
    #write函数必须写入一个str的数据类型
    #resp.read()读出来的是一个bytes数据类型
    #bytes -> decode -> str  解码
    #str -> encode -> bytes  编码
    file.write(resp.read().decode("utf-8"))