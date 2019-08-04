import requests
import unittest_1
from Request.Blog.API_Blog import Blog

class Test_Blog(unittest_1.TestCase):
    def setUp(self):
        s = requests.Session()
        self.blog = Blog(s)

    def tearDown(self):
        cookie = self.blog.login()
        print(cookie)

    def test_01(self):
        #第一步：登录
        self.blog.login()
        #第二步：保存
        sava_url = self.blog.save("Hi,nihao","jjndaidnwq")
        #第三步：获取postid
        postid = self.blog.get_postid(sava_url)
        #第四步：删除草稿
        result1 = self.blog.delete_box(postid)
        print(type(result1))
        self.assertEqual(result1["isSuccess"],True)

if __name__ == '__main__':
    # s = requests.Session()
    unittest_1.main(verbosity=2)




