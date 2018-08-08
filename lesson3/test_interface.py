# coding=utf-8
import unittest
from urllib.parse import urlparse, parse_qsl, parse_qs
import requests
from parameterized import parameterized

class TestInterfaceBaseFunc(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestInterfaceBaseFunc, self).__init__(*args, **kwargs)
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "newsbj.app.autohome.com.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
        }
        self.url = "https://newsbj.app.autohome.com.cn/carhelper_v8.9.0/news/carhelper.ashx?userid=0&pm=2&source=3&ask=%E5%A5%A5%E8%BF%AAa4l%E4%B8%8A%E5%B8%82%E6%97%B6%E9%97%B4%E3%80%82&pname=%E5%8C%97%E4%BA%AC&osver=0&cname=%E5%8C%97%E4%BA%AC&_timestamp=1532416054&latitude=39.98533139448861&projectid=2&conid=S4EVqiw0ss84oVtGm&version=9.3.0&refer=&cid=110100&deviceid=f7afe07726d41444b6c449175e14d018e90db0c2&isfirst=0&longitude=116.3187476653883&pid=110000&_appid=app&_sign=05FD4ADEE55F49EE44437E013DE591AE"
        self.response = requests.get(self.url)
        # self.res_json = self.response.json()


    # @classmethod
    # def setUpClass(cls):
    #     headers = {
    #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #         "Accept-Encoding": "gzip, deflate, br",
    #         "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    #         "Cache-Control": "max-age=0",
    #         "Connection": "keep-alive",
    #         "Host": "newsbj.app.autohome.com.cn",
    #         "Upgrade-Insecure-Requests": "1",
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
    #     }
    #     url = "https://newsbj.app.autohome.com.cn/carhelper_v8.9.0/news/carhelper.ashx?userid=0&pm=2&source=3&ask=%E5%A5%A5%E8%BF%AAa4l%E4%B8%8A%E5%B8%82%E6%97%B6%E9%97%B4%E3%80%82&pname=%E5%8C%97%E4%BA%AC&osver=0&cname=%E5%8C%97%E4%BA%AC&_timestamp=1532416054&latitude=39.98533139448861&projectid=2&conid=S4EVqiw0ss84oVtGm&version=9.3.0&refer=&cid=110100&deviceid=f7afe07726d41444b6c449175e14d018e90db0c2&isfirst=0&longitude=116.3187476653883&pid=110000&_appid=app&_sign=05FD4ADEE55F49EE44437E013DE591AE"
    #     cls.response = requests.get(url, headers)
    #     cls.res_json = cls.response.json()

    # @parameterized.expand([
    #     "http://www.baidu.com",
    #     "https://newsbj.app.autohome.com.cn/carhelper_v8.9.0/news/carhelper.ashx?userid=0&pm=2&source=3&ask=%E5%A5%A5%E8%BF%AAa4l%E4%B8%8A%E5%B8%82%E6%97%B6%E9%97%B4%E3%80%82&pname=%E5%8C%97%E4%BA%AC&osver=0&cname=%E5%8C%97%E4%BA%AC&_timestamp=1532416054&latitude=39.98533139448861&projectid=2&conid=S4EVqiw0ss84oVtGm&version=9.3.0&refer=&cid=110100&deviceid=f7afe07726d41444b6c449175e14d018e90db0c2&isfirst=0&longitude=116.3187476653883&pid=110000&_appid=app&_sign=05FD4ADEE55F49EE44437E013DE591AE"
    # ])
    def test_return_code(self):
        self.assertEqual(
            self.response.status_code,
            200
        )
        print(self.url)

    def test_first_key(self):
        self.assertEqual(
            "returncode" in self.response.json().keys(),
            True
        )
        self.assertEqual(
            "message" in self.response.json().keys(),
            True
        )
        self.assertEqual(
            "result" in self.response.json().keys(),
            True
        )
        print(self.url)

    def test_returncode_is_right(self):
        self.assertEqual(
            self.response.json().get("returncode"),
            0
        )
        print(self.url)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)