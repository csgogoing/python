#coding=utf-8
from selenium import webdriver

class Init_open(object):
	def __init__(self, url):
		self.driver = webdriver.Firefox()
		self.driver.get(url)
		self.driver.implicitly_wait(5)
		self.driver.maximize_window()


	def f_element(self, loc):
		return self.driver.find_element(loc)

	def f_elements(self, *loc):
		return self.driver.find_elements(loc)

	def close(self):
		self.driver.close()