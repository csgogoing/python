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

class Statistics_Dianhua(object):
	'''
	'''
	def __init__(self, wb, date_time):
		self.wb = wb
		self.cur = date_time
		#self.cur = datetime.datetime.now()
		self.pass_day = self.cur.timetuple().tm_yday
		self.row = int(4+(self.cur.month+2)/3+self.cur.month+self.pass_day)-1
		print(self.row+1)
		self.headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
		}

	def dianhua_login(self):
		#获取加密参数与cookie
		self.url_login = 'http://dhys.z.xywy.com/login.php'
		self.req = requests.Session()
		self.req.cookies['clubsid']=r'tJNHHHaKM4sttZ26XUD7lOnGmZEcH8RnlqeieFRCstR%252FbkxdQQlz19ZbCd%252Fz5s6EKguC3MzXdx4Kc989%252Fk7%252F7s5N46Gv9i7jfc3hoTn1UesrukWkXQngl%252FzHKqe0eGXTl4OdwXaDQ%252F9mW8yfsDBARvBu8dKX53J%252F'
		self.req.cookies['member_login_captcha']=r'460a5d21e549b15e8632df2aab8404fc'
		self.req.cookies['PHPSESSID']=r'a5i8mfsvn9pjd7dli4bs354056'
		data = {
		'backurl':'',
		'username':'dujun',
		'passwd':'m=$=Bn(qoFYb',
		'img_code':'smqqs',
		'submit':'登陆'.encode('gb2312')
		}
		self.req.post(self.url_login, headers=self.headers, data=data)

	def get_num(self, sheet, column, params):
		while True:
			req = self.req.post(self.url, params=params, headers=self.headers)
			if req.status_code==200:
				break
			else:
				sleep(2)		
		req_text = req.content.decode('GBK')
		self.ws = self.wb.get_sheet(sheet)
		total_num = re.findall(r'总计: (.*)条', req_text)
		pay_num = re.findall(r'已付款订单量：(\d*) &nbsp', req_text)
		pay_amount = re.findall(r'已付款总金额：(\d+\.\d+)', req_text)
		if total_num==[]:
			#print('空')
			self.ws.write(self.row, column, 0)
		else:
			#print(total_num[0])
			self.ws.write(self.row, column, total_num[0])

		if pay_num==[]:
			#print('空')
			self.ws.write(self.row, column+1, 0)
		else:
			#print(total_num[0])
			self.ws.write(self.row, column+1, pay_num[0])

		if pay_amount==[]:
			#print('空')
			self.ws.write(self.row, column+3, 0)
		else:
			#print(pay_amount[0])
			self.ws.write(self.row, column+3, pay_amount[0])


	def get_data(self):
		#测试类
		self.dianhua_login()
		self.url = 'http://dhys.z.xywy.com/order.php'

		dianhua_3g = {
			'type':'order_list',
			'hidden_test':'1',
			'state':'0',	
			'pay_state':'0',
			'call_start':'',
			'call_start': '',
			'expert_name':'',
			'operator_id':'0',
			'created_at_start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'created_at_end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'done_at_start':'',
			'done_at_end':'',
			'search': '1',
			'trade_type':'0',
			'is_balance':'0',
			'order_type': '0',
			'balance_start':'',
			'balance_end':'',
			'order_num': '',
			'is_dhysfz':'全部'.encode('gb2312'),
			'source':'2',
			'platform_source_pay':'0',
			'hidden_test_check': 'on',	
			'search':'搜  索'.encode('gb2312')
			}

		dianhua_xywyapp = {
			'type':'order_list',
			'hidden_test':'1',
			'state':'0',	
			'pay_state':'0',
			'call_start':'',
			'call_start': '',
			'expert_name':'',
			'operator_id':'0',
			'created_at_start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'created_at_end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'done_at_start':'',
			'done_at_end':'',
			'search': '1',
			'trade_type':'0',
			'is_balance':'0',
			'order_type': '0',
			'balance_start':'',
			'balance_end':'',
			'order_num': '',
			'is_dhysfz':'全部'.encode('gb2312'),
			'source':'3',
			'platform_source_pay':'0',
			'hidden_test_check': 'on',	
			'search':'搜  索'.encode('gb2312')
			}

		dianhua_askapp = {
			'type':'order_list',
			'hidden_test':'1',
			'state':'0',	
			'pay_state':'0',
			'call_start':'',
			'call_start': '',
			'expert_name':'',
			'operator_id':'0',
			'created_at_start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'created_at_end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'done_at_start':'',
			'done_at_end':'',
			'search': '1',
			'trade_type':'0',
			'is_balance':'0',
			'order_type': '0',
			'balance_start':'',
			'balance_end':'',
			'order_num': '',
			'is_dhysfz':'全部'.encode('gb2312'),
			'source':'8',
			'platform_source_pay':'0',
			'hidden_test_check': 'on',	
			'search':'搜  索'.encode('gb2312')
			}

		dianhua_wx = {
			'type':'order_list',
			'hidden_test':'1',
			'state':'0',	
			'pay_state':'0',
			'call_start':'',
			'call_start': '',
			'expert_name':'',
			'operator_id':'0',
			'created_at_start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'created_at_end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'done_at_start':'',
			'done_at_end':'',
			'search': '1',
			'trade_type':'0',
			'is_balance':'0',
			'order_type': '0',
			'balance_start':'',
			'balance_end':'',
			'order_num': '',
			'is_dhysfz':'全部'.encode('gb2312'),
			'source':'12',
			'platform_source_pay':'0',
			'hidden_test_check': 'on',	
			'search':'搜  索'.encode('gb2312')
			}

		dianhua_baidu_xzh = {
			'type':'order_list',
			'hidden_test':'1',
			'state':'0',	
			'pay_state':'0',
			'call_start':'',
			'call_start': '',
			'expert_name':'',
			'operator_id':'0',
			'created_at_start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'created_at_end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'done_at_start':'',
			'done_at_end':'',
			'search': '1',
			'trade_type':'0',
			'is_balance':'0',
			'order_type': '0',
			'balance_start':'',
			'balance_end':'',
			'order_num': '',
			'is_dhysfz':'全部'.encode('gb2312'),
			'source':'14',
			'platform_source_pay':'0',
			'hidden_test_check': 'on',	
			'search':'搜  索'.encode('gb2312')
			}

		dianhua_sougou = {
			'type':'order_list',
			'hidden_test':'1',
			'state':'0',	
			'pay_state':'0',
			'call_start':'',
			'call_start': '',
			'expert_name':'',
			'operator_id':'0',
			'created_at_start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'created_at_end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'done_at_start':'',
			'done_at_end':'',
			'search': '1',
			'trade_type':'0',
			'is_balance':'0',
			'order_type': '0',
			'balance_start':'',
			'balance_end':'',
			'order_num': '',
			'is_dhysfz':'全部'.encode('gb2312'),
			'source':'18',
			'platform_source_pay':'0',
			'hidden_test_check': 'on',	
			'search':'搜  索'.encode('gb2312')
			}

		dianhua_pc = {
			'type':'order_list',
			'hidden_test':'1',
			'state':'0',	
			'pay_state':'0',
			'call_start':'',
			'call_start': '',
			'expert_name':'',
			'operator_id':'0',
			'created_at_start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'created_at_end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'done_at_start':'',
			'done_at_end':'',
			'search': '1',
			'trade_type':'0',
			'is_balance':'0',
			'order_type': '0',
			'balance_start':'',
			'balance_end':'',
			'order_num': '',
			'is_dhysfz':'全部'.encode('gb2312'),
			'source':'1',
			'platform_source_pay':'0',
			'hidden_test_check': 'on',	
			'search':'搜  索'.encode('gb2312')
			}

		dianhua_jrtt = {
			'type':'order_list',
			'hidden_test':'1',
			'state':'0',	
			'pay_state':'0',
			'call_start':'',
			'call_start': '',
			'expert_name':'',
			'operator_id':'0',
			'created_at_start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'created_at_end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'done_at_start':'',
			'done_at_end':'',
			'search': '1',
			'trade_type':'0',
			'is_balance':'0',
			'order_type': '0',
			'balance_start':'',
			'balance_end':'',
			'order_num': '',
			'is_dhysfz':'全部'.encode('gb2312'),
			'source':'17',
			'platform_source_pay':'0',
			'hidden_test_check': 'on',	
			'search':'搜  索'.encode('gb2312')
			}

		try:
			self.get_num(6, 17, params=dianhua_3g)
			self.get_num(6, 25, params=dianhua_xywyapp)
			self.get_num(6, 33, params=dianhua_askapp)
			self.get_num(6, 41, params=dianhua_wx)
			self.get_num(6, 49, params=dianhua_baidu_xzh)
			self.get_num(6, 57, params=dianhua_sougou)
			self.get_num(6, 65, params=dianhua_pc)
			self.get_num(6, 73, params=dianhua_jrtt)
		except Exception as e:
			print(e)
			print('电话医生统计失败')
		else:
			print('电话医生统计完成')


if __name__ == '__main__':
	#测试运行
	A = Statistics_Dianhua()
	#A.tiezi_login()
	#A.test()
	#A.get_data()
