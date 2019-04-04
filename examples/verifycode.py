#coding=utf-8
import time
from time import sleep
from lxml import etree
import requests
import re
import sys
import json
import tesserocr
from PIL import Image

class Ask(object):
	'''
	提问等接口相关类
	qtype:1 免费，2悬赏，3指定
	'''
	def __init__(self):
		self.msg_id_origin = 1
		self.now_time = 0

	def im_login(self):
		#获取加密参数与cookie
		# url = 'http://admin.d.xywy.com'
		# url_login='http://admin.d.xywy.com/admin/user/login'
		# #传入的user_id查找页
		# headers={
		# "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
		# }
		# req=requests.get(url_login)
		# sleep(2)
		# cookies=req.cookies.get_dict()
		# m_value = re.findall(r'f" value="(.*)">', req.text)
		# pic = re.findall(r'verifycode-image" src="(.*)" alt="', req.text)
		# url_pic = url + pic[0]
		# print(url_pic)
		# #请求验证码图,保存
		# req_pic=requests.get(url_pic)
		with open('1.png', 'wb') as f:
			f.write(req_pic.content)
		#识别验证码
		image=Image.open('1.png')
		verifyCode = tesserocr.image_to_text(image).strip('\n\r\t')  
		print('verfy:%s'%verifyCode)
		#写入密钥
		# cookie=req_pic.cookies.get_dict()
		# #cookies['PHPSESSID']=cookie['PHPSESSID']
		# cookies['PHPSESSID']='a5fjoq805qsfpmpbnmk8h5qrm6'
		# print(cookies)
		# #登录im后台
		# data={
		# '_csrf':m_value,
		# 'Login[verifyCode]':'neuoja'
		# }
		# #登陆IM后台获取Cookie
		# try:
		# 	req_login=requests.post(url_login,data=data,cookies=cookies)
		# except:
		# 	return
		# self.im_cookies=req_login.cookies.get_dict()
		# with open('cookies', 'wb') as f:
		# 	f.write(self.im_cookies)

	def get_id(self, did):
		sum = 0
		page_1 = 1
		page_2 = 1
		self.im_login()
		url = "http://admin.d.xywy.com/question/default/index"
		data_1_1 = {
			'QuestionBaseSearch[depa_pid]' : '',
			'QuestionBaseSearch[depa_sid]' : '',
			'QuestionBaseSearch[type]' : '',
			'QuestionBaseSearch[bgDate]' : '2018-11-22',
			'QuestionBaseSearch[edDate]' : '2018-12-21',
			'QuestionBaseSearch[keyword_type]' : 'did',
			'QuestionBaseSearch[keyword]' : '%s'%did,
			'QuestionBaseSearch[status]' : 1,
			'QuestionBaseSearch[source]' : '',
			'page' : page_1,
			'per-page' : 10
			}
		data_1_2 = {
			'QuestionBaseSearch[depa_pid]' : '',
			'QuestionBaseSearch[depa_sid]' : '',
			'QuestionBaseSearch[type]' : '',
			'QuestionBaseSearch[bgDate]' : '2018-12-22',
			'QuestionBaseSearch[edDate]' : '2018-12-29',
			'QuestionBaseSearch[keyword_type]' : 'did',
			'QuestionBaseSearch[keyword]' : '%s'%did,
			'QuestionBaseSearch[status]' : 1,
			'QuestionBaseSearch[source]' : '',
			'page' : page_1,
			'per-page' : 10
			}
		data_2_1 = {
			'QuestionBaseSearch[depa_pid]' : '',
			'QuestionBaseSearch[depa_sid]' : '',
			'QuestionBaseSearch[type]' : '',
			'QuestionBaseSearch[bgDate]' : '2018-11-22',
			'QuestionBaseSearch[edDate]' : '2018-12-21',
			'QuestionBaseSearch[keyword_type]' : 'did',
			'QuestionBaseSearch[keyword]' : '%s'%did,
			'QuestionBaseSearch[status]' : 2,
			'QuestionBaseSearch[source]' : '',
			'page' : page_1,
			'per-page' : 10
			}
		data_2_2 = {
			'QuestionBaseSearch[depa_pid]' : '',
			'QuestionBaseSearch[depa_sid]' : '',
			'QuestionBaseSearch[type]' : '',
			'QuestionBaseSearch[bgDate]' : '2018-12-22',
			'QuestionBaseSearch[edDate]' : '2018-12-29',
			'QuestionBaseSearch[keyword_type]' : 'did',
			'QuestionBaseSearch[keyword]' : '%s'%did,
			'QuestionBaseSearch[status]' : 2,
			'QuestionBaseSearch[source]' : '',
			'page' : page_1,
			'per-page' : 10
			}
		#while True:
		while True:
			try:
				request_1 = requests.get(url, params=data_1, cookies=self.im_cookies)
				elements = etree.HTML(request_1.text)
				result = re.findall(r'未开', request_1.text)
				sum = sum + len(result)
				print(1)
				qids = elements.xpath('//tbody/tr[10]/td[1]/text()')[0]
				print(2)
				qid = int(qids)
			except:
				break
			else:
				page_1+=1
				data_1['page']=page_1
		while True:
			try:
				request_2 = requests.get(url, params=data_2, cookies=self.im_cookies)
				elements = etree.HTML(request_2.text)
				result = re.findall(r'未开', request_2.text)
				sum = sum + len(result)
				qids = elements.xpath('//tbody/tr[10]/td[1]/text()')[0]
				qid = int(qids)
			except:
				break
			else:
				page_2+=1
				data_2['page']=page_2

		print('该医生38天内未总结问题数为%s'%sum)

if __name__ == '__main__':
	#测试运行
	A = Ask()
	A.get_id(117965200)
	#print(A.get_id(user_id=117333661))
	#print(A.baidu_page(2, user_id=117333661))
	#K = print(A.persue(15660, 'ywb', 666667))
	#print(K)
	#if 'Success!' in K:
	#	print(1)
	#A.other_page('xiaomi')