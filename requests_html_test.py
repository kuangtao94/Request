from requests_html import HTMLSession
s = HTMLSession()

url = "https://www.cnblogs.com/Teachertao/tag/Selenium/"
r = s.get(url)
#xpath 方法
# file = r.html.xpath("//*[@id='myposts']/div/div/a",first=True).text
# print(file)
#
# all = r.html.xpath("//*[@id='myposts']/div/div/a")
# for item in all:
#     print(item.text)
#     print(item.absolute_links)
#
#css 方法
file_css = r.html.find("#myposts>div>div>a")
# print(file_css.html)
# print(file_css.attrs)

print(file_css.find("value"))

css_all = r.html.find("#myposts>div>div>a")
for item in css_all:
    # print(item.text)
    # print(item.absolute_links)
    # print(item.html)
    pass