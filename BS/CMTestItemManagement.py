# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv

reload(sys)
sys.setdefaultencoding('utf8')


class CMTestItemManagement(unittest.TestCase):
    """BS端增加检测项"""

    def setUp(self):
        print("start"),
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        self.driver.maximize_window()
        self.driver.get("http://172.16.40.240:9999/SITO2000_CQ")
        sleep(1)
        # 登录密码
        self.driver.find_element_by_id('userId').clear()
        self.driver.find_element_by_id('userId').send_keys('admin')
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys('123456')
        # 登录
        self.driver.find_element_by_xpath('//button[@onclick="login();"]').click()
        # 等待
        sleep(5)

    def tearDown(self):
        print("end"),
        sleep(100)
        self.driver.quit()

    def test1_add(self):
        # 配置管理
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen59"]/b').click()
        # 检测项管理
        sleep(1)
        self.driver.find_element_by_xpath('//ul[@id="7"]/li[1]/a').click()
        sleep(1)
        self.driver.switch_to.frame('mainFrame')
        self.driver.switch_to.frame('/SITO2000_CQ/action/sd/devicetype/list.jspx')

        # 读取本地csv文件
        data = csv.reader(open('TestItemManagement.csv', 'r'))

        for data_item in data:
            # 新增
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="ext-gen34"]/span').click()
            # 检测项名称
            sleep(1)
            self.driver.find_element_by_id('deviceTypeName').send_keys(data_item[0].decode('utf-8'))
            # 检测项编码
            sleep(1)
            self.driver.find_element_by_id('deviceCode').send_keys(data_item[1].decode('utf-8'))
            # 描述
            sleep(1)
            self.driver.find_element_by_id('remark').send_keys(data_item[2].decode('utf-8'))
            # 保存
            sleep(1)
            self.driver.find_element_by_xpath('//*[text()="保存"]').click()
            # 按键Esc键
            sleep(1)
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()


if __name__ == '__main__':
    unittest.main()
