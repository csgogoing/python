#coding=utf-8
from requests.auth import HTTPBasicAuth
from time import sleep
from lxml import etree
import time
import requests
import re
import sys
import json
import datetime
import pic_rec

class Statistics_Yhq(object):
	'''
	'''
	def __init__(self, wb, date_time):
		# , wb, date_time
		self.wb = wb
		self.cur = date_time
		#self.cur = datetime.datetime.now()
		self.pass_day = self.cur.timetuple().tm_yday
		#由于医患群excel页面结构，需要行数-1
		self.row = int(4+(self.cur.month+2)/3+self.cur.month+self.pass_day-1)
		print(self.row)
		self.headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
		}

	def yhq_login(self):
		#获取加密参数与cookie
		self.url_login = 'http://yhqadmin.xywy.com/index.php?r=login/index'
		self.url_pic = 'http://yhqadmin.xywy.com/index.php?r=login/create-verify-code'
		self.req = requests.Session()
		times = 1
		retry = 30
		req_token = self.req.post(self.url_login, headers=self.headers)
		html = etree.HTML(req_token.text)
		token = html.xpath('//head/meta[4]/@content')[0]
		print(self.req.cookies)
		print(token)
		while True:
			req_pic = self.req.get(self.url_pic, headers=self.headers)
			result = pic_rec.recognition(req_pic.content, 4)		
			data = {
			'_csrf':'%s'%token,
			'LoginForm[uname]':'',
			'LoginForm[password]':'',
			'LoginForm[verify]':'%s'%result,
			'login-button':''
			}
			self.req.post(self.url_login, headers=self.headers, data=data)
			login_req = self.req.get('http://yhqadmin.xywy.com/index.php?r=frame%2Findex', headers=self.headers).text
			if 'wangpan666' in login_req:
				return True
			else:
				if times > retry:
					return False
				else:
					times = times + 1

	def get_num_yhq(self, sheet, column, params):
		while True:
			req = self.req.get(self.url, params=params, headers=self.headers)
			if req.status_code==200:
				break
			else:
				sleep(2)
		self.wb.Worksheets[sheet].Activate()

		q_num = re.findall(r'总订单：(.*)笔', req.text)[0]
		q_amount = re.findall(r'总金额：(.*)元', req.text)[0]
		self.wb.ActiveSheet.Cells(self.row, column+1).Value=q_num
		self.wb.ActiveSheet.Cells(self.row, column+2).Value=q_amount



	def get_data(self):
		#测试类
		if not self.yhq_login():
			print('预约挂号登陆失败')
			return
		self.url = 'http://yhqadmin.xywy.com/index.php'

		yhq_param = {
			'r':'order/index',
			'Order[doctor_id]':'',
			'Order[doctor_name]':'',
			'Order[user_id]':'',
			'Order[nickname]':'',
			'Order[order_num]':'',
			'Order[pay_num]':'',
			'Order[state]':'1',
			'Order[order_type]':'',
			'Order[is_zhzhen]':'',
			'Order[list]':'1',
			'Order[start]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'Order[end]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'Order[tag]':''
			}
		try:
			self.get_num_yhq(0, 61, params=yhq_param)
		except Exception as e:
			print(e)
			print('医患群统计失败')
		else:
			print('医患群统计完成')
		#self.get_num_yhq(0, 61, params=yhq_param)


if __name__ == '__main__':
	#测试运行
	A = Statistics_Yhq()
	A.get_data()
	#A.get_data()
