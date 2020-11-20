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
        x=denglu.driver.find_element_by_css_selector('#top_menu > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').text
        # y='前台浏览'
        self.assertTrue(x)
    def test_xzlb_15(self):#新增溯源管理
        xzsy.syslgl_xzsysl()

    def test_xzlb_16(self): # 不正常新增溯源实例
        xzsy.syslgl_bzcxzsysl()

    def test_xzlb_17(self): # 溯源实例正常搜索
         xzsy.syslgl_syslzcss()

    def test_xzlb_18(self):#溯源实例不正常搜索
         xzsy.syslgl_syslbzcss()

    def test_xzlb_19(self):  # 溯源选择编辑自己添加的
            xzsy.syslgl_syslbjzjtj()
            x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
            self.assertTrue(x,msg='失败')

    def test_xzlb_20(self):  # 溯源实例管理查看
        xzsy.syslgl_syslcknr()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-title').text
        y='预览'
        self.assertEqual(x,y, msg='失败')

    def test_xzlb_21(self):  # 溯源选择删除
        xzsy.syslgl_syslscyx()

    def test_xzlb_22(self):  # 溯源选择删除自己添加的
        xzsy.syslgl_syslsczjtj()

    def test_xzlb_23(self):  # 溯源选择删除所以
        xzsy.syslgl_syslscsy()

    def test_xzlb_24(self):  # 溯源批量操作按物流码
        xzsy.syslgl_plsyczawlm()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x,msg='失败')

    def test_xzlb_25(self):  # 溯源批量操作按防伪ID
        xzsy.syslgl_plsyczaid()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')#失败
        self.assertTrue(x, msg='失败')
        time.sleep(5)

    def test_xzlb_26(self):  # 溯源批量操作按产品名称
        xzsy.syslgl_plsyczacpmc()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')#失败
        self.assertTrue(x, msg='失败')
        time.sleep(5)

    def test_xzlb_27(self):  # 溯源批量操作按产品名称
        xzsy.syslgl_plsyczascrq()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')  # 失败
        self.assertTrue(x, msg='失败')
        time.sleep(5)

    def test_xzlb_28(self):  # 溯源批量操作按产品名称
        xzsy.syslgl_cwplsyczawlm()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')  # 失败
        self.assertTrue(x, msg='失败')
        time.sleep(5)

    def test_xzlb_29(self):  # 溯源批量操作按防伪ID
        xzsy.syslgl_cwplsyczaid()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')#失败
        self.assertTrue(x, msg='失败')
        time.sleep(5)

    def test_xzlb_30(self):  # 溯源操作记录正常搜索
        xzsy.syslgl_syczzcss()
        x = denglu.driver.find_element_by_css_selector('.table > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2) > p:nth-child(4) > span:nth-child(1)').text  # 失败
        y='寇旭珂'
        self.assertEqual(x,y,msg='失败')
    #     time.sleep(5)

    def test_xzlb_31(self):  # 溯源操作记录全部删除
         xzsy.syslgl_syczqbsc()

    def test_xzlb_32(self):  # 溯源操作记录选择删除
         xzsy.syslgl_syczxzsc()

    def test_xzlb_33(self):  # 溯源操作记录单条按钮删除
            xzsy.syslgl_syczansc()
            x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
            self.assertTrue(x, msg='失败')

    @classmethod
    def tearDownClass(cls):
        denglu.driver.quit()


if __name__ == '__main__':
    unittest.main()