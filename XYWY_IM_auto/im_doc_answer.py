#coding=utf-8
import time
from time import sleep
from urllib import request,parse
import requests
import re
import sys
import websocket
import json

class login():
	'''
	医生端i、抢题、回答
	'''
	def __init__(self, did=117333219):
		#医平台登录
		self.did = did
		url_login = 'http://test.dr.xywy.com/site/login'
		url_login_doc = 'http://test.dr.xywy.com/account/list?AccountList[doc_id]=%d'%did
		url_doc_im = 'http://test.d.xywy.com/doctor-client/im'
		#传入的user_id查找页
		self.headers = {
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
		}
		req=requests.get(url_login)
		m_value = re.findall(r'f" value="(.*)">', req.text)
		self.dr_cookies = req.cookies.get_dict()
		#帐号密码
		data = {
		"_csrf":m_value,
		"userlogin":"admin",
		"password":"123456",
		}
		#注册_csrf
		req_login = requests.get(url_login, headers=self.headers, data=data, cookies=self.dr_cookies)
		#医生库查找医生获取info
		req_login_doc = requests.get(url_login_doc, headers=self.headers, cookies=self.dr_cookies)
		info = re.findall(r'info:(\d{6})', req_login_doc.text)
		#登录医生主页，注意cookie持久化问题
		url_doc = 'http://test.dr.xywy.com/account/pc-login?id=%s&user_id=%d'%(info[0],did)
		dr_doc = requests.get(url_doc, headers=self.headers, cookies=self.dr_cookies)
		self.dr_doc_cookies = dr_doc.cookies.get_dict()
		#登录IM平台并获取cookie
		doc_im = requests.get(url_doc_im, headers=self.headers, cookies=self.dr_doc_cookies)
		self.doc_im_cookies = dr_doc.cookies.get_dict()

	def take_question(self, qid):
		#问题库抢题
		url_rob = 'http://test.d.xywy.com/api-doctor/rob-question?qid=%d'%qid
		rob_qid = requests.get(url_rob, headers=self.headers, cookies=self.doc_im_cookies)
		code = json.loads(rob_qid.text)["code"]
		if code == 10000:
			return True
		else:
			print('抢题失败')
			return False

	def answer_question(self, qid, uid, is_summary):
		self.qid = qid
		self.uid = uid
		self.ws = websocket.create_connection("ws://10.20.4.22:8078/websocket")
		self.ws.send('{"userid": "%d", "act": "CONNECT"}'%self.did)
		while True:
			result = self.ws.recv()
			print(result)
			if json.loads(result)['act'] == "CONNECT_ACK":
				for i in range(4):
					self.ws.send('{"from": "%d","to": "%d","id": "%d","body": {"content": "回复内容1","qid": %d},"act": "PUB"}'%(self.did,self.uid,int(round(time.time() * 1000)),self.qid))
					sleep(0.5)
			if is_summary == 0:
				print('不写总结')
				return
			else:
				url_summary = 'http://test.d.xywy.com/api-doctor/summary'
				data = {
				"qid": "%d"%self.qid,
				"symptoms": "问题分析问题分析问题分析问题分析问题分析问题分析",
				"advice": "指导建议指导建议指导建议指导建议指导建议指导建议"
				}
				count = 0
				while count < 4:
					result = self.ws.recv()
					print(result)
					if json.loads(result)['act'] == "PING":
						self.ws.send('{"act":"PONG"}')
					if json.loads(result)['act'] == "PUB_ACK":
						count+=1
				sleep(5)
				while True:
					req_summary = requests.post(url_summary, headers=self.headers, data=data, cookies=self.doc_im_cookies)
					code = json.loads(req_summary.text)["code"]
					if code == 10000:
						print('写总结')
						return True
					elif code == 30000:
						sleep(2)
						continue
					else:
						print('写总结失败')
						return False

	def reply(self, times=0):
		#self.ws = websocket.create_connection("ws://10.20.4.22:8078/websocket")
		#self.ws.send('{"userid": "68258667", "act": "CONNECT"}')
		while True:
			result = self.ws.recv()
			print(result)
			if json.loads(result)['act'] == "PUB":
				self.ws.send('{"from": "%d","to": "%d","id": "%d","body": {"content": "医生回复内容%d","qid": "%d"},"act": "PUB"}'%(self.did,self.uid,int(round(time.time() * 1000)),times,self.qid))
				print('医生第%d次回复'%times)
				return

	def wsclose(self):
		self.ws.close()

if __name__ == '__main__':
	A = login(117333219)
	#print(A.take_question(15541))
	print(A.answer_question(15579,117333645,1))
	#A.reply(3)