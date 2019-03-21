#coding=utf-8
import time
import requests
import re
import sys
import json
import datetime
from time import sleep
from urllib import request,parse
from lxml import etree

class Statistics_Im(object):
	'''
	IM统计类
	'''
	def __init__(self, wb, date_time):
		self.wb = wb
		self.cur = date_time
		self.pass_day = self.cur.timetuple().tm_yday
		self.row = int(4+(self.cur.month+2)/3+self.cur.month+self.pass_day)-1
		print(self.row+1)
		self.headers={
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
		}

	def im_login(self):
		#获取加密参数与cookie
		# try:
		# 	with open('im_cookies') as f:
		# 		cookies_origin = f.read()
		# except FileNotFoundError:
		# 	print('请在当前目录下保存im_cookies文件与相应cookies内容')
		# else:
		# 	cookie_item = re.split(r'; |=', cookies_origin)
		# 	self.cookies = {}
		# 	for i in range(len(cookie_item)):
		# 		if i%2 == 0:
		# 			self.cookies[cookie_item[i]] = cookie_item[i+1]
				#获取加密参数与cookie
		self.url_login = 'http://admin.d.xywy.com/admin/user/login'
		self.req = requests.Session()
		self.req.cookies['_csrf']=r'7869301893ff8393ee576f9b6c9bc514281e3c97a85b62ef781e1a52260eca2ea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22kXLPW14kTobTVnm-afCz055h5qzmiqqs%22%3B%7D'
		self.req.cookies['PHPSESSID']=r'ms0l2tu9h4ptqnde47vhosgvu2'
		self.req.cookies['_identity']=r'0c1e5eba030192c62326099615c43ff4cf5e632dea0b7499e9aa7c7918d99ad1a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A47%3A%22%5B14%2C%2251UEIILfTj07Vd4XaDk6ftfhM3yYb5pT%22%2C2592000%5D%22%3B%7D'
		data = {
		'_csrf':r'd3ZZUXpxb0YcLhUBLUBbLSMZOwUsHwJrFhAaK0pEWi5CByM8EwAeNQ==',
		'Login[username]':'',
		'Login[password]':'',
		'Login[verifyCode]':'wefe',
		'Login[rememberMe]':'0',
		'Login[rememberMe]':'1',
		'login-button':''
		}
		try:
			self.req.post(self.url_login, headers=self.headers, data=data)
		except Exception as e:
			print('请检查网络是否通畅')

	def get_num_unpaid(self, sheet, column, params):
		while True:
			req = self.req.get(self.url, params=params, headers=self.headers)
			if req.status_code==200:
				break
			else:
				sleep(2)
		self.ws = self.wb.get_sheet(sheet)
		q_num = re.findall(r'共<b>(.*)</b>条数据.</div>', req.text)
		if q_num==[]:
			self.ws.write(self.row, column, 0)
		else:
			self.ws.write(self.row, column, q_num[0])

	def get_num_paid(self, sheet, column, params):
		while True:
			req = self.req.get(self.url, params=params, headers=self.headers)
			if req.status_code==200:
				break
			else:
				sleep(2)
		self.ws = self.wb.get_sheet(sheet)
		shifu = re.findall(r'实付金额：(.*)元</span>', req.text)[0]
		q_num = re.findall(r'共<b>(.*)</b>条数据.</div>', req.text)
		self.ws.write(self.row, column+3, shifu)
		if q_num==[]:
			self.ws.write(self.row, column+1, 0)
		else:
			self.ws.write(self.row, column+1, q_num[0])

	def get_num_paid_l(self, sheet, column, params):
		while True:
			req = self.req.get(self.url, params=params, headers=self.headers)
			if req.status_code==200:
				break
			else:
				sleep(2)
		self.ws = self.wb.get_sheet(sheet)
		shifu = re.findall(r'实付金额：(.*)元</span>', req.text)[0]
		q_num = re.findall(r'共<b>(.*)</b>条数据.</div>', req.text)
		self.ws.write(self.row, column+2, shifu)
		if q_num==[]:
			self.ws.write(self.row, column+1, 0)
		else:
			self.ws.write(self.row, column+1, q_num[0])


	def get_data(self):
		self.im_login()
		self.url = "http://admin.d.xywy.com/order/question/index"
		#免费
		#百度
		reward_baidu_unpaid = {
			'QuestionOrderSearch[order_type]':'1',
			'QuestionOrderSearch[pay_source]':'1',
			'QuestionOrderSearch[pay_status]':'',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#寻医问药
		reward_xywyapp_unpaid = {
			'QuestionOrderSearch[order_type]':'1',
			'QuestionOrderSearch[pay_source]':'2',
			'QuestionOrderSearch[pay_status]':'',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		try:

			self.get_num_unpaid(1, 10, reward_baidu_unpaid)
			self.get_num_unpaid(1, 16, reward_xywyapp_unpaid)
			
		except Exception as e:
			print(e)
			print('IM免费统计失败')
		else:
			print('IM免费统计完成')

		#悬赏
		#寻医问药app
		reward_xywyapp_unpaid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'2',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_xywyapp_paid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'2',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#问医生app
		reward_askapp_unpaid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'11',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_askapp_paid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'11',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#百度熊掌号
		reward_bdxzh_unpaid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'16',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_bdxzh_paid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'16',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#熊掌号底bar
		reward_bdxzh_bar_unpaid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'22',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_bdxzh_bar_paid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'22',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#熊掌号mip
		reward_bdxzh_mip_unpaid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'23',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_bdxzh_mip_paid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'23',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#wap
		reward_3g_unpaid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'4',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_3g_paid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'4',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#微信小程序
		reward_weixin_unpaid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'25',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_weixin_paid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'25',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#百度
		reward_baidu_unpaid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'1',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_baidu_paid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'1',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#华夏保险
		reward_hxbx_unpaid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'19',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_hxbx_paid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'19',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#搜狗
		reward_sougou_unpaid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'26',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_sougou_paid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'26',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#快应用
		reward_kuaiyingyong_unpaid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'14',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_kuaiyingyong_paid = {
			'QuestionOrderSearch[order_type]':'2',
			'QuestionOrderSearch[pay_source]':'14',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		try:
			self.get_num_unpaid(3, 13, reward_xywyapp_unpaid)
			self.get_num_paid(3, 13, reward_xywyapp_paid)

			self.get_num_unpaid(3, 19, reward_askapp_unpaid)
			self.get_num_paid(3, 19, reward_askapp_paid)

			self.get_num_unpaid(3, 25, reward_bdxzh_unpaid)
			self.get_num_paid(3, 25, reward_bdxzh_paid)

			self.get_num_unpaid(3, 31, reward_bdxzh_bar_unpaid)
			self.get_num_paid(3, 31, reward_bdxzh_bar_paid)

			self.get_num_unpaid(3, 37, reward_bdxzh_mip_unpaid)
			self.get_num_paid(3, 37, reward_bdxzh_mip_paid)

			self.get_num_unpaid(3, 43, reward_3g_unpaid)
			self.get_num_paid(3, 43, reward_3g_paid)

			self.get_num_unpaid(3, 49, reward_weixin_unpaid)
			self.get_num_paid(3, 49, reward_weixin_paid)

			self.get_num_unpaid(3, 55, reward_baidu_unpaid)
			self.get_num_paid(3, 55, reward_baidu_paid)

			self.get_num_unpaid(3, 60, reward_hxbx_unpaid)
			self.get_num_paid(3, 60, reward_hxbx_paid)

			self.get_num_unpaid(3, 65, reward_sougou_unpaid)
			self.get_num_paid(3, 65, reward_sougou_paid)

			self.get_num_unpaid(3, 70, reward_kuaiyingyong_unpaid)
			self.get_num_paid(3, 70, reward_kuaiyingyong_paid)

		except Exception as e:
			print(e)
			print('IM悬赏统计失败')
		else:
			print('IM悬赏统计完成')

		#指定
		#寻医问药app
		assign_xywyapp_unpaid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'2',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_xywyapp_paid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'2',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#问医生app
		assign_askapp_unpaid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'11',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_askapp_paid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'11',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#百度熊掌号
		assign_bdxzh_unpaid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'16',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_bdxzh_paid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'16',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#熊掌号底bar
		assign_bdxzh_bar_unpaid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'22',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_bdxzh_bar_paid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'22',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#熊掌号mip
		assign_bdxzh_mip_unpaid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'23',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_bdxzh_mip_paid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'23',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#wap
		assign_3g_unpaid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'4',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_3g_paid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'4',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#微信小程序
		assign_weixin_unpaid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'25',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_weixin_paid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'25',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#百度
		assign_baidu_unpaid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'1',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_baidu_paid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'1',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#华夏保险
		assign_hxbx_unpaid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'19',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_hxbx_paid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'19',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#搜狗
		assign_sougou_unpaid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'26',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_sougou_paid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'26',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#快应用
		assign_kuaiyingyong_unpaid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'14',
			'QuestionOrderSearch[pay_status]':'3',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_kuaiyingyong_paid = {
			'QuestionOrderSearch[order_type]':'3',
			'QuestionOrderSearch[pay_source]':'14',
			'QuestionOrderSearch[pay_status]':'2',
			'QuestionOrderSearch[pay_type]':'',
			'QuestionOrderSearch[keyword_type]':'',
			'QuestionOrderSearch[keyword]':'',
			'QuestionOrderSearch[bgDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		try:
			self.get_num_unpaid(5, 13, assign_xywyapp_unpaid)
			self.get_num_paid(5, 13, assign_xywyapp_paid)

			self.get_num_unpaid(5, 19, assign_askapp_unpaid)
			self.get_num_paid(5, 19, assign_askapp_paid)

			self.get_num_unpaid(5, 25, assign_bdxzh_unpaid)
			self.get_num_paid(5, 25, assign_bdxzh_paid)

			self.get_num_unpaid(5, 31, assign_bdxzh_bar_unpaid)
			self.get_num_paid(5, 31, assign_bdxzh_bar_paid)

			self.get_num_unpaid(5, 37, assign_bdxzh_mip_unpaid)
			self.get_num_paid(5, 37, assign_bdxzh_mip_paid)

			self.get_num_unpaid(5, 43, assign_3g_unpaid)
			self.get_num_paid(5, 43, assign_3g_paid)

			self.get_num_unpaid(5, 49, assign_kuaiyingyong_unpaid)
			self.get_num_paid_l(5, 49, assign_kuaiyingyong_paid)

			self.get_num_unpaid(5, 54, assign_baidu_unpaid)
			self.get_num_paid_l(5, 54, assign_baidu_paid)

			self.get_num_unpaid(5, 59, assign_sougou_unpaid)
			self.get_num_paid_l(5, 59, assign_sougou_paid)

		except Exception as e:
			print(e)
			print('IM指定统计失败')
		else:
			print('IM指定统计完成')



if __name__ == '__main__':
	#测试运行
	A = Statistics_Im()
	#A.get_data()
