#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import unittest
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   

class BaiduSet(unittest.TestCase):
	def setUp(self):
#		self.browser=webdriver.Chrome()
		self.browser=webdriver.Remote(command_executor='http://192.168.18.169:5555/wd/hub',\
			desired_capabilities=DesiredCapabilities.CHROME)
		self.base_url="https://www.baidu.com"
		self.verificationErrors=[]

	def test_baidu_set(self):
		u'''搜索设置'''
		browser=self.browser
		browser.get(self.base_url)
		browser.maximize_window()
		browser.find_element_by_link_text('设置').click()
		browser.find_element_by_link_text("搜索设置").click()
		time.sleep(3)
		browser.find_element_by_xpath('//*[@id="nr"]').click()
		try:
			browser.find_element_by_xpath('//*[@id="nr"]/option[2]').click()
		except:
			browser.get_screenshot_as_file('E:\\unittestframe\\error_png\\set.png')

		browser.find_element_by_link_text('保存设置').click()
		time.sleep(1)
		alert=browser.switch_to_alert()
#		print alert.text
		alert.accept()
		browser.find_element_by_id('kw').send_keys('webdriver')
		browser.find_element_by_id('su').click()
		'''
		print browser.get_cookies()
		for i in browser.get_cookies():
			print "%s--%s" %(i['name'],i['value'])
		js="var q=document.documentElement.scrollTop=10000"
		browser.execute_script(js)
		time.sleep(5)
		js="var q=document.documentElement.scrollTop=0"
		browser.execute_script(js)
		'''
		time.sleep(5)
		browser.quit()

def tearDown(self):
	self.browser.quit()
	self.assertEqual(self.verificationErrors,[])

if __name__=='__main__':
	unittest.main()