import unittest

from common import login1
from testcase import test_01
from testcase import test_02
from testcase import test_03
xzlb = test_01.XZCP()
xzsy = test_02.SYGL()
fwm = test_03.FWM()
denglu=login1.Test_Denglu()
import time
class Test_size(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        denglu.Denglu()
        # x=denglu.driver.find_element_by_css_selector('#top_menu > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').text
        # y='前台浏览'
        # self.assertTrue(x)

    def test_xzlb_01(self):#新增流程类别

            xzlb.xzlclb()

    def test_xzlb_02(self):#新增流程类别反案例流程类别名有重复

        xzlb.xzlclb_FAN()

    def test_xzlb_03(self):#流程增添已禁用

        xzlb.xzlclb_lczt()

    def test_xzlb_04(self):#搜索

        xzlb.zclbgl_sousuo()

    def test_xzlb_05(self):#编辑

        xzlb.zclbgl_bianji()

    # def test_xzlb_06(self):#批量删除
    #     xzlb.zclbgl_plsc()

    # def test_xzlb_07(self):#单个删除
    #     xzlb.zclbgl_dgsc()

    def test_xzlb_08(self):#正常录入流程记录
        xzlb.zclbgl_lrlcjl()

    def test_xzlb_09(self):# 不正常录入流程记录
        xzlb.zclbgl_lrlcjlfalse()

    def test_xzlb_10(self): # 流程记录管理搜索
        xzlb.zclbgl_lrlcjlsousuo()


    def test_xzlb_11(self): # 流程记录管理编辑自己添加的记录
        xzlb.zclbgl_lcjlglbjzjtj()

    def test_xzlb_12(self):# 流程记录管理删除已选
        xzlb.zclbgl_lcjlglscyx()

    def test_xzlb_13(self): # 流程记录管理删除自己添加的记录
        xzlb.zclbgl_lcjlglsczjtj()
        x = denglu.driver.find_element_by_xpath('/html/body/div[3]/div').text
        y = '批量删除成功！'
        denglu.driver.assertEqual(x, y, msg='失败')
        time.sleep(3)

    # def test_xzlb_14(self): # 流程记录管理删除所有
    #     xzlb.zclbgl_lcjlglscsy()
        # x=denglu.driver.find_element_by_xpath('/html/body/div[3]/div').text
        # y='批量删除成功！'
        # denglu.driver.assertEqual(x, y, msg='失败')
        time.sleep(3)
    # @classmethod
    # def tearDownClass(cls):
    #         denglu.driver.quit()


if __name__ == '__main__':
        unittest.main()