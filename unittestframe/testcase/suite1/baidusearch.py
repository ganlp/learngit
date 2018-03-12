#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import unittest
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   

class BaiduSearch(unittest.TestCase):
	def setUp(self):
#		self.browser=webdriver.Chrome()
		self.browser=webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',\
			desired_capabilities=DesiredCapabilities.CHROME)

		self.base_url="https://www.baidu.com"
		self.verificationErrors=[]

	def test_baidu_search(self):
		u"""百度搜索"""
		browser=self.browser
		browser.get(self.base_url)
		browser.maximize_window()
		browser.find_element_by_id('kw').send_keys('selenium')
		browser.find_element_by_id('su').click()
		time.sleep(5)

	def tearDown(self):
		self.browser.quit()
		self.assertEqual(self.verificationErrors,[])

if __name__=='__main__':
	unittest.main()