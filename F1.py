import requests

# 请求头
headers = {
"Connection": "keep-alive",
"Accept": "application/json, text/javascript, */*; q=0.01",
"Origin": "https://account.cnblogs.com",
"X-Requested-With": "XMLHttpRequest",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"Referer":"https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F",
"Accept-Encoding":"gzip, deflate, br",
"Cookie":"_ga=GA1.2.309422837.1547046866; __gads=ID=fda98058cc409734:T=1547046870:S=ALNI_MZyZa4iJ53G-i7vMO8VplOItZ2oNw; UM_distinctid=168f9db4983533-0dd7abeb8ec9cd-5d1f3b1c-100200-168f9db49841e4; .Cnblogs.Account.Antiforgery=CfDJ8D8Q4oM3DPZMgpKI1MnYlrmGpsks3Dk-VJ4CUSIzul0m6VyvM4zgmnRXbEMbo4I0acfTLRoa8t_PZZhv3IMNGi2NomMa-tnxV6YY-KCOzvirZeyAK3AEpySA8ljUYHaAOu1EBAykmiH2RPPyNVDU8wY; .Cnblogs.Account.Session=CfDJ8D8Q4oM3DPZMgpKI1MnYlrnP51HrpACKhjH0omIgR0opOLugWiW6N4aKG5q7dRvvueeJVdjnPHHvOAZOkuJLxRufseT5DHcQYDkFjdlf8Ae%2BbpN%2BRdD6D%2BD65RxXCSXw3ot4g1g%2FmD9h%2Fp9Lzl2Qua7DS8Dh7YRkF9d7dasron4H; _gid=GA1.2.546164367.1561788236; SERVERID=72a9dcfa61520d2c68e0c62ba3a369c8|1561824759|1561824683",
}
data = {
    "LoginName":"MkV5T69jUTwwMCI83Vq+WqxSsmjE1l6WqH9VqASOwxFZQ46mCuEMCV+1M6myy5tGwkzYk8sHdHe2WZi/argISsy2cjEe99DtF+x+TBW4BqK+Yww9vGsUCvE5J2cT/vVdaccF24wwbTS2lNjV/pN+oT7vJGvvsOQt0MJ6pT61SaU=",
    "Password":"KsmhE3n3Zqd4UirGLPvLpT841o8aXVoJGmpgku9o58jHoBex+uPAlgwkEfCHKfYvuWjKP/OSEngH0dqw7+lEK3fQZW/CXsg+InJXUGsf2nGaprZfZFMwbCcoopXJ/zHq75VprgnKY0L5Kmvm6o2pOwzFbi2dkbiHd89v4zxWWeI=",
    "PublicKey":"MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCp0wHYbg/NOPO3nzMD3dndwS0MccuMeXCHgVlGOoYyFwLdS24Im2e7YyhB0wrUsyYf0/nhzCzBK8ZC9eCWqd0aHbdgOQT6CuFQBMjbyGYvlVYU2ZP7kG9Ft6YV6oc9ambuO7nPZh+bvXH0zDKfi02prknrScAKC0XhadTHT3Al0QIDAQAB",
    "EnableCaptcha":"true",
    "__RequestVerificationToken":"CfDJ8D8Q4oM3DPZMgpKI1MnYlrm206IXNLiTmQuniu7kjMgAPHyfGrcItktxDzwfZwFkHqb0KMXQ8x_bAEN1k884Aa5XOmjy0RmNnEmUoETnD5-q_p76TixwtPMlPmQqEpXDj5VUyDOkZIGUPe5ot5fN9iA",
    "IsRemember":"false",
    "EnableCaptcha":"false",
    "isEncrypted":"true",
    "geetest_challenge":"60753239bee7cbf757d886ac91d3222f",
    "geetest_validate":"5b16cc4e3c2529647b8308372733f967",
    "geetest_seccode":"5b16cc4e3c2529647b8308372733f967|jordan"
}
url = "https://account.cnblogs.com/Account/SignIn?returnurl=https%3A%2F%2Fwww.cnblogs.com%2F"
r = requests.post(url=url,headers=headers,data=data,verify=False)
print(r.json())
print(r.cookies)


