# encoding: utf-8
"""
@author: suchao
@file: yaml.py
@time: 2018/11/6 10:44
@desc: Yaml类，解析Yaml文件
       data.yaml可以用来管理测试数据
"""

import yaml
import os


class Yaml:

    def __init__(self, file_path=None):
        self.data_s = []
        if file_path:
            self.path = file_path
        else:
            self.path = os.path.join(os.path.dirname(os.getcwd()), "data\\data.yaml")


    def read_yaml(self):
        with open(self.path) as f:
            data = yaml.load(f)
        return data

    def read_all_yaml(self):
        with open(self.path) as f:
            data = yaml.load_all(f)
            for x in data:
                self.data_s.append(x)
            return self.data_s


if __name__ == '__main__':
    y = Yaml()

    data = y.read_yaml()
    print data

    # datas = y.read_all_yaml()
    # print datas
