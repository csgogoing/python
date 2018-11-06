#coding=utf-8
from urllib import request, parse
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from base import Page
from time import sleep
from bs4 import BeautifulSoup
import requests
import re

class login(Page):
	'''
	登陆类，定义当前页面登陆元素定位输入、登陆方式
	'''
	answer_num = 2

	login_username_loc = (By.NAME, 'userName')
	login_password_loc = (By.NAME, 'password')
	login_button_loc = (By.CLASS_NAME, 'bc39')

	def login_doctor(self, id=117333219):
		#登陆医生端
		print('登陆医生端')
		self.driver.get("http://test.dr.xywy.com/site/login")
		self.driver.find_element_by_name('userlogin').send_keys('admin')
		self.driver.find_element_by_name('password').send_keys('123456')
		self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[4]/button').click()
		sleep(2)
		#进入IM问答页
		js1 = 'window.open("http://test.dr.xywy.com/account/pc-login?id=436558&user_id=%d");' %id
		try:
			self.script(js1)
		except:
			self.script(js1)
		else:
			pass
		sleep(1)
		js2 = 'window.open("http://test.d.xywy.com/doctor-client/im");'
		self.script(js2)
		handles = self.driver.window_handles
		self.driver.close()
		self.driver.switch_to_window(handles[2])
		self.driver.close()
		self.driver.switch_to_window(handles[1])
		sleep(2)


	def get_id(self, user_id, zd=None, did=None):
		#获取加密参数与cookie
		url_login='http://test.admin.d.xywy.com/admin/user/login'
		#传入的user_id查找页
		url="http://test.admin.d.xywy.com/question/default/index?QuestionBaseSearch[keyword_type]=uid&QuestionBaseSearch[keyword]=%d"%user_id
		headers={
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
		}
		req=requests.get(url_login)
		m_value = re.findall(r'f" value="(.*)">', req.text)
		cookies=req.cookies.get_dict()
		#登录im后台
		data={
		'_csrf':m_value,
		'Login[username]':'admin',
		'Login[password]':'123456',
		'Login[verifyCode]':'testme'
		}
		req_login=requests.post(url_login,data=data,cookies=cookies)
		a_cookies=req_login.cookies.get_dict()
		request_qid=req_login.get(url,cookies=a_cookies)
		#获取问题ID
		qid=re.findall(r'<td>(\d{5})</td>', request_qid)
		#置问题状态
		if did:
			request.urlopen('http://test.admin.d.xywy.com/site/question-order-pay-status?qid=%d&zd=1&%d' %qid,did)
		else:
			request.urlopen('http://test.admin.d.xywy.com/site/question-order-pay-status?qid=%d' %qid)

		return qid

	def take_question(self, qid):
		#问题库抢题
		#点击第1个问题
		handles = self.driver.window_handles
		self.driver.switch_to_window(handles[0])
		while True:
			self.Load_button()
			self.driver.find_element_by_xpath('//*[@class="message-status pr fYaHei clearfix"]/div[2]').click()
			sleep(1)
			My_questions = self.driver.find_elements_by_class_name('message-user-item')
			for i in My_questions:
				if int(i.get_attribute('data-qid')) == qid:
					i.click()
					self.Load_button()
					self.driver.find_element_by_link_text('抢题').click()
					print('抢题成功')
					return
		print('问题库找不到提问的qid为%d的问题' %qid)

	def answer_question(self, qid, is_summary):
		handles = self.driver.window_handles
		self.driver.switch_to_window(handles[0])
		#点击处理中
		self.driver.find_element_by_xpath('//*[@class="message-status pr fYaHei clearfix"]/div[1]')
		self.Load_button()
		#点击处理中问题
		My_questions = self.driver.find_elements_by_class_name('message-user-item')
		for i in My_questions:
			if int(i.get_attribute('data-qid')) == qid:
				i.click()
				self.Load_button()
				break
		#快速问答设置为An
		An = self.driver.find_element_by_xpath('//*[@class="message-quick-list clearfix fYaHei"]/li[1]')
		self.Load_button()
		#点击快速回答
		for i in range(4):
			An.click()
			sleep(0.5)
		if is_summary == 1:
			print('写总结')
			self.driver.find_element_by_xpath('//*[@class="pr tc f14 fYaHei message-select"]/span[2]').click()
			sleep(1)
			self.driver.find_element_by_id('zzs').send_keys('请描述患者症状，详细分析该症状是什么疾病，引发这种疾病或症状的原因是什么')
			self.driver.find_element_by_id('jys').send_keys('针对问题分析，尽可能详细的给出用户各种意见建议，包含：就诊建议、挂号科室建议、检查建议、用药建议、日常注意事项及护理建议等')
			self.driver.find_element_by_xpath('//*[@class="summary-send-btn f14 fYaHei"]').click()
			sleep(1)
		else:
			print('不写总结')

	def answer_ques_20(self, times):
		self.driver.find_element_by_name('message').clear()
		self.driver.find_element_by_name('message').send_keys('医生回复%d' %times)
		self.driver.find_element_by_name('message').send_keys(Keys.ENTER)

if __name__ == '__main__':
	A = login()
	# A.login_doctor()
	# test_id = 13624
	# A.take_question(test_id)
	# A.answer_question(test_id, 1)
	# A.answer_ques_20(test_id, 2)

	A.get_id(456654)