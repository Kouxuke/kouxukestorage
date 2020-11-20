# import sys
# sys.path.append(r'C:\Users\Administrator\PycharmProjects\autosuyuansys\common\majorfunctionfwm.py')



import sys
import os
curPath = os.path.abspath(os.path.dirname(r'C:\Users\Administrator\PycharmProjects\autosuyuansys\common\majorfunctionfwm.py'))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
from common import login1
from testcase import test_03
fwm = test_03.FWM()
denglu=login1.Test_Denglu()
import time
class Test_size(unittest.TestCase):
    # @classmethod
    # def setUpClass(self):
    #     denglu.Denglu()
    #     x=denglu.driver.find_element_by_css_selector('#top_menu > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').text
        # y='前台浏览'
        # self.assertTrue(x)
    def test_xzlb_34(self):  # 正常批量生成防伪码
            fwm.fwmgl_plscfwm()
            x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
            self.assertTrue(x, msg='失败')

    def test_xzlb_35(self):  # 防伪码长度为7位前缀为五位正常批量生成防伪码
        fwm.fwmgl_plscfwm2()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

    def test_xzlb_36(self):  # 防伪码长度为13位前缀为1位正常批量生成防伪码
        fwm.fwmgl_plscfwm3()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

    def test_xzlb_37(self):  # 防伪码功能为禁用正常批量生成防伪码***
        fwm.fwmgl_plscfwm4()
        # x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        # self.assertTrue(x, msg='失败')

    def test_xzlb_38(self):  # 正常单个生成防伪码
        fwm.fwmgl_dgscfwm()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

    def test_xzlb_39(self):  # 按物流码修改防伪码
        fwm.fwmgl_awlmplxgfwm()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

    def test_xzlb_40(self):  # 错误按物流码修改防伪码
        fwm.fwmgl_cwawlmplxgfwm()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

    def test_xzlb_41(self):  # 按防伪ID修改防伪码
        fwm.fwmgl_afwidplxgfwm()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

    def test_xzlb_42(self):  # 错误按防伪ID修改防伪码
        fwm.fwmgl_cwafwidplxgfwm()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

    def test_xzlb_43(self):  # 按批次批量修改防伪码
        fwm.fwmgl_apcplxgfwm()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

    def test_xzlb_44(self):  # 按产品批量修改防伪码
        fwm.fwmgl_apcplxgfwm()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

    def test_xzlb_45(self):  # 按生成日期修改防伪码
        fwm.fwmgl_ascrqxgfwm()
        # x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        # self.assertTrue(x, msg='失败')

    def test_xzlb_46(self):  # 按批次批量删除防伪码
        fwm.fwmgl_apcplscfwm()
        # x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        # self.assertTrue(x, msg='失败')

    def test_xzlb_47(self):  # 按产品名批量删除防伪码
        fwm.fwmgl_acpmplscfwm()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

    def test_xzlb_48(self):  # 按生成日期批量删除防伪码
        fwm.fwmgl_ascrqplscfwm()
        # x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        # self.assertTrue(x, msg='失败')

    def test_xzlb_49(self):  # 按查询次数批量删除防伪码
        fwm.fwmgl_acxcsplscfwm()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

    # def test_xzlb_50(self):  # 按查询次数批量删除防伪码
    #     fwm.fwmgl_scqbfwm()
    #     x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
    #     self.assertTrue(x, msg='失败')

    @classmethod
    def tearDownClass(cls):
        denglu.driver.quit()


if __name__ == '__main__':
        unittest.main()