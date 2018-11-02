#coding=utf-8
from selenium import webdriver

class Page(object):
	'''
	父类，定义登陆主网址、打开方式，查找元素类等
	'''

	xywy_url = ""

	def __init__(self):
		#初始化
		retry = 1
		while retry < 4:
			try:
				self.driver = webdriver.Firefox()
			except:
				print('调起浏览器失败，重试第%d次，共3次' %retry)
				retry = retry + 1
			else:
				break
		if retry == 4:
			exit('无法调起浏览器，请联系管理员')
		print('调起成功')
		self.driver.implicitly_wait(5)
		self.driver.maximize_window()
		self.timeout = 30


	def find_element(self, *loc):
		return self.driver.find_element(*loc)

	def find_elements(self, *loc):
		return self.driver.find_elements(*loc)

	def open(self, url):
		#打开网站
		self.driver.get(url)

	def on_page(self):
		#判断当前网址
		return self.driver.current_url == (self.base_url + self.url)

	def script(self, src):
		return self.driver.execute_script(src)

	def Load_button(self):
		while True:
			try:
				self.driver.find_element_by_id('loading')
			except:
				break
			else:
				pass

	def quit():
		self.driver.quit()