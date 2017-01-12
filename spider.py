import requests
from bs4 import BeautifulSoup
from pypinyin import lazy_pinyin


class Connection:
    def __init__(self):
        self.session = requests.session()
        self.session.headers.update({"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, "
                                                   "like Gecko) Chrome/49.0.2623.87 Safari/537.36"})
        self.home_url = 'http://m.autohome.com.cn/'

    def get_hot_cars(self):
        """获取首页的热门品牌
        @:return {'奥迪': ['//car.m.autohome.com.cn/brand/33/#pvareaid=100239', 'aodi'] : {"品牌名"：[url, 拼音]}
        拼音用于保存文件"""
        soup = BeautifulSoup(self.session.get(self.home_url).content, "lxml")
        contents = soup.find(class_='hot-brand').div.contents
        format_contents = {}
        for x in contents:
            if x != '\n':
                # 可能会有多个品牌同一个名字的问题？
                format_contents[x.text] = [x['href'][2:], ''.join(lazy_pinyin(x.text))]
        return format_contents
