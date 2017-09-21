# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class YearPlan(unittest.TestCase):
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
        sleep(200)
        self.driver.quit()

    def test1_add(self):
        sleep(1)
        # 年计划申请
        sleep(1)
        self.driver.find_element_by_xpath('//ul[@id="1"]/li[2]/a').click()
        sleep(1)
        el = self.driver.find_element_by_id('mainFrame')
        self.driver.switch_to.frame(el)
        sleep(1)
        el = self.driver.find_element_by_xpath('//iframe[@id="/SITO2000_CQ/workflow/plan_list.jsp"]')
        self.driver.switch_to.frame(el)
        # 新增计划
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen92"]').click()
        self.driver.switch_to.parent_frame()
        el = self.driver.find_element_by_xpath('//iframe[@id="/SITO2000_CQ//sd/wf/plan_add.jspx"]')
        self.driver.switch_to.frame(el)

        # 单位
        sleep(1)
        self.driver.find_element_by_id('enterpriseId').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen138"]/div[7]').click()
        # 变电站
        sleep(1)
        self.driver.find_element_by_id('substationId').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen141"]/div').click()
        # 检测项目
        sleep(1)
        self.driver.find_element_by_id('deviceType').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen147"]/div[2]').click()
        # 设备名称
        sleep(1)
        self.driver.find_element_by_id('planEquipmentName').send_keys(u'变压器')
        # 电压级别
        sleep(1)
        self.driver.find_element_by_id('voltageCode').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen153"]/div[4]').click()
        # 检测周期
        sleep(1)
        self.driver.find_element_by_id('period').send_keys(u'1年')
        # 设备总数量
        sleep(1)
        self.driver.find_element_by_id('totalEquipmentCount').send_keys('10')
        # 事实单位
        sleep(1)
        self.driver.find_element_by_id('companyId').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen155"]/div[12]').click()
        # 计划检测年份
        sleep(1)
        self.driver.find_element_by_id('planYear').send_keys('2017')

        # 选择设备列表
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen97"]/div[1]/table/tbody/tr/td[2]/div/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen97"]/div[2]/table/tbody/tr/td[2]/div/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen97"]/div[6]/table/tbody/tr/td[2]/div/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen97"]/div[7]/table/tbody/tr/td[2]/div/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen117"]').click()

        # 计划检测月份
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen127"]/div/table/thead/tr/td[1]/div/div').click()

        # 提交
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen14"]').click()

        # ---------------------------------年计划审核--------------------------------
        self.driver.switch_to.default_content()
        # 年计划审核
        sleep(1)
        self.driver.find_element_by_xpath('//ul[@id="1"]/li[3]/a').click()
        sleep(1)
        el = self.driver.find_element_by_id('mainFrame')
        self.driver.switch_to.frame(el)
        sleep(1)
        el = self.driver.find_element_by_xpath('//iframe[@id="/SITO2000_CQ//sd/wf/plan_verify_list.jspx"]')
        self.driver.switch_to.frame(el)

        # 默认第一行审核
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen15"]/div[1]/table/tbody/tr/td[12]/div/a').click()

        sleep(1)
        self.driver.switch_to.parent_frame()
        el = self.driver.find_element_by_xpath('//iframe[contains(@id, "/SITO2000_CQ//sd/wf/plan_detail.jspx?operation=verify&planId=")]')
        self.driver.switch_to.frame(el)

        # 处理意见
        sleep(1)
        self.driver.find_element_by_id('note').send_keys(u'通过审核')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen14"]').click()
        # 确认
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen118"]').click()

        # ---------------------------------年计划审批--------------------------------
        self.driver.switch_to.default_content()
        # 年计划审核
        sleep(1)
        self.driver.find_element_by_xpath('//ul[@id="1"]/li[4]/a').click()
        sleep(1)
        el = self.driver.find_element_by_id('mainFrame')
        self.driver.switch_to.frame(el)
        sleep(1)
        el = self.driver.find_element_by_xpath('//iframe[@id="/SITO2000_CQ//sd/wf/plan_approve_list.jspx"]')
        self.driver.switch_to.frame(el)

        # 默认第一行审批
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen15"]/div/table/tbody/tr/td[12]/div/a').click()

        sleep(1)
        self.driver.switch_to.parent_frame()
        el = self.driver.find_element_by_xpath('//iframe[contains(@id, "/SITO2000_CQ//sd/wf/plan_detail.jspx?operation=approve&planId=")]')
        self.driver.switch_to.frame(el)

        # 处理意见
        sleep(1)
        self.driver.find_element_by_id('note').send_keys(u'通过审批')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen14"]').click()
        # 确认
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ext-gen135"]').click()


if __name__ == '__main__':
    unittest.main()
