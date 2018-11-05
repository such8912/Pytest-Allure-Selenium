# encoding: utf-8
"""
@author: suchao
@file: shell.py
@time: 2018/11/5 14:25
@desc:Shell类，用来执行CMD Shell
"""

import subprocess


class Shell:

    @staticmethod
    def invoke(cmd):
        # shell设为true，程序将通过shell来执行
        # stdin, stdout, stderr分别表示程序的标准输入、输出、错误句柄。
        # 他们可以是PIPE，文件描述符或文件对象，也可以设置为None，表示从父进程继承。
        # subprocess.PIPE实际上为文本流提供一个缓存区
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        if output == "":
            print "Shell Error is:" + errors
        else:
            print  output
