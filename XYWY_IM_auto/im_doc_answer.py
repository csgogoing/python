#coding=utf-8
import time
from time import sleep
from urllib import request,parse
import requests
import re
import sys
from time import sleep

class login(Page):
	'''
	医生端i、抢题、回答
	'''
	answer_num = 2

	login_username_loc = (By.NAME, 'userName')
	login_password_loc = (By.NAME, 'password')
	login_button_loc = (By.CLASS_NAME, 'bc39')

	def login_doctor(self, did=117333219):
		#医平台登录
		url_login = 'http://test.dr.xywy.com/site/login'
		#传入的user_id查找页
		self.headers = {
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
		}
		req=requests.get(url_login)
		m_value = re.findall(r'f" value="(.*)">', req.text)
		self.dr_cookies = req.cookies.get_dict()
		#帐号密码
		data = {
		'_csrf':m_value,
		'userlogin':'admin',
		'password':'123456',
		}
		#注册_csrf
		req_login = requests.get(url_login, headers=self.headers, data=data, cookies=self.dr_cookies)
		#登录医生主页
		dr_doc = requests.get(url_doc, headers=self.headers, cookies=self.dr_cookies)
		self.dr_doc_cookies = dr_doc.cookies.get_dict()
		#登录IM平台并获取cookie
		doc_im = requests.get(url_im, headers=self.headers, cookies=self.dr_doc_cookies)
		self.doc_im_cookies = dr_doc.cookies.get_dict()

	def take_question(self, qid):
		#问题库抢题
		rob_qid = requests.get(url_rob, headers=self.headers, cookies=self.doc_im_cookies)
		print(rob_qid.text)


	def answer_question(self, qid, is_summary):
		handles = self.driver.window_handles
		self.driver.switch_to_window(handles[0])
		sleep(1)
		self.driver.refresh()
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
		if is_summary == 0:
			print('不写总结')
		else:
			print('写总结')
			self.driver.find_element_by_xpath('//*[@class="pr tc f14 fYaHei message-select"]/span[2]').click()
			sleep(1)
			self.driver.find_element_by_id('zzs').send_keys('请描述患者症状，详细分析该症状是什么疾病，引发这种疾病或症状的原因是什么')
			self.driver.find_element_by_id('jys').send_keys('针对问题分析，尽可能详细的给出用户各种意见建议，包含：就诊建议、挂号科室建议、检查建议、用药建议、日常注意事项及护理建议等')
			self.driver.find_element_by_xpath('//*[@class="summary-send-btn f14 fYaHei"]').click()
			sleep(1)

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