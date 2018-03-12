#coding=utf-8
import os,sys
sys.path.append('./suite')
import unittest,doctest,site
from suite import *
import HTMLTestRunner

alltestnames=[
	'suite.baidusearch.BaiduSearch',
	'suite.baiduset.BaiduSet',]
suite=unittest.TestSuite()

if __name__=='__main__':
	for test in alltestnames:
		try:
			suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
		except Exception:
			print 'ERROR:SKipping tests from "%s.'%test
			try:
				__import__(test)
			except ImportError:
				print "could not import the module."
			else:
				print "could not load the test suite"
			from traceback import print_exc
			print_exc()
		print
		print 'Running the tests'

filename='E:\\unittestframe\\result.html'
fp=file(filename,'wb')

runner=HTMLTestRunner.HTMLTestRunner(
	stream=fp,
	title='Report',
	description='details')
runner.run(suite)
'''
caselist=os.listdir('E:\\unittestframe\\testcase')
for a in caselist:
	print a
	s=a.split('.')[1:][0]
	if s=='py':
		os.system('python E:\\unittestframe\\testcase\\%s 1>>log.txt 2>&1'%a)
'''

