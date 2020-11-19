from common import login1
import time
import unittest

DL = login1.Test_Denglu()
from selenium.webdriver.support.select import Select


class FWM():


        def fwmgl_plscfwm(self):  #  正常批量生成防伪码
            time.sleep(3)
            DL.driver.find_element_by_css_selector(
                "li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量生成防伪码').click()
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)").clear()
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys('kou123456789')
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").clear()
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys('13')
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)").send_keys('kou1')
            Select(DL.driver.find_element_by_id('code_type')).select_by_visible_text("前缀+数字和字母")
            Select(DL.driver.find_element_by_id('txm_type')).select_by_visible_text("纯数字")
            DL.driver.find_element_by_css_selector("div.col-sm-2:nth-child(4) > input:nth-child(1)").clear()
            DL.driver.find_element_by_css_selector("div.col-sm-2:nth-child(4) > input:nth-child(1)").send_keys('8')
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(6) > div:nth-child(2) > input:nth-child(1)").send_keys('1')
            DL.driver.execute_script("document.getElementById('s1').style.display='block';")
            Select(DL.driver.find_element_by_id('s1')).select_by_visible_text("寇旭珂")
            DL.driver.execute_script("document.getElementById('s2').style.display='block';")
            Select(DL.driver.find_element_by_id('s2')).select_by_visible_text("口扩扩")
            DL.driver.execute_script("document.getElementById('qiyong').style.display='block';")
            Select(DL.driver.find_element_by_id('qiyong')).select_by_visible_text("启用")
            DL.driver.find_element_by_css_selector("#tj").click()
            time.sleep(1)

        def fwmgl_plscfwm2(self):  #  防伪码长度为7位前缀为五位正常批量生成防伪码
            # DL.driver.find_element_by_css_selector(
            #     "li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量生成防伪码').click()
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)").clear()
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys('kou123456789')
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").clear()
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys('7')
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)").send_keys('kouxu')
            DL.driver.execute_script("document.getElementById('code_type').style.display='block';")
            Select(DL.driver.find_element_by_id('code_type')).select_by_visible_text("前缀+数字和字母")
            DL.driver.execute_script("document.getElementById('txm_type').style.display='block';")
            Select(DL.driver.find_element_by_id('txm_type')).select_by_visible_text("纯数字")
            DL.driver.find_element_by_css_selector("div.col-sm-2:nth-child(4) > input:nth-child(1)").clear()
            DL.driver.find_element_by_css_selector("div.col-sm-2:nth-child(4) > input:nth-child(1)").send_keys('8')
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(6) > div:nth-child(2) > input:nth-child(1)").send_keys('1')
            DL.driver.execute_script("document.getElementById('s1').style.display='block';")
            Select(DL.driver.find_element_by_id('s1')).select_by_visible_text("寇旭珂")
            DL.driver.execute_script("document.getElementById('s2').style.display='block';")
            Select(DL.driver.find_element_by_id('s2')).select_by_visible_text("口扩扩")
            DL.driver.execute_script("document.getElementById('qiyong').style.display='block';")
            Select(DL.driver.find_element_by_id('qiyong')).select_by_visible_text("启用")
            DL.driver.find_element_by_css_selector("#tj").click()
            time.sleep(1)

        def fwmgl_plscfwm3(self):  # 防伪码长度为13位前缀为1位正常批量生成防伪码
            # DL.driver.find_element_by_css_selector(
            #     "li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量生成防伪码').click()
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)").clear()
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys('kou123456789')
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").clear()
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys('13')
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)").send_keys('k')
            DL.driver.execute_script("document.getElementById('code_type').style.display='block';")
            Select(DL.driver.find_element_by_id('code_type')).select_by_visible_text("前缀+数字和字母")
            DL.driver.execute_script("document.getElementById('txm_type').style.display='block';")
            Select(DL.driver.find_element_by_id('txm_type')).select_by_visible_text("纯数字")
            DL.driver.find_element_by_css_selector("div.col-sm-2:nth-child(4) > input:nth-child(1)").clear()
            DL.driver.find_element_by_css_selector("div.col-sm-2:nth-child(4) > input:nth-child(1)").send_keys('8')
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(6) > div:nth-child(2) > input:nth-child(1)").send_keys('1')
            DL.driver.execute_script("document.getElementById('s1').style.display='block';")
            Select(DL.driver.find_element_by_id('s1')).select_by_visible_text("寇旭珂")
            DL.driver.execute_script("document.getElementById('s2').style.display='block';")
            Select(DL.driver.find_element_by_id('s2')).select_by_visible_text("口扩扩")
            DL.driver.execute_script("document.getElementById('qiyong').style.display='block';")
            Select(DL.driver.find_element_by_id('qiyong')).select_by_visible_text("启用")
            DL.driver.find_element_by_css_selector("#tj").click()
            time.sleep(1)
        def fwmgl_plscfwm4(self):  # 防伪码功能为禁用正常批量生成防伪码
            # DL.driver.find_element_by_css_selector(
            #     "li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量生成防伪码').click()
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)").clear()
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys('kou123456789')
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").clear()
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys('8')
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)").send_keys('kou')
            DL.driver.execute_script("document.getElementById('code_type').style.display='block';")
            Select(DL.driver.find_element_by_id('code_type')).select_by_visible_text("前缀+数字和字母")
            DL.driver.execute_script("document.getElementById('txm_type').style.display='block';")
            Select(DL.driver.find_element_by_id('txm_type')).select_by_visible_text("纯数字")
            DL.driver.find_element_by_css_selector("div.col-sm-2:nth-child(4) > input:nth-child(1)").clear()
            DL.driver.find_element_by_css_selector("div.col-sm-2:nth-child(4) > input:nth-child(1)").send_keys('8')
            DL.driver.find_element_by_css_selector(
                "div.form-group:nth-child(6) > div:nth-child(2) > input:nth-child(1)").send_keys('1')
            DL.driver.execute_script("document.getElementById('s1').style.display='block';")
            Select(DL.driver.find_element_by_id('s1')).select_by_visible_text("寇旭珂")
            DL.driver.execute_script("document.getElementById('s2').style.display='block';")
            Select(DL.driver.find_element_by_id('s2')).select_by_visible_text("口扩扩")
            DL.driver.execute_script("document.getElementById('qiyong').style.display='block';")
            Select(DL.driver.find_element_by_id('qiyong')).select_by_visible_text("不启用")
            DL.driver.find_element_by_css_selector("#tj").click()
            time.sleep(3)
        def fwmgl_dgscfwm(self):  #  正常单个生成防伪码
            time.sleep(3)
            # DL.driver.find_element_by_css_selector("li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('单个生成防伪码').click()
            DL.driver.find_element_by_css_selector(".col-sm-3 > input:nth-child(1)").clear()
            DL.driver.find_element_by_css_selector(".col-sm-3 > input:nth-child(1)").send_keys('kou123456789')
            DL.driver.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').clear()
            DL.driver.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('kou123456789')
            DL.driver.find_element_by_css_selector("div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)").clear()
            DL.driver.find_element_by_css_selector("div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)").send_keys('123456789')
            DL.driver.execute_script("document.getElementById('s1').style.display='block';")
            Select(DL.driver.find_element_by_id('s1')).select_by_visible_text("寇旭珂")
            DL.driver.execute_script("document.getElementById('s2').style.display='block';")
            Select(DL.driver.find_element_by_id('s2')).select_by_visible_text("口扩扩")
            DL.driver.execute_script("document.getElementById('qiyong').style.display='block';")
            Select(DL.driver.find_element_by_id('qiyong')).select_by_visible_text("启用")
            DL.driver.find_element_by_css_selector(".btn").click()
            time.sleep(1)

        def fwmgl_awlmplxgfwm(self):  # 按物流码批量修改防伪码
            time.sleep(3)
            # DL.driver.find_element_by_css_selector(
            #     "li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量修改防伪码').click()
            DL.driver.find_element_by_css_selector("#txm").send_keys('123456789')
            DL.driver.execute_script("document.getElementById('s000').style.display='block';")
            Select(DL.driver.find_element_by_id('s000')).select_by_visible_text("寇旭珂")
            DL.driver.execute_script("document.getElementById('s001').style.display='block';")
            Select(DL.driver.find_element_by_id('s001')).select_by_visible_text("口扩扩")
            DL.driver.find_element_by_css_selector("div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)").click()
            time.sleep(1)
        def fwmgl_cwawlmplxgfwm(self):  # 错误按物流码批量修改防伪码
            time.sleep(3)
            # DL.driver.find_element_by_css_selector("li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量修改防伪码').click()
            DL.driver.find_element_by_css_selector("#txm").send_keys('12345678954984654684534864165')
            DL.driver.execute_script("document.getElementById('s000').style.display='block';")
            Select(DL.driver.find_element_by_id('s000')).select_by_visible_text("寇旭珂")
            DL.driver.execute_script("document.getElementById('s001').style.display='block';")
            Select(DL.driver.find_element_by_id('s001')).select_by_visible_text("口扩扩")
            DL.driver.find_element_by_css_selector("div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)").click()
            time.sleep(1)

        def fwmgl_afwidplxgfwm(self):  # 按防伪ID批量修改防伪码
            # DL.driver.find_element_by_css_selector("li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量修改防伪码').click()
            time.sleep(2)
            target_elem = DL.driver.find_element_by_css_selector('div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)')
            DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
            DL.driver.find_element_by_css_selector('div.col-sm-2:nth-child(2) > input:nth-child(1)').send_keys('0')
            DL.driver.find_element_by_css_selector('div.col-sm-2:nth-child(3) > input:nth-child(1)').send_keys('100')
            DL.driver.execute_script("document.getElementById('s00').style.display='block';")
            Select(DL.driver.find_element_by_id('s00')).select_by_visible_text("寇旭珂")
            DL.driver.execute_script("document.getElementById('s01').style.display='block';")
            Select(DL.driver.find_element_by_id('s01')).select_by_visible_text("口扩扩")
            time.sleep(2)
            DL.driver.find_element_by_css_selector('div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)').click()
            time.sleep(1)
        def fwmgl_cwafwidplxgfwm(self):  # 按防伪ID批量修改防伪码
            # DL.driver.find_element_by_css_selector("li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量修改防伪码').click()
            time.sleep(2)
            target_elem = DL.driver.find_element_by_css_selector('div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)')
            DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
            DL.driver.find_element_by_css_selector('div.col-sm-2:nth-child(2) > input:nth-child(1)').send_keys('999999999999999999999999999')
            DL.driver.find_element_by_css_selector('div.col-sm-2:nth-child(3) > input:nth-child(1)').send_keys('1009999999999999999999999999999999999')
            DL.driver.execute_script("document.getElementById('s00').style.display='block';")
            Select(DL.driver.find_element_by_id('s00')).select_by_visible_text("寇旭珂")
            DL.driver.execute_script("document.getElementById('s01').style.display='block';")
            Select(DL.driver.find_element_by_id('s01')).select_by_visible_text("口扩扩")
            time.sleep(2)
            DL.driver.find_element_by_css_selector('div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)').click()
            time.sleep(1)
        def fwmgl_apcplxgfwm(self):  # 按批次批量修改防伪码
            # DL.driver.find_element_by_css_selector("li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量修改防伪码').click()
            time.sleep(2)
            target_elem = DL.driver.find_element_by_css_selector('div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)')
            DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
            DL.driver.execute_script("document.getElementById('s1').style.display='block';")
            Select(DL.driver.find_element_by_id('s1')).select_by_visible_text("kou123456789")
            DL.driver.execute_script("document.getElementById('s2').style.display='block';")
            Select(DL.driver.find_element_by_id('s2')).select_by_visible_text("寇旭珂")
            DL.driver.execute_script("document.getElementById('s3').style.display='block';")
            Select(DL.driver.find_element_by_id('s3')).select_by_visible_text("口扩扩")
            time.sleep(2)
            DL.driver.find_element_by_css_selector('div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)').click()
            time.sleep(1)
        def fwmgl_acpplxgfwm(self):  # 按产品批量修改防伪码
            # DL.driver.find_element_by_css_selector("li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量修改防伪码').click()
            time.sleep(2)
            target_elem = DL.driver.find_element_by_css_selector('div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)')
            DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
            DL.driver.execute_script("document.getElementById('cp').style.display='block';")
            Select(DL.driver.find_element_by_id('cp')).select_by_visible_text("寇旭珂")
            DL.driver.execute_script("document.getElementById('s4').style.display='block';")
            Select(DL.driver.find_element_by_id('s4')).select_by_visible_text("口扩扩")
            time.sleep(2)
            DL.driver.find_element_by_css_selector('div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)').click()
            time.sleep(1)

        def fwmgl_ascrqxgfwm(self):  # 按生成日期修改防伪码
            # DL.driver.find_element_by_css_selector("li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量修改防伪码').click()
            time.sleep(2)
            target_elem = DL.driver.find_element_by_css_selector('div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)')
            DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
            DL.driver.execute_script("document.getElementById('s5').style.display='block';")
            Select(DL.driver.find_element_by_id('s5')).select_by_visible_text("2020-11-19")
            DL.driver.execute_script("document.getElementById('s6').style.display='block';")
            Select(DL.driver.find_element_by_id('s6')).select_by_visible_text("寇旭珂")
            DL.driver.execute_script("document.getElementById('s7').style.display='block';")
            Select(DL.driver.find_element_by_id('s7')).select_by_visible_text("枇杷露")
            time.sleep(2)
            DL.driver.find_element_by_css_selector('div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)').click()
            time.sleep(1)

        def fwmgl_apcplscfwm(self):  # 按批次批量删除防伪码
            # DL.driver.find_element_by_css_selector("li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量删除防伪码').click()
            time.sleep(2)
            DL.driver.execute_script("document.getElementById('s1').style.display='block';")
            Select(DL.driver.find_element_by_id('s1')).select_by_visible_text("20201119152037")
            time.sleep(2)
            DL.driver.find_element_by_css_selector('div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)').click()
            time.sleep(1)

        def fwmgl_acpmplscfwm(self):  # 按产品名批量删除防伪码
            # DL.driver.find_element_by_css_selector("li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量删除防伪码').click()
            time.sleep(2)
            DL.driver.execute_script("document.getElementById('cp').style.display='block';")
            Select(DL.driver.find_element_by_id('cp')).select_by_visible_text("寇旭珂")
            time.sleep(2)
            DL.driver.find_element_by_css_selector('div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)').click()
            time.sleep(1)

        def fwmgl_ascrqplscfwm(self):  # 按生成日期批量删除防伪码
            # DL.driver.find_element_by_css_selector("li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量删除防伪码').click()
            time.sleep(2)
            target_elem = DL.driver.find_element_by_css_selector(
                'div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)')
            DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
            DL.driver.execute_script("document.getElementById('s5').style.display='block';")
            Select(DL.driver.find_element_by_id('s5')).select_by_visible_text("2020-11-19")
            time.sleep(2)
            DL.driver.find_element_by_css_selector(
                'div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)').click()
            time.sleep(1)

        def fwmgl_acxcsplscfwm(self):  # 按查询次数批量删除防伪码
            # DL.driver.find_element_by_css_selector("li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
            DL.driver.find_element_by_link_text('批量删除防伪码').click()
            time.sleep(2)
            target_elem = DL.driver.find_element_by_css_selector(
                'div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)')
            DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
            DL.driver.find_element_by_css_selector('.form-control').clear()
            DL.driver.find_element_by_css_selector('.form-control').send_keys('1000')
            time.sleep(2)
            DL.driver.find_element_by_css_selector(
                'div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)').click()
            time.sleep(1)
        # def fwmgl_scqbfwm(self):  # 删除全部防伪码
        #     DL.driver.find_element_by_css_selector("li.sub-menu:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
        #     DL.driver.find_element_by_link_text('批量删除防伪码').click()
        #     time.sleep(2)
        #     target_elem = DL.driver.find_element_by_css_selector(
        #         'div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)')
        #     time.sleep(2)
        #     DL.driver.find_element_by_css_selector(
        #         'div.form-group:nth-child(3) > div:nth-child(1) > button:nth-child(1)').click()
        #     time.sleep(1)