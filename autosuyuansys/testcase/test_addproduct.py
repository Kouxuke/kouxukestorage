import time
from selenium import webdriver
import unittest
from common import loginto
from selenium.webdriver.support.select import Select
class Newaddproduct(loginto.Login_To):
    def test_02(self):
        time.sleep(5)
        self.driver.find_element_by_link_text('流程记录管理').click()
        self.driver.find_element_by_css_selector('li.sub-menu:nth-child(3) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()
        self.driver.find_element_by_css_selector('.col-sm-4 > input:nth-child(1)').send_keys('樱桃分拣3')
        self.driver.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('100')
        self.driver.find_element_by_css_selector('.btn').click()
        time.sleep(5)
        x=self.driver.find_element_by_link_text('流程类别名有重复!').text
        y="流程类别名有重复!"
        self.assertEqual(x,y,msg='失败')
    def test_03(self):
        time.sleep(5)
        self.driver.find_element_by_css_selector('.col-sm-4 > input:nth-child(1)').send_keys('樱桃分拣5')
        self.driver.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('101420')
        self.driver.find_element_by_css_selector('.btn').click()
        self.driver.find_element_by_link_text('流程类别管理').click()
        x=self.driver.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[3]').text
        y="樱桃分拣3"
        try:
            self.assertEqual(x,y,msg='失败')
        except Exception as e:
            print(e)
            time.sleep(5)
    def test_04(self):
        time.sleep(5)
        self.driver.find_element_by_css_selector('.col-sm-4 > input:nth-child(1)').send_keys('樱桃分拣6')
        self.driver.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('10501')
        Select(self.driver.find_element_by_css_selector('#zt')).select_by_value('禁止')
        self.driver.find_element_by_css_selector('.btn').click()



        # self.driver.find_element_by_css_selector('.btn').click()
        # time.sleep(2)
        # self.driver.find_element_by_link_text('流程类别管理').click()
        # x=self.driver.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[3]').text
        # y="樱桃分拣3"
        # try:
        #     self.assertEqual(x,y,msg='失败')
        # except Exception as e:
        #     print(e)

        #








