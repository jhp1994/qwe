from selenium import webdriver
import unittest
import time
class Oa(unittest.TestCase):
    def setUp(self):
        self.we = webdriver.Firefox()
        self.we.maximize_window()
        self.we.get("http://192.168.0.119:801/")
        self.we.find_element_by_css_selector("#tbx_UserName").send_keys("adm")
        self.we.find_element_by_css_selector("#tbx_Password").send_keys("adm")
        self.we.find_element_by_css_selector("#ibtLogin").click()
        self.we.implicitly_wait(3)
    #增加事务表单
    def test_case1(self):
        self.we.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/ul[6]/li[1]").click()
        time.sleep(3)
        self.we.switch_to.frame("tab_OaAffairPost_ifm")
        self.we.find_element_by_css_selector('#subject').send_keys("出差报销")
        self.we.find_element_by_css_selector("#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").clear()
        self.we.find_element_by_css_selector("#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").send_keys("2020-06-08")
        self.we.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input").send_keys("2")
        self.we.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(1)").send_keys("交通")
        self.we.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(3) > input:nth-child(1)").send_keys("200")
        self.we.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(3) > input:nth-child(1)").send_keys("200")
        self.we.find_element_by_css_selector("#save").click()
        self.we.implicitly_wait(8)
        a = self.we.switch_to.alert.text
        self.assertEqual(a,"成功：当前事务创建成功！",msg="未能成功创建事务表单")
        time.sleep(2)

    # 查询事务表单
    def test_case2(self):
        self.we.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/ul[6]/li[2]").click()
        time.sleep(3)
        self.we.switch_to.frame("tab_OaAffairList_ifm")
        self.we.implicitly_wait(3)
        self.we.find_element_by_css_selector("#tbx_Keyword").send_keys("出差报销")
        self.we.find_element_by_css_selector("#btnSearch").click()
        self.we.implicitly_wait(6)
        self.we.find_element_by_xpath('//*[@id="GridView1_ctl02_lbtSubject"]').click()
        self.we.implicitly_wait(3)
        self.we.switch_to.default_content()
        a = self.we.find_element_by_css_selector(".title").text
        self.assertEqual(a,"浏览：%s"%("出差报销"),msg="查询失败")
        time.sleep(6)
    #修改事务表单
    # def test_case3(self):
    #
    #
    # # 删除事务表单
    # def test_case4(self):
    #
    def tearDown(self):
        self.we.quit()
if __name__ == '__main__':
    unittest.main()
