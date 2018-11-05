#coding=utf-8

class Page(object):
	'''
	登陆父类，定义登陆主网址、打开方式，查找元素类等
	'''

	xywy_url = ""

	def __init__(self, selenium_driver, base_url=xywy_url, parent=None):
		#初始化
		self.driver = selenium_driver
		self.base_url = base_url
		self.timeout = 30
		self.parent = parent


	def find_element(self, *loc):
		return self.driver.find_element(*loc)

	def find_elements(self, *loc):
		return self.driver.find_elements(*loc)

	def open(self):
		#打开网站
		#self._open(self.url)
		new_url = self.base_url
		self.driver.implicitly_wait(5)
		self.driver.get(new_url)

	def on_page(self):
		判断当前网址
		return self.driver.current_url == (self.base_url + self.url)

	def script(self):
		return self.driver.execute_script(src)
