#coding=utf-8
import time
from time import sleep
from urllib import request,parse
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
		#传入的user_id查找页
		# cookies = {'_csrf=2b7ffcbd2dce2c393cff65059f26eb41dec964639a739e3607710f4fe7bfb005a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%222EGL9xLtFUtH57kn2v632UjmhCrGCGKf%22%3B%7D; PHPSESSID=fr2ohukn16616erun5eck5lfn6; _identity=0c1e5eba030192c62326099615c43ff4cf5e632dea0b7499e9aa7c7918d99ad1a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A47%3A%22%5B14%2C%2251UEIILfTj07Vd4XaDk6ftfhM3yYb5pT%22%2C2592000%5D%22%3B%7D'}
		# url = 'http://admin.d.xywy.com'
		url_login='http://admin.d.xywy.com/admin/user/login'
		headers={
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
		}
		req_login=requests.get(url_login)
		# sleep(2)
		# cookies=req.cookies.get_dict()
		# m_value = re.findall(r'f" value="(.*)">', req.text)
		# pic = re.findall(r'verifycode-image" src="(.*)" alt="', req.text)
		# url_pic = url + pic[0]
		# print(url_pic)
		# #请求验证码图,保存
		# req_pic=requests.get(url_pic)
		# with open('1.png', 'wb') as f:
		# 	f.write(req_pic.content)
		# #识别验证码
		# image = Image.open('1.png')
		# verifyCode = tesserocr.image_to_text(image).strip('\n\r\t')  
		# print('verfy:%s'%verifyCode)
		# image = image.convert('L')
		# threashold = 80
		# table = []
		# for i in range(256):
		# 	if i < threashold:
		# 		table.append(0)
		# 	else:
		# 		table.append(1)
		# image_l = image.point(table, '1')
		# verifyCode = tesserocr.image_to_text(image_l).strip('\n\r\t')  
		# print('verfy2:%s'%verifyCode)
		# image.show()
		#写入密钥
		cookies=req_login.cookies.get_dict()
		#cookies['PHPSESSID']=cookie['PHPSESSID']
		cookies['PHPSESSID']='bevkcne9ea2h9ofa9bu4p7i170'
		print(cookies)
		#登录im后台
		data={
		'_csrf':m_value,
		'Login[username]':'fuyanqiu',
		'Login[password]':'123456',
		'Login[verifyCode]':'neuoja'
		}
		#登陆IM后台获取Cookie
		try:
			req_login=requests.post(url_login,data=data,cookies=cookies)
		except:
			return
		self.im_cookies=req_login.cookies.get_dict()
		with open('cookies', 'wb') as f:
			f.write(self.im_cookies)

	def get_id(self, did):
		cookies_origin = "PHPSESSID=bsb56aoeu7urp09d3ul6vopfp5; _csrf=652707f57b3f8425592c1b669e067d3c060535a78e54b285e6d529366a561eefa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22fLGAOGvd4BFCbmPWLMDl_bHYuhjnL2od%22%3B%7D; _identity=0c1e5eba030192c62326099615c43ff4cf5e632dea0b7499e9aa7c7918d99ad1a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A47%3A%22%5B14%2C%2251UEIILfTj07Vd4XaDk6ftfhM3yYb5pT%22%2C2592000%5D%22%3B%7D"		
		cookie_item = re.split(r'; |=', cookies_origin)
		cookies = {}
		for i in range(len(cookie_item)):
			if i%2 == 0:
				cookies[cookie_item[i]] = cookie_item[i+1]
				print('%s:%s'%(cookies[cookie_item[i]],cookie_item[i+1]))


		headers = {
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
		}
		sum = 0
		page_1 = 1
		page_2 = 1
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
				request_1 = requests.get(url, params=data_1_1, headers=headers, cookies=cookies)
				elements = etree.HTML(request_1.text)
				result = re.findall(r'未开', request_1.text)
				sum = sum + len(result)
				print(1)
				qids = elements.xpath('//tbody/tr[10]/td[1]/text()')[0]
				print(2)
				qid = int(qids)
			except Exception as e:
				print(e)
				break
			else:
				page_1+=1
				data_1['page']=page_1
		while True:
			try:
				request_2 = requests.get(url, params=data_2_1, headers=headers, cookies=cookies)
				elements = etree.HTML(request_2.text)
				result = re.findall(r'未开', request_2.text)
				sum = sum + len(result)
				qids = elements.xpath('//tbody/tr[10]/td[1]/text()')[0]
				qid = int(qids)
			except Exception as e:
				print(e)
				break
			else:
				page_2+=1
				data_2['page']=page_2

		print('该医生38天内未总结问题数为%s'%sum)

if __name__ == '__main__':
	#测试运行
	A = Ask()
	#A.get_id(117965200)
	#A.im_login()
	print(A.get_id(did=117965200))
	#print(A.baidu_page(2, user_id=117333661))
	#K = print(A.persue(15660, 'ywb', 666667))
	#print(K)
	#if 'Success!' in K:
	#	print(1)
	#A.other_page('xiaomi')