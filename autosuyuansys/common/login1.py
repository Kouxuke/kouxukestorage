from selenium import webdriver
import time
class Test_Denglu():
    driver=webdriver.Firefox()
    def Denglu(self):
       self.driver.get(r"http://123.57.140.190/manage/index.php")
       self.driver.implicitly_wait(2)
       self.driver.find_element_by_css_selector("input.form-control:nth-child(1)").send_keys("admin")
       self.driver.find_element_by_css_selector("input.form-control:nth-child(2)").send_keys("admin999")
       self.driver.find_element_by_css_selector(".btn").click()
       time.sleep(5)
