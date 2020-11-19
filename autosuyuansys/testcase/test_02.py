from common import login1
import time
import unittest

DL = login1.Test_Denglu()
from selenium.webdriver.support.select import Select


class SYGL():
    def syslgl_xzsysl(self):  # 正常新增溯源实例
        time.sleep(3)

        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text('新增溯源实例').click()
        DL.driver.find_element_by_name('name').click()
        DL.driver.find_element_by_name('name').send_keys('寇旭珂')
        DL.driver.switch_to.frame(0)
        DL.driver.find_element_by_css_selector("html").click()
        DL.driver.find_element_by_css_selector("html").send_keys('123')
        DL.driver.switch_to_default_content()
        DL.driver.find_element_by_css_selector(".btn").click()
        # x=DL.driver.find_element_by_css_selector('.layui-layer-content').text
        # y='批量删除成功！'
        # if(x!=y):
        #     print('失败')
        time.sleep(5)


    def syslgl_bzcxzsysl(self):  # 不正常新增溯源实例
        time.sleep(3)

        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text('新增溯源实例').click()
        DL.driver.find_element_by_name('name').click()
        DL.driver.find_element_by_name('name').send_keys(
            '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222333333333333333333333333333333333333333333333333333333333333334444444444444444444444444444444444444444444444444444444444444444456666666666666666666666666666666666666666666666666666666666666656666666666666666666666666666666666666666666666666666666666666666666')
        DL.driver.switch_to.frame(0)
        DL.driver.find_element_by_css_selector("html").click()
        DL.driver.find_element_by_css_selector("html").send_keys('123')
        DL.driver.switch_to_default_content()
        DL.driver.find_element_by_css_selector(".btn").click()
        # x=DL.driver.find_element_by_css_selector('.layui-layer-content').text
        # y='批量删除成功！'
        # if(x!=y):
        #     print('失败')
        time.sleep(5)


    def syslgl_syslzcss(self):  # 溯源实例正常搜索
        time.sleep(3)
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) li:nth-child(2) > a").click()
        DL.driver.find_element_by_id('key').click()
        DL.driver.find_element_by_id('key').send_keys('寇旭珂')
        DL.driver.find_element_by_css_selector('.btn-success').click()
        time.sleep(5)

    def syslgl_syslbzcss(self):  # 溯源实例不正常搜索
        time.sleep(3)
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) li:nth-child(2) > a").click()
        DL.driver.find_element_by_id('key').click()
        DL.driver.find_element_by_id('key').send_keys('123456789123456789')
        DL.driver.find_element_by_css_selector('.btn-success').click()
        time.sleep(5)

    def syslgl_syslbjzjtj(self):  # 溯源实例编辑自己添加的记录
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) li:nth-child(2) > a").click()
        DL.driver.find_element_by_link_text('编辑').click()
        DL.driver.find_element_by_name('name').click()
        DL.driver.find_element_by_name('name').send_keys('寇')
        DL.driver.switch_to.frame(0)
        DL.driver.find_element_by_css_selector("html").click()
        DL.driver.find_element_by_css_selector("html").send_keys('123')
        DL.driver.switch_to_default_content()
        DL.driver.find_element_by_css_selector(".btn").click()
        time.sleep(1)


    def syslgl_syslcknr(self):  # 溯源实例管理查看内容预览
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) li:nth-child(2) > a").click()
        DL.driver.find_element_by_css_selector("tr:nth-child(1) > td:nth-child(4) > .ew80_ontext").click()
        DL.driver.find_element_by_css_selector('.layui-layer-ico').click()
        time.sleep(1)


    def syslgl_syslscyx(self):  # 溯源实例删除已选
        time.sleep(3)
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) li:nth-child(2) > a").click()
        target_elem = DL.driver.find_element_by_id('del')
        DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        DL.driver.find_element_by_css_selector('#chk\\[\\]').click()
        DL.driver.find_element_by_id('del').click()
        alert = DL.driver.switch_to_alert()
        time.sleep(2)
        print(alert.text)
        alert.accept()
        # n
        # x=DL.driver.find_element_by_css_selector('.layui-layer-content').text
        # y='批量删除成功！'
        # if(x!=y):
        #     print('失败')
        time.sleep(5)


    def syslgl_syslscsy(self):  # 溯源实例删除所有
        time.sleep(3)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) li:nth-child(2) > a").click()
        target_elem = DL.driver.find_element_by_id('del')
        DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        DL.driver.find_element_by_css_selector('#chkAll').click()
        DL.driver.find_element_by_id('del').click()
        alert = DL.driver.switch_to.alert
        time.sleep(2)
        print(alert.text)
        alert.accept()
        time.sleep(3)
        alert = DL.driver.switch_to.alert
        time.sleep(2)
        print(alert.text)
        alert.accept()
        # x=DL.driver.find_element_by_css_selector('.layui-layer-content').text
        # y='批量删除成功！'
        # if(x!=y):
        #     print('失败')
        time.sleep(5)


    def syslgl_syslsczjtj(self):  # 溯源实例删除自己添加的
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) li:nth-child(2) > a").click()

        DL.driver.find_element_by_css_selector("tr:nth-child(1) .label-danger").click()
        DL.driver.find_element_by_link_text('确认').click()
        #     # x=DL.driver.find_element_by_css_selector('.layui-layer-content').text
        #     # y='批量删除成功！'
        #     # if(x!=y):
        #     #     print('失败')
        #
        time.sleep(5)

    def syslgl_plsyczawlm(self):  # 批量溯源操作按物流码操作
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text('批量溯源操作').click()
        DL.driver.find_element_by_id('txm').click()
        DL.driver.find_element_by_id('txm').send_keys('53355')
        DL.driver.execute_script("document.getElementById('s001').style.display='block';")
        Select(DL.driver.find_element_by_id('s001')).select_by_visible_text("ASD")
        DL.driver.find_element_by_name('Submit').click()
        time.sleep(1)


    def syslgl_plsyczaid(self):  # 批量溯源操作按防伪ID操作
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text('批量溯源操作').click()
        DL.driver.find_element_by_css_selector('div.col-sm-2:nth-child(2) > input:nth-child(1)').send_keys('0')
        DL.driver.find_element_by_css_selector('div.col-sm-2:nth-child(3) > input:nth-child(1)').send_keys('100')
        DL.driver.execute_script("document.getElementById('s00').style.display='block';")
        Select(DL.driver.find_element_by_id('s00')).select_by_visible_text("阿尔泰送人头新用户")
        DL.driver.find_element_by_name('Submit').click()
        time.sleep(2)


    def syslgl_plsyczafwm(self):  # 批量溯源操作按防伪码操作
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text('批量溯源操作').click()
        time.sleep(2)
        target_elem = DL.driver.find_element_by_css_selector('div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)')
        DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        time.sleep(2)
        DL.driver.execute_script("document.getElementById('s1').style.display='block';")
        Select(DL.driver.find_element_by_id('s1')).select_by_visible_text("202010121")
        time.sleep(1)
        DL.driver.execute_script("document.getElementById('s01').style.display='block';")
        Select(DL.driver.find_element_by_id('s01')).select_by_visible_text("ASD")
        time.sleep(1)
        DL.driver.find_element_by_css_selector(
            'div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)').click()
        time.sleep(1)


    def syslgl_plsyczacpmc(self):  # 批量溯源操作按产品名称操作
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text('批量溯源操作').click()
        time.sleep(2)
        target_elem = DL.driver.find_element_by_css_selector('div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)')
        DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        time.sleep(2)
        DL.driver.execute_script("document.getElementById('cp').style.display='block';")
        Select(DL.driver.find_element_by_id('cp')).select_by_visible_text("1212")
        time.sleep(1)
        DL.driver.execute_script("document.getElementById('s03').style.display='block';")
        Select(DL.driver.find_element_by_id('s03')).select_by_visible_text("ASD")
        time.sleep(1)
        DL.driver.find_element_by_css_selector(
            'div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)').click()
        time.sleep(1)


    def syslgl_plsyczascrq(self):  # 批量溯源操作按生成日期操作
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text('批量溯源操作').click()
        time.sleep(2)
        target_elem = DL.driver.find_element_by_css_selector(
            'div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)')
        DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        time.sleep(2)
        DL.driver.execute_script("document.getElementById('s5').style.display='block';")
        Select(DL.driver.find_element_by_id('s5')).select_by_visible_text("2020-10-23")
        time.sleep(1)
        DL.driver.execute_script("document.getElementById('s04').style.display='block';")
        Select(DL.driver.find_element_by_id('s04')).select_by_visible_text("品质")
        time.sleep(1)
        DL.driver.find_element_by_css_selector(
            'div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)').click()
        time.sleep(1)


    def syslgl_cwplsyczawlm(self):  # 错误批量溯源操作按物流码操作
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text('批量溯源操作').click()
        DL.driver.find_element_by_id('txm').click()
        DL.driver.find_element_by_id('txm').send_keys('5335564654564156415415641541564151565')
        DL.driver.execute_script("document.getElementById('s001').style.display='block';")

        Select(DL.driver.find_element_by_id('s001')).select_by_visible_text("ASD")
        DL.driver.find_element_by_name('Submit').click()
        time.sleep(1)


    def syslgl_cwplsyczaid(self):  # 错误批量溯源操作按防伪ID操作
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text('批量溯源操作').click()
        DL.driver.find_element_by_css_selector('div.col-sm-2:nth-child(2) > input:nth-child(1)').send_keys(
            '9999999999999999999999999999999999999999999999')
        DL.driver.find_element_by_css_selector('div.col-sm-2:nth-child(3) > input:nth-child(1)').send_keys(
            '100999999999999999999999999999999999999999999999')
        DL.driver.execute_script("document.getElementById('s00').style.display='block';")
        Select(DL.driver.find_element_by_id('s00')).select_by_visible_text("ASD")
        DL.driver.find_element_by_css_selector(
            'div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)').click()
        time.sleep(1)


    def syslgl_syczzcss(self):  # 溯源操作记录正常搜索
        time.sleep(3)
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text('溯源操作记录').click()

        DL.driver.find_element_by_css_selector('#key').click()
        DL.driver.find_element_by_css_selector('#key').send_keys('寇旭珂')
        DL.driver.find_element_by_css_selector('button.btn:nth-child(2)').click()
        time.sleep(3)


    def syslgl_syczqbsc(self):  # 溯源操作记录全部删除
        time.sleep(3)
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text('溯源操作记录').click()

        target_elem = DL.driver.find_element_by_css_selector('#del')
        DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        DL.driver.find_element_by_css_selector('#chkAll').click()
        DL.driver.find_element_by_css_selector('#del').click()
        alert = DL.driver.switch_to_alert()
        time.sleep(2)
        print(alert.text)
        alert.accept()
        time.sleep(3)
        alert = DL.driver.switch_to_alert()
        time.sleep(2)
        print(alert.text)
        alert.accept()
        time.sleep(1)


    def syslgl_syczxzsc(self):  # 溯源操作记录选择删除
        time.sleep(3)
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text('溯源操作记录').click()

        target_elem = DL.driver.find_element_by_css_selector('#del')
        DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        DL.driver.find_element_by_css_selector(
            '.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)').click()
        DL.driver.find_element_by_css_selector('#del').click()
        alert = DL.driver.switch_to.alert
        time.sleep(2)
        print(alert.text)
        alert.accept()
        time.sleep(3)
        alert = DL.driver.switch_to.alert
        time.sleep(2)
        print(alert.text)
        alert.accept()
        time.sleep(1)


    def syslgl_syczansc(self):  # 溯源操作记录单条按钮删除
        time.sleep(3)
        # DL.driver.find_element_by_css_selector(".sub-menu:nth-child(4) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text('溯源操作记录').click()
        # DL.driver.find_element_by_css_selector("li.active > a:nth-child(1)").click()
        DL.driver.find_element_by_css_selector(
            '.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > span:nth-child(1)').click()
        DL.driver.find_element_by_css_selector('.layui-layer-btn0').click()
        time.sleep(1)
