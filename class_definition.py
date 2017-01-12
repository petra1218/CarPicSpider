import configparser


class Car:
    def __init__(self, brand):
        # 品牌
        self.brand = brand
        # 型号
        self.version = []
        # 颜色，考虑可能一款型号有多种颜色的情况。
        self.color = []


class ReadConfig:
    def __init__(self):
        cf = configparser.ConfigParser()
        cf.read('config.ini')
