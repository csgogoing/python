#coding=utf-8
import time
import requests
import re
import sys
import json
import datetime
from requests.auth import HTTPBasicAuth
from time import sleep
from lxml import etree

class Statistics_Jiating(object):
	'''
	'''
	def __init__(self, wb, date_time):
		# , wb, date_time
		self.wb = wb
		self.cur = date_time
		# self.cur = datetime.datetime.now()
		self.pass_day = self.cur.timetuple().tm_yday
		self.row = int(4+(self.cur.month+2)/3+self.cur.month+self.pass_day)
		print(self.row)
		self.headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
		}

	def jiating_login(self):
		#获取加密参数与cookie
		self.url_login = 'http://cadmin.xywy.com/login.php'
		self.auth = HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')
		self.req = requests.Session()
		self.req.get(self.url_login, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk'))
		self.req.cookies['clubsid']=r'f6rSPMffrC%252Ble7VLt20eDcqB2F%252F77K7NzylLzC8pWGQYhDIHJKX%252FguL%252FwmAmLrySLs2FaHGRg1LPDgveGoYX83V2WjyXS5%252FiK3vqAYhyaoyrI5aLImsWjXsjE1hTDo05g%252B1lwiOCql2sIpxOqDB2iazOUFDmOHgZ'
		data = {
		'backurl':'',
		'username':'',
		'passwd':'',
		'submit':'登陆'.encode('gb2312')
		}
		self.req.post(self.url_login, headers=self.headers, data=data, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk'))
		login_req = self.req.get('http://cadmin.xywy.com/main.php', headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('gb2312', errors='ignore')
		if '欢迎进入' in login_req:
			return True
		else:
			return False

	def get_num(self, sheet, column, data):
		while True:
			req = self.req.post(self.url, data=data, headers=self.headers, auth=self.auth)
			if req.status_code==200:
				break
			else:
				sleep(2)
		req_text = req.content.decode('gb2312', errors='ignore')
		#self.ws = self.wb.get_sheet(sheet)
		total_num = re.findall(r'总计: (.*)条', req_text)
		pay_num = re.findall(r'已付款订单量：(\d*) &nbsp', req_text)
		pay_amount = re.findall(r'已付款总金额：(\d+\.\d+)', req_text)

		self.wb.Worksheets[sheet].Activate()
		if total_num==[]:
			#print('空')
			self.wb.ActiveSheet.Cells(self.row, column+1).Value='0'
		else:
			#print(total_num[0])
			self.wb.ActiveSheet.Cells(self.row, column+1).Value=total_num[0]

		#print(pay_num[0])
		self.wb.ActiveSheet.Cells(self.row, column+2).Value=pay_num[0]

		if pay_amount==[]:
			#print('空')
			self.wb.ActiveSheet.Cells(self.row, column+5).Value='0'
		else:
			#print(pay_amount[0])
			self.wb.ActiveSheet.Cells(self.row, column+5).Value=pay_amount[0]

			
	def get_data(self):
		#获取数据
		if not self.jiating_login():
			print('有问必答登陆失败')
			return
		self.url = 'http://cadmin.xywy.com/fd_doctor.php?type=orderlist'

		reward_jtys = {
			'sel':'0',
			'title':'',
			'status':'-2',	
			'amount':'0',
			'xcode':'0',
			'orderfrom': '0',
			'subject_1':'-1',
			'subject_2':'-1',
			'category_1':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'p_start':'',
			'p_end':'',
			'e_start':'',
			'e_end':'',
			'trans_type':'',
			'vip_code':'',
			'search':'搜索'.encode('gb2312')
			}

		try:
			self.get_num(7, 2, data=reward_jtys)
		except Exception as e:
			print(e)
			print('家庭医生统计失败')
		else:
			print('家庭医生统计完成')


if __name__ == '__main__':
	#测试运行
	A = Statistics_Jiating()
	print(A.jiating_login())
	#A.get_data()
