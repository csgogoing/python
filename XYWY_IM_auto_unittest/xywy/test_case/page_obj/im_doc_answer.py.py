#coding=utf-8


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
	'''
	登陆类，定义当前页面登陆元素定位输入、登陆方式
	'''
	url = ''

	login_username_loc = (By.NAME, 'userName')
	login_password_loc = (By.NAME, 'password')
	login_button_loc = (By.CLASS_NAME, 'bc39')

	def login_username(self, username):
		self.find_elemesnt(*self.login_username_loc).clear()	
		self.find_element(*self.login_username_loc).send_keys(username)

	def login_password(self, password):
		self.find_element(*self.login_password_loc).clear()	
		self.find_element(*self.login_password_loc).send_keys(password)

	def login_button(self):
		self.find_element(*self.login_button_loc).click()

	def user_login(self, username='', password=''):
		self.open()
		self.login_username(username)
		self.login_password(password)
		self.login_button()

	error_hint_loc = (By.CLASS_NAME, "Login-Ts")
	user_login_success_loc = (By.CLASS_NAME, "col04a")

	# 用户名错误提示
	def error_hint(self):
		return self.find_element(*self.error_hint_loc).text

	def user_login_success(self):
		return self.find_element(*self.user_login_success_loc).text

