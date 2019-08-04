import requests
#禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
"""
1.由于登录时候是多加 2 个 cookie，我们可以先用 get 方法打开登录首页，获取部分 cookie
2.再把登录需要的 cookie 添加到 session 里
3.添加成功后，随便编辑正文和标题保存到草稿箱
"""

def Blog_login(url,s,header):
    # 先打开登录首页，获取部分 cookie
    # header = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    #     }

    # s = requests.Session()
    r = s.get(url,headers=header)
    print(r.cookies)

    # 添加登录需要的两个 cookie
    c = requests.cookies.RequestsCookieJar()
    c.set(".Cnblogs.AspNetCore.Cookies","CfDJ8D8Q4oM3DPZMgpKI1MnYlrmOY_jOv7gEsF3KQAjD-Qt4Xdu-H8ce-oT6zHXBNx9MolL_faNWYW9iKAa8PK7Pj2BcNPuE2GkbkHRkTcp5sRh9tyEPQnrfYbvk-N3MssxPnMKBZu8RKO3HynjNdYEw4nxRNBTzmobZwThrQ_EaoM-jRlTmBhb7x0eL-LSyH5ZwAaAuOmf1qtyZyBYEZZs3TF6XPSaTF3KIUYQBnErd9AorsIr70bum9NDAHlj5Onmt11kJU3fZVhFfgfzqsUzGP5loEHtZPiERZpLfNVCVde6AwW5VzDwYzhK6lCt0Au5_EoEQwCRte6xs_8BV6i1L5WeOXvtt8Ld4bBDI8sLi-2ZS01t4Z6QsDR-YJjYmAjKNJ4v7W8yrvAfXXADzce3s9CtWUGC9hjAAYPEnt6kGEAVQrbl9fCvUqhGf3mlFd7PI5fD7PunxMQeOan8K3xemgXY;")
    c.set(".CNBlogsCookie","9AD453CAE2BBDCB95396325383FAFEFB9D991F80457AF26B0C29622884FABD7EA5083E0035A350120B68A2955C47A3055B1E320881F86FEC34EEDA1E16CAA0174463E4F2AE4EF976798BB27F058483C0E368E7B2")
    # c.set('AlwaysCreateItemsAsActive',"True")
    # c.set('AdminCookieAlwaysExpandAdvanced',"True")
    s.cookies.update(c)
    print(s.cookies)
    return s.cookies

def save_box(s,url2,title,body_data,header):
    # 登录成功后保存编辑内容
    r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=header,verify=False)
    # print(r1.text)

    # 保存草稿箱
    body = {
        "__VIEWSTATE":"",
        "__VIEWSTATEGENERATOR":"FE27D343",
        "Editor$Edit$txbTitle":title,
        "Editor$Edit$EditorBody":body_data,
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

    r2 = s.post(url2,data=body,verify=False)
    # print(r.content.decode("utf-8"))
    #获取当前的url地址
    save_url = r2.url
    print(save_url)
    return save_url

def get_postid(u):
    #正则获取需要的postid参数
    import re
    postid = re.findall(r"postid=(.*?)&",u)
    print(postid) #正则提取的值是list
    if len(postid)<1:
        return ""
    else:
        return postid[0]   #提取为字符串

def delete_box(s,url3,postid):
    #删除草稿箱
    form_json = {"postId":postid}
    result = s.post(url3,json=form_json,verify=False)
    print(result.json())

if __name__ == '__main__':
    url = "https://account.cnblogs.com/signin?returnurl=https%3A%2F%2Fwww.cnblogs.com%2F"
    s = requests.Session()
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }
    Blog_login(url,s,header)
    url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
    u = save_box(s,url2,"Hi,你们","Are you ok？",header)
    postid = get_postid(u)
    url3 = "https://i.cnblogs.com/post/delete"
    delete_box(s,url3,postid)


