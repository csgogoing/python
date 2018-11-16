#coding=utf-8

from selenium import webdriver
from .driver import browser
import unittest


class MyTest(unittest.TestCase):
	#每一个测试用例需要执行打开网页、隐式等待、关闭网页过程
	def setUp(self):
		self.driver = browser()
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
		

	def tearDown(self):
		self.driver.quit()
