# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class EquipmentManagement(unittest.TestCase):
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
        sleep(10)
        self.driver.quit()

    def test1_add(self):
        # 组织机构
        sleep(1)
        self.driver.find_element_by_xpath('//div[@id="ext-comp-1009"]/div[1]/span/b').click()
        # 台账管理
        sleep(1)
        self.driver.find_element_by_xpath('//ul[@id="6"]/li[3]/a').click()
        sleep(1)
        el = self.driver.find_element_by_id('mainFrame')
        self.driver.switch_to.frame(el)
        sleep(1)
        el = self.driver.find_element_by_xpath('//iframe[@id="/SITO2000_CQ/admin/equipment_list.jsp "]')
        self.driver.switch_to.frame(el)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen45"]/span').click()
        sleep(1)
        self.driver.find_element_by_name('enterpriseName').send_keys('asd')
        sleep(1)
        self.driver.find_element_by_name('remark').send_keys('asd')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen203"]').click()






if __name__ == '__main__':
    unittest.main()
