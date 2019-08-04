from selenium import webdriver
import time
driver = webdriver.Chrome() #加载浏览器
driver.get("https://www.baidu.com/")

#加载cookies
cookie_1 = {"name":"BAIDUID","value":"C6CEAB4D3A1DFC502C82A1B71F2D3D53:SL=0:NR=10:FG=1"}
cookie_2 = {"name":"BDUSS","value":"zJySlRubUUweTNLTGxzRzBjYVBXSHU0LU9XTG4xbERaalIxY3puTVlSaTRydXBjSVFBQUFBJCQAAAAAAAAAAAEAAACyKyphz6PN-8P3zOy4~LrDODYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALghw1y4IcNcM"}
driver.add_cookie(cookie_1)
driver.add_cookie(cookie_2)

time.sleep(5)
driver.get("https://www.baidu.com/")
