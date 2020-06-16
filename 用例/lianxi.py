from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://mail.qq.com/')
time.sleep(3)                                #time.sleep强制等待
browser.switch_to.frame("login_frame")
browser.find_element_by_class_name("inputstyle").send_keys("836863704")
browser.find_element_by_id("p").send_keys("jhp215216.")
browser.find_element_by_id("login_button").click()
browser.switch_to.default_content()
time.sleep(3)
browser.find_element_by_id("composebtn").click()
time.sleep(2)
browser.find_element_by_css_selector("body").send_keys("世界，你好")
browser.switch_to.frame("mainFrame")
browser.find_element_by_css_selector("#toAreaCtrl > div:nth-child(2) > input:nth-child(1)").send_keys("1670143025@qq.com")
browser.find_element_by_css_selector("#subject").send_keys("你好")
browser.find_element_by_css_selector("#frm > div:nth-child(12) > div:nth-child(1) > a:nth-child(2)").click()

browser.switch_to.default_content()
# browser.switch_to.frame(0)
time.sleep(3)

# browser.switch_to.default_content()
time.sleep(3)
browser.quit()


