# encoding: utf-8
"""
@author: suchao
@file: configParse.py
@time: 2018/11/6 10:05
@desc:config配置文件解析类
"""
import ConfigParser
import os


class Config:
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.getcwd()), "data\\config.ini")
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.path)

    # 依据section和key读取指定信息
    def get_ini(self, section, key):
        try:
            result = self.cf.get(section, key)
        except:
            result = ""
        return result

    # 设置ini文件
    def set_ini(self, section, key, value):
        try:
            # self.cf.add_section(field)
            key_list = self.cf.sections()

            if section not in key_list:
                self.cf.add_section(section)

            self.cf.set(section, key, value)
            self.cf.write(open(self.path, 'w'))
        except:
            return False
        return True

    # 获取 section 列表
    # sections: ['db', 'ssh']
    def get_sections(self):
        return self.cf.sections()

    # 依据section获取其Key的列表
    # options of [db]: ['host', 'port', 'user', 'pass']
    def get_options(self, section):
        return self.cf.options(section)

    # 依据section获取其（Key，values)的元组列表
    # items of [ssh]: [('host', '192.168.1.101'), ('user', 'huey'), ('pass', 'huey')]
    def get_items(self, section):
        return self.cf.items(section)

    # 删除section


if __name__ == '__main__':
    cf = Config()
    # ip = cf.get_ini("ssh", "host")
    # print ip
