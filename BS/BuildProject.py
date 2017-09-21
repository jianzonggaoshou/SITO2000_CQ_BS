# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class YearPlan(unittest.TestCase):
    """BS端增加检测项"""
    # 项目名称
    project_name = u'非计划创建项目test3'

    def setUp(self):
        print("start"),
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        self.driver.maximize_window()
        self.driver.get("http://172.16.40.240:9999/SITO2000_CQ")
        sleep(1)
        # 登录密码
        self.driver.find_element_by_id('userId').clear()
        self.driver.find_element_by_id('userId').send_keys('wentao')
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys('123456')
        # 登录
        self.driver.find_element_by_xpath('//button[@onclick="login();"]').click()
        # 等待
        sleep(5)

    def tearDown(self):
        print("end"),
        sleep(200)
        self.driver.quit()

    def test1_add(self):
        # 项目管理
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen29"]/b').click()
        # 创建项目
        sleep(1)
        self.driver.find_element_by_xpath('//ul[@id="2"]/li[1]/a').click()
        # 转换iframe
        sleep(1)
        self.driver.switch_to.frame('mainFrame')
        self.driver.switch_to.frame('/SITO2000_CQ/workflow/project_add.jsp')
        # 项目基本信息
        # 用户单位
        sleep(1)
        self.driver.find_element_by_id('enterpriseId').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen71"]/div[9]').click()
        # 检测地点
        sleep(1)
        self.driver.find_element_by_id('substationId').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen74"]/div').click()
        # 项目名称
        sleep(1)
        self.driver.find_element_by_id('projectName').send_keys(YearPlan.project_name)
        # 开始时间
        sleep(1)
        self.driver.find_element_by_id('startTime').send_keys('2017-09-21')
        # 结束时间
        sleep(1)
        self.driver.find_element_by_id('endTime').send_keys('2017-12-30')
        # 项目描述
        sleep(1)
        self.driver.find_element_by_id('projectNote').send_keys(u'非计划创建项目test1')

        # 添加检测项目
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen28"]').click()
        # 待检测项目
        sleep(1)
        self.driver.find_element_by_id('deviceType').click()
        # 红外精确测温
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen108"]/div[2]/div').click()
        # 再次点击待检测项目
        sleep(1)
        self.driver.find_element_by_id('deviceType').click()
        # 确定
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen90"]').click()

        # 红外精确测温选择设备
        # 1和6
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen157"]/div[1]/table/tbody/tr/td[2]/div/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen157"]/div[6]/table/tbody/tr/td[2]/div/div').click()
        # 实施单位
        sleep(1)
        self.driver.find_element_by_id('companyId_2').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen203"]/div[12]').click()
        # 检测仪器
        sleep(1)
        self.driver.find_element_by_id('device_2').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen205"]/div/div').click()
        sleep(1)
        self.driver.find_element_by_id('device_2').click()
        # 检测人员
        sleep(1)
        self.driver.find_element_by_id('user_2').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen208"]/div[1]/div').click()
        sleep(1)
        self.driver.find_element_by_id('user_2').click()
        # 发布
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen32"]').click()

    def test2_start(self):
        # 项目管理
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen29"]/b').click()
        # 项目管理
        sleep(1)
        self.driver.find_element_by_xpath('//ul[@id="2"]/li[2]/a').click()
        # 转换iframe
        sleep(1)
        self.driver.switch_to.frame('mainFrame')
        self.driver.switch_to.frame('/SITO2000_CQ/project/management.jspx')
        # 默认开始第一个项目
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/span[1]/img').click()

        # 进入【开始项目】界面
        # 转换iframe
        sleep(1)
        self.driver.switch_to.parent_frame()
        el = self.driver.find_element_by_xpath('//iframe[contains(@id, "/SITO2000_CQ//action/sd/start/project.jspx?projectId")]')
        self.driver.switch_to.frame(el)
        # 勾选检测现场负责人
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-comp-1019"]').click()
        # 点击【开始】
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen19"]').click()

if __name__ == '__main__':
    unittest.main()
