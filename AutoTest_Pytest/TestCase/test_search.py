# -*- coding: utf-8 -*-
import allure
import pytest
import sys

from Base.browser_engine import BrowserEngine
from TestPage.page_BaiduShouYe import *
#
# reload(sys)
# sys.setdefaultencoding('utf8')


@allure.feature(u"搜索功能")
class Test_search_baidu():

    # =====fixtures========
    def setup(self):
        self.driver = BrowserEngine().get_browser()  # 启动浏览器

    def teardown(self):
        self.driver.quit()  # 启动浏览器

    # =====测试用例========
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.story(u"搜索框搜索")
    def test_search(self):
        baidu_page = PageBaidu(self.driver, "https://www.baidu.com/", u"百度一下，你就知道")
        baidu_page.open()

        with allure.step(u"搜索框搜索内容为Pytest"):
            allure.attach(u'搜索内容', 'Pytest')
            baidu_page.input_search("Pytest")
            time.sleep(2)
            baidu_page.click_search()
            time.sleep(2)

        with allure.step(u"点击第三条搜索内容"):
            baidu_page.click_3th()
            time.sleep(2)

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.story(u"百度Logo进入")
    def test_search_logo(self):
        baidu_page = PageBaidu(self.driver, "https://www.baidu.com/", u"百度一下，你就知道")
        baidu_page.open()
        time.sleep(2)

        with allure.step(u"点击百度Logo进入搜索首页"):
            allure.attach(u'百度Logo', u'点击进入')
            baidu_page.click_logo()
            time.sleep(2)
