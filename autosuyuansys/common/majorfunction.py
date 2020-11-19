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
        # # y='前台浏览'
        # self.assertTrue(x)

        # def test_xzlb_01(self):#新增流程类别
        #
        #     xzlb.xzlclb()
        #
        # def test_xzlb_02(self):#新增流程类别反案例流程类别名有重复
        #
        #     xzlb.xzlclb_FAN()
        #
        # def test_xzlb_03(self):#流程增添已禁用
        #
        #     xzlb.xzlclb_lczt()
        #
        # def test_xzlb_04(self):#搜索
        #
        #     xzlb.zclbgl_sousuo()
        #
        # def test_xzlb_05(self):#编辑
        #
        #     xzlb.zclbgl_bianji()
        #
        # def test_xzlb_06(self):#批量删除
        #     xzlb.zclbgl_plsc()
        #
        # def test_xzlb_07(self):#单个删除
        #     xzlb.zclbgl_dgsc()
        #
        # def test_xzlb_08(self):#正常录入流程记录
        #     xzlb.zclbgl_lrlcjl()
        #
        # def test_xzlb_09(self):# 不正常录入流程记录
        #     xzlb.zclbgl_lrlcjlfalse()
        #
        # def test_xzlb_10(self): # 流程记录管理搜索
        #     xzlb.zclbgl_lrlcjlsousuo()
        #
        #
        # def test_xzlb_11(self): # 流程记录管理编辑自己添加的记录
        #     xzlb.zclbgl_lcjlglbjzjtj()
        #
        # def test_xzlb_12(self):# 流程记录管理删除已选
        #     xzlb.zclbgl_lcjlglscyx()
        #
        # def test_xzlb_13(self): # 流程记录管理删除自己添加的记录
        #     xzlb.zclbgl_lcjlglsczjtj()
        #     x = denglu.driver.find_element_by_xpath('/html/body/div[3]/div').text
        #     y = '批量删除成功！'
        #     denglu.driver.assertEqual(x, y, msg='失败')
        #     time.sleep(3)
        #
        # def test_xzlb_14(self): # 流程记录管理删除所有
        #     xzlb.zclbgl_lcjlglscsy()
        #     # x=denglu.driver.find_element_by_xpath('/html/body/div[3]/div').text
        #     # y='批量删除成功！'
        #     # denglu.driver.assertEqual(x, y, msg='失败')
        #     time.sleep(3)
        # def test_xzlb_15(self):#新增溯源管理
        #     xzsy.syslgl_xzsysl()
        #
        # def test_xzlb_16(self): # 不正常新增溯源实例
        #     xzsy.syslgl_bzcxzsysl()
        #
        # def test_xzlb_17(self): # 溯源实例正常搜索
        #      xzsy.syslgl_syslzcss()
        #
        # def test_xzlb_18(self):#溯源实例不正常搜索
        #      xzsy.syslgl_syslbzcss()
        #
        # def test_xzlb_19(self):  # 溯源选择编辑自己添加的
        #         xzsy.syslgl_syslbjzjtj()
        #         x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        #         self.assertTrue(x,msg='失败')
        #
        # def test_xzlb_20(self):  # 溯源实例管理查看
        #     xzsy.syslgl_syslcknr()
        #     x = denglu.driver.find_element_by_css_selector('.layui-layer-title').text
        #     y='预览'
        #     self.assertEqual(x,y, msg='失败')
        #
        # def test_xzlb_21(self):  # 溯源选择删除
        #     xzsy.syslgl_syslscyx()
        #
        # def test_xzlb_22(self):  # 溯源选择删除自己添加的
        #     xzsy.syslgl_syslsczjtj()
        #
        # def test_xzlb_23(self):  # 溯源选择删除所以
        #     xzsy.syslgl_syslscsy()
        #
        # def test_xzlb_24(self):  # 溯源批量操作按物流码
        #     xzsy.syslgl_plsyczawlm()
        #     x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        #     self.assertTrue(x,msg='失败')
        #
        # def test_xzlb_25(self):  # 溯源批量操作按防伪ID
        #     xzsy.syslgl_plsyczaid()
        #     x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')#失败
        #     self.assertTrue(x, msg='失败')
        #     time.sleep(5)
        #
        # def test_xzlb_26(self):  # 溯源批量操作按产品名称
        #     xzsy.syslgl_plsyczacpmc()
        #     x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')#失败
        #     self.assertTrue(x, msg='失败')
        #     time.sleep(5)
        #
        # def test_xzlb_27(self):  # 溯源批量操作按产品名称
        #     xzsy.syslgl_plsyczascrq()
        #     x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')  # 失败
        #     self.assertTrue(x, msg='失败')
        #     time.sleep(5)
        #
        # def test_xzlb_28(self):  # 溯源批量操作按产品名称
        #     xzsy.syslgl_cwplsyczawlm()
        #     x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')  # 失败
        #     self.assertTrue(x, msg='失败')
        #     time.sleep(5)
        #
        # def test_xzlb_29(self):  # 溯源批量操作按防伪ID
        #     xzsy.syslgl_cwplsyczaid()
        #     x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')#失败
        #     self.assertTrue(x, msg='失败')
        #     time.sleep(5)
        #
        # def test_xzlb_30(self):  # 溯源操作记录正常搜索
        #     xzsy.syslgl_syczzcss()
        #     x = denglu.driver.find_element_by_css_selector('.table > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2) > p:nth-child(4) > span:nth-child(1)').text  # 失败
        #     y='寇旭珂'
        #     self.assertEqual(x,y,msg='失败')
        # #     time.sleep(5)
        #
        # def test_xzlb_31(self):  # 溯源操作记录全部删除
        #      xzsy.syslgl_syczqbsc()
        #
        # def test_xzlb_32(self):  # 溯源操作记录选择删除
        #      xzsy.syslgl_syczxzsc()
        #
        # def test_xzlb_33(self):  # 溯源操作记录单条按钮删除
        #         xzsy.syslgl_syczansc()
        #         x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        #         self.assertTrue(x, msg='失败')

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
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

    def test_xzlb_46(self):  # 按批次批量删除防伪码
        fwm.fwmgl_apcplscfwm()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

    def test_xzlb_47(self):  # 按产品名批量删除防伪码
        fwm.fwmgl_acpmplscfwm()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

    def test_xzlb_48(self):  # 按产品名批量删除防伪码
        fwm.fwmgl_ascrqplscfwm()
        x = denglu.driver.find_element_by_css_selector('.layui-layer-ico')
        self.assertTrue(x, msg='失败')

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