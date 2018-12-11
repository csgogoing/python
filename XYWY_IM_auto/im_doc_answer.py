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
	def __init__(self, did=117333219):
		#医平台登录
		url_login = 'http://test.dr.xywy.com/site/login'
		url_doc = 'http://test.dr.xywy.com/site/login'
		url_im = 'http://test.dr.xywy.com/site/login'
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

class answer_question():
	def __init__(self, qid, is_summary):
		self.qid = qid
		websocket.enableTrace(True)
		self.ws = websocket.WebSocketApp("ws://10.20.4.22:8078/websocket",on_message = on_message,on_error = on_error,on_close = on_close)
		self.ws.on_open = self.on_open
		for i in range(4):
			self.reply(1)
		if is_summary == 0:
			print('不写总结')
		else:
			print('写总结')
			pass
		ws.run_forever()

	def reply(self, ws, times):
		self.ws.send('{"from": "68258667","to": "333","id": "%d","body": {"content": "回复内容%d","qid": "%d"},"act": "PUB"}'%(int(round(time.time() * 1000))),times,%self.qid)

	def on_message(ws, message):
		print(message)
		if json.loads(message)['act'] == "PING":
			self.ws.send('{"act":"PONG"}')

	def on_error(ws, error):
		print(error)

	def on_close(ws):
		print("### closed ###")

	def on_open(ws):
		self.ws.send('{"userid": "68258667", "act": "CONNECT"}')


if __name__ == '__main__':
	A = login()
	# A.login_doctor()
	# test_id = 13624
	# A.take_question(test_id)
	# A.answer_question(test_id, 1)
	# A.answer_ques_20(test_id, 2)

	A.get_id(456654)