# coding=utf-8

import requests
from selenium import webdriver
import time, yaml
from selenium.common.exceptions import NoSuchElementException
import pymongo, datetime, re




def get_password(filepath):
    with open(filepath, "r") as f:
        data = yaml.load(f.read())
    up = data.get("github")
    return up["username"], up["password"]

class GetGithubStuff():

    def __init__(self):
        # 初始化
        self.url = "https://github.com"
        # 启动driver
        self.driver = webdriver.Chrome()
        # 访问url
        self.driver.get(self.url)
        # 执行登陆方法
        self.login()

    def login(self):
        # 定义登陆url
        login_url = "https://github.com/login"
        # 请求登陆链接
        self.driver.get(login_url)
        # 根据id获取位置
        u = self.driver.find_element_by_id("login_field")
        p = self.driver.find_element_by_id("password")
        # 获取登陆用户名密码，调用get_password方法
        username, password = get_password("user.yaml")
        # 输入用户名密码并回车
        u.send_keys(username)
        p.send_keys(password + "\n")


    def get_emails(self, search_url):
        # 请求搜索URL
        self.driver.get(search_url)
        # 获取数据块部分元素
        user_list = self.driver.find_elements_by_class_name("user-list-item")
        # 打开gdata.yaml文件，为后期存储做准备
        f = open("gdata.yaml", "w")
        # 循环获取数据
        for user in user_list:
            # 捕获异常
            try:
                email = user.find_element_by_class_name("muted-link")
                print(email.get_attribute("href")[7:])
                print(email.text)
                uname = user.find_element_by_tag_name("em")
                href = "https://github.com/%s" % uname.text
                print(uname.text)
                # 组装数据
                data = {
                    uname.text: {
                        "email": email.text,
                        "href": href,
                        "date": datetime.datetime.utcnow()
                    }
                }
                # 写yaml文件
                yaml.dump(data, f, default_flow_style=False)
            # 捕获找不到元素的异常
            except NoSuchElementException as e:
                pass
            # 捕获其他异常，当出现时，关闭文件
            except Exception as e:
                f.close()
        # 关闭文件
        f.close()
        # 关闭浏览器driver
        self.driver.close()


    def run(self):
        # 要获取多少页数据
        for n in range(1, 101, 1):
            # 定义搜索url
            url = "https://github.com/search?p=%s&q=jack&type=Users" % n
            self.get_emails(url)

class GetGithubStuffInOtherFunc():

    def login(self):
        url = "https://github.com/login"
        username, password = get_password("user.yaml")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
        }
        session = requests.Session()
        response = session.get(url, headers=headers)
        pattern = re.compile(r'<input type="hidden" name="authenticity_token" value=[^>]+>')

        authenticity_token = pattern.findall(response.text)[0][54:-4]
        # "commit=Sign+in&utf8=%E2%9C%93&authenticity_token=xAMCUKG8BNj50p7IWU%2F926kYe0H7fp6n9nYaM4o0QRhWfr%2FPb6ZhMo17Ea1oqsCD9sr%2FiUc%2FQeamxR%2FsJ31T3w%3D%3D&login=xiaoyaoyangeren%40gmail.com&password=ZhangNa3212088"
        data = {
            'commit': 'Sign in',
            'utf8': '%E2%9C%93',
            'authenticity_token': authenticity_token,
            'login': username,
            'password': password
        }
        print(data)
        session_url = 'https://github.com/session'
        response = session.post(session_url, headers=headers, data=data)
        print(response.content)

        # beautifulsoup pyquery


if __name__ == '__main__':
    # g = GetGithubStuffInOtherFunc()
    # g.login()
    g = GetGithubStuff()
    g.run()
    # save_email()