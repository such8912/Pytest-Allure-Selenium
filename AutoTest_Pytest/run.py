# encoding: utf-8
"""
@author: suchao
@file: run.py
@time: 2018/11/5 14:21
@desc:调用cmd，执行用例，并且生成Allure测试报告
"""
import pytest
import os
from utils.shell import Shell

if __name__ == '__main__':
    xml_report_path = os.path.join(os.getcwd(), "Report\\xml")
    html_report_path = os.path.join(os.getcwd(), "Report\\html")

    # 开始测试
    args = ['-s', '-q', '--alluredir', xml_report_path]
    pytest.main(args)

    # 生成html测试报告
    cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path)

    try:
        Shell.invoke(cmd)
    except:
        print u"Html测试报告生成失败,确保已经安装了Allure-Commandline"
