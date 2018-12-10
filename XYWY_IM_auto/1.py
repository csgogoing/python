#coding=utf-8
import time
from time import sleep
from urllib import request,parse
import requests
import re
import urllib,httplib2


class Ask(object):
	'''
	qtype:1 免费，2悬赏，3指定
	'''
	def __init__(self):
		self.msg_id_origin = 1
		self.now_time = 0

	def dr_login(self):
		#获取加密参数与cookie
		url_login = 'http://test.dr.xywy.com/site/login'
		#传入的user_id查找页
		self.headers = {
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
		}
		req=requests.get(url_login)
		m_value = re.findall(r'f" value="(.*)">', req.text)
		self.dr_cookies = req.cookies.get_dict()
		#登陆医平台
		data = {
		'_csrf':m_value,
		'userlogin':'admin',
		'password':'123456',
		}
		#登陆IM后台获取Cookie
		req_login = requests.get(url_login, headers=self.headers, data=data, cookies=self.dr_cookies)


	def doc_im_login(self, did):
		#登陆医生账号
		url_doc="http://test.dr.xywy.com/account/pc-login?id=436363&user_id=%d"%did
		url_im = 'http://test.d.xywy.com/doctor-client/im'
		url_rob = 'http://test.d.xywy.com/api-doctor/rob-question?qid=15336'

		self.dr_login()
		dr_doc = requests.get(url_doc, headers=self.headers, cookies=self.dr_cookies)
		self.dr_doc_cookies = dr_doc.cookies.get_dict()
		doc_im = requests.get(url_im, headers=self.headers, cookies=self.dr_doc_cookies)
		self.doc_im_cookies = dr_doc.cookies.get_dict()
		rob = requests.get(url_rob, headers=self.headers, cookies=self.doc_im_cookies)
		print(rob.text)





if __name__ == '__main__':
	A = Ask()
	resut = A.doc_im_login(68258667)