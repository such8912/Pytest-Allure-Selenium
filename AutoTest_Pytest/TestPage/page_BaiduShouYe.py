# encoding: utf-8
"""
@author: suchao
@file: page_test.py
@time: 2018/11/5 14:04
@desc:定义百度首页页面的元素和操作
"""

from Base.base_page import *


class PageBaidu(BasePage):
    loc_search_text = ('XPATH', '//*[@id="kw"]')
    loc_search_button = ('XPATH', '//*[@id="su"]')
    loc_logo_picture = ('XPATH', '//*[@id="lg"]/map/area')
    loc_3th = ('XPATH', '//*[@id="3"]/h3/a')

    def open(self):
        self._open(self.base_url, self.pagetitle)

    def input_search(self, text):
        self.find_element(self.loc_search_text).send_keys(text)

    def click_search(self):
        self.find_element(self.loc_search_button).click()

    def click_logo(self):
        self.find_element(self.loc_logo_picture).click()

    def click_3th(self):
        self.find_element(self.loc_3th).click()

