import time
from selenium import webdriver
import unittest
from ddt import ddt,data,unpack
from datasj import getdata
cc=getdata.Getdata(r'C:\Users\Administrator\PycharmProjects\autosuyuansys\datasj\溯源系统登录数据.xlsx')
sj=cc.login_data()
print(sj)
@ddt
class Login_To(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.driver.get('http://123.57.140.190/manage/')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
    @classmethod
    def tearDownClass(cls) :
        # cls.driver.quit()
        pass
    @data(*sj)
    @unpack
    def test_01(self,name,pwd):
        self.driver.find_element_by_css_selector('input.form-control:nth-child(1)').send_keys(name)
        self.driver.find_element_by_css_selector('input.form-control:nth-child(2)').send_keys(pwd)
        self.driver.find_element_by_css_selector('.btn').click()
        time.sleep(3)
        x=self.driver.find_element_by_css_selector('#top_menu > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').text
        y='前台浏览'
        try:
            self.assertEqual(x,y,msg='登录失败')
        except Exception as e:
            print(e)
if __name__ == '__main__':
    unittest.main()
