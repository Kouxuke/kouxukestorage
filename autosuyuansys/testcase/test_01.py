from common import login1
import time
import unittest
DL = login1.Test_Denglu()
from selenium.webdriver.support.select import Select


class XZCP():
    def xzlclb(self):#新增流程类别
        time.sleep(3)
        DL.driver.find_element_by_link_text('流程记录管理').click()
        DL.driver.find_element_by_css_selector(
            'li.sub-menu:nth-child(3) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()
        DL.driver.find_element_by_css_selector('.col-sm-4 > input:nth-child(1)').send_keys('樱桃分拣111')
        DL.driver.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('100')
        DL.driver.find_element_by_css_selector('.btn').click()
        time.sleep(3)

    def xzlclb_FAN(self):#新增流程类别反案例流程类别名有重复
        time.sleep(3)
        # DL.driver.find_element_by_link_text('流程记录管理').click()
        DL.driver.find_element_by_css_selector(
            'li.sub-menu:nth-child(3) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()
        DL.driver.find_element_by_css_selector('.col-sm-4 > input:nth-child(1)').send_keys('樱桃分拣3')
        DL.driver.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('100')
        DL.driver.find_element_by_css_selector('.btn').click()

        # x = DL.driver.find_element_by_link_text('流程类别名有重复!').text
        # y = "流程类别名有重复!"
        # DL.driver.assertEqual(x, y, msg='失败')
        time.sleep(3)

    def xzlclb_lczt(self):#流程增添已禁用
        # DL.driver.find_element_by_link_text('流程记录管理').click()
        DL.driver.find_element_by_css_selector(
            'li.sub-menu:nth-child(3) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()
        DL.driver.find_element_by_css_selector('.col-sm-4 > input:nth-child(1)').send_keys('樱桃分拣6')
        DL.driver.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('101540')
        DL.driver.find_element_by_id("zt").click()
        dropdown = DL.driver.find_element_by_id("zt")
        dropdown.find_element_by_xpath("//option[. = '禁用']").click()
        DL.driver.find_element_by_css_selector('.btn').click()
        DL.driver.find_element_by_link_text('流程类别管理').click()
        # x= DL.driver.find_element_by_link_text(' 已禁用').text
        # y='已禁用'
        # DL.driver.assertEqual(x, y, msg='失败')
        time.sleep(3)

    def zclbgl_sousuo(self):#搜索
        time.sleep(3)
        # DL.driver.find_element_by_link_text('流程记录管理').click()
        DL.driver.find_element_by_link_text('流程类别管理').click()
        DL.driver.find_element_by_css_selector('.form-control').send_keys('樱桃分拣6')
        DL.driver.find_element_by_css_selector('button.btn:nth-child(2)').click()
        # x=DL.driver.find_element_by_link_text('樱桃分拣6').text
        # y='樱桃分拣6'
        # if(x==y):
        #     print("成功")
        time.sleep(5)

    def zclbgl_bianji(self):#编辑
        time.sleep(3)
        # DL.driver.find_element_by_link_text('流程记录管理').click()
        DL.driver.find_element_by_link_text('流程类别管理').click()
        DL.driver.find_element_by_css_selector('.table > tbody:nth-child(2) > tr:nth-child(7) > td:nth-child(7) > a:nth-child(1)').click()
        DL.driver.find_element_by_name('lcname').click()
        DL.driver.find_element_by_name('lcname').send_keys('koukuokuokuo')
        DL.driver.find_element_by_css_selector('.btn').click()

        time.sleep(3)
    def zclbgl_plsc(self):#批量删除
        time.sleep(3)
        # DL.driver.find_element_by_link_text('流程记录管理').click()
        DL.driver.find_element_by_link_text('流程类别管理').click()
        DL.driver.find_element_by_id('chkAll').click()
        DL.driver.find_element_by_id('del').click()
        alert = DL.driver.switch_to.alert
        time.sleep(2)
        print(alert.text)
        alert.accept()
        time.sleep(2)
        alert = DL.driver.switch_to.alert
        time.sleep(2)
        print(alert.text)
        alert.accept()
        time.sleep(3)

    def zclbgl_dgsc(self):#单个删除
        time.sleep(3)
        # DL.driver.find_element_by_link_text('流程记录管理').click()
        DL.driver.find_element_by_link_text('流程类别管理').click()
        DL.driver.find_element_by_css_selector('.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > span:nth-child(2)').click()
        DL.driver.find_element_by_link_text('确认').click()
        # x=DL.driver.find_element_by_css_selector('.layui-layer-content').text
        # y='删除成功！'
        # if(x!=y):
        #     print('失败')
        time.sleep(3)
    def zclbgl_lrlcjl(self):#正常录入流程记录
        time.sleep(3)
        # DL.driver.find_element_by_link_text('流程记录管理').click()
        DL.driver.find_element_by_link_text('录入流程记录').click()
        DL.driver.find_element_by_css_selector('.searchable-select-holder').click()
        DL.driver.find_element_by_css_selector('div.searchable-select-item:nth-child(4)').click()
        DL.driver.find_element_by_name('txm').send_keys('53355')
        DL.driver.find_element_by_name('zrr').send_keys('寇旭珂')
        DL.driver.find_element_by_name('Submit').click()
        # x=DL.driver.find_element_by_css_selector('.layui-layer-content').text
        # y='操作成功！'
        # if(x!=y):
        #     print('失败')
        time.sleep(5)

    def zclbgl_lrlcjlfalse(self):  # 不正常录入流程记录
        time.sleep(3)
        # DL.driver.find_element_by_link_text('流程记录管理').click()
        DL.driver.find_element_by_link_text('录入流程记录').click()
        DL.driver.find_element_by_css_selector('.searchable-select-holder').click()
        DL.driver.find_element_by_css_selector('div.searchable-select-item:nth-child(4)').click()
        DL.driver.find_element_by_name('txm').send_keys('32154521553355')
        DL.driver.find_element_by_name('zrr').send_keys('寇旭珂')
        DL.driver.find_element_by_name('Submit').click()
        # x = DL.driver.find_element_by_css_selector('.layui-layer-content').text
        # y = '物流码不存在'
        # if (x != y):
        #     print('失败')
        time.sleep(3)

    def zclbgl_lrlcjlsousuo(self):  # 流程记录管理搜索
        time.sleep(3)
        # DL.driver.find_element_by_link_text('流程记录管理').click()
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) li:nth-child(4) > a").click()

        DL.driver.find_element_by_name('txm').click()
        DL.driver.find_element_by_name('txm').send_keys('53355')
        DL.driver.find_element_by_css_selector('.btn-success').click()
        time.sleep(3)

    def zclbgl_lcjlglscyx(self):  # 流程记录管理删除已选
        time.sleep(3)
        # DL.driver.find_element_by_link_text('流程记录管理').click()
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) li:nth-child(4) > a").click()
        target_elem = DL.driver.find_element_by_id('del')
        DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        DL.driver.find_element_by_css_selector('#chk\[\]').click()
        DL.driver.find_element_by_id('del').click()
        alert = DL.driver.switch_to.alert
        time.sleep(2)
        print(alert.text)
        alert.accept()
        # x=DL.driver.find_element_by_css_selector('.layui-layer-content').text
        # y='批量删除成功！'
        # if(x!=y):
        #     print('失败')

        time.sleep(5)

    def zclbgl_lcjlglscsy(self):  # 流程记录管理删除所有
        time.sleep(3)
        # DL.driver.find_element_by_link_text('流程记录管理').click()
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) li:nth-child(4) > a").click()
        target_elem = DL.driver.find_element_by_id('del')
        DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        DL.driver.find_element_by_css_selector('#chkAll').click()
        DL.driver.find_element_by_id('del').click()
        alert = DL.driver.switch_to.alert
        time.sleep(2)
        print(alert.text)
        alert.accept()
        # x=DL.driver.find_element_by_css_selector('.layui-layer-content').text
        # y='批量删除成功！'
        # if(x!=y):
        #     print('失败')

        # time.sleep(5)

    def zclbgl_lcjlglsczjtj(self):  # 流程记录管理删除自己添加的记录
        time.sleep(3)
        # DL.driver.find_element_by_link_text('流程记录管理').click()
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) li:nth-child(4) > a").click()
        time.sleep(3)
        DL.driver.find_element_by_css_selector("tr:nth-child(1) .label-danger").click()
        DL.driver.find_element_by_link_text('确认').click()
        # x=DL.driver.find_element_by_css_selector('.layui-layer-content').text
        # y='批量删除成功！'
        # if(x!=y):
        #     print('失败')

        time.sleep(5)

    def zclbgl_lcjlglbjzjtj(self):  # 流程记录管理编辑自己添加的记录
        time.sleep(3)
        # DL.driver.find_element_by_link_text('流程记录管理').click()
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) li:nth-child(4) > a").click()
        time.sleep(3)
        DL.driver.find_element_by_css_selector("tr:nth-child(5) .label-success").click()
        DL.driver.find_element_by_css_selector(".searchable-select-holder").click()
        DL.driver.find_element_by_css_selector(".hover").click()
        DL.driver.find_element_by_name('zrr').click()
        DL.driver.find_element_by_name('zrr').send_keys('123')
        DL.driver.find_element_by_css_selector(".btn").click()
        # x=DL.driver.find_element_by_css_selector('.layui-layer-content').text
        # y='批量删除成功！'
        # if(x!=y):
        #     print('失败')

        time.sleep(5)
