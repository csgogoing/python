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
import zlib

class Statistics_Tiezi(object):
	'''
	'''
	def __init__(self):
		# , wb, date_time
		#self.wb = wb
		#self.cur = date_time
		self.cur = datetime.datetime.now()-datetime.timedelta(days=1)
		self.pass_day = self.cur.timetuple().tm_yday
		self.row = int(4+(self.cur.month+2)/3+self.cur.month+self.pass_day)
		print(self.row)
		self.headers={
		#"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		#"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
		}

	def tiezi_login(self):
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
		login_req = self.req.get('http://cadmin.xywy.com/main.php', headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
		if '欢迎进入' in login_req:
			return True
		else:
			return False

	def get_reward_unpaid(self, sheet, column, data):
		while True:
			self.req.encoding = 'gb2312'
			req = self.req.post(self.reward_url, data=data, headers=self.headers, auth=self.auth)
			if req.status_code==200:
				break
			else:
				sleep(2)
		req_text = req.content.decode('gb2312', errors='ignore')
		q_num = re.findall(r'总计: (.*)条', req_text)

		# self.ws = self.wb.get_sheet(sheet)
		# if q_num==[]:
		# 	#print('空')
		# 	self.ws.write(self.row, column, 0)
		# else:
		# 	#print('非空')
		# 	self.ws.write(self.row, column, q_num[0])

		#self.wb.Worksheets[sheet].Activate()
		if q_num==[]:
			print('空')
			#self.wb.ActiveSheet.Cells(self.row, column+1).Value='0'
		else:
			print(q_num[0])
			#self.wb.ActiveSheet.Cells(self.row, column+1).Value=q_num[0]


	def get_reward_paid(self, sheet, column, data):
		while True:
			req = self.req.post(self.reward_url, data=data, headers=self.headers, auth=self.auth)
			if req.status_code==200:
				break
			else:
				sleep(2)
		req_content = req.content.replace('0xe8', '')
		req_text=req_content.decode('gb2312')
		shifu = re.findall(r'总悬赏金额：(.*)元', req_text)[0]
		q_num = re.findall(r'总计: (.*)条', req_text)

		# self.ws = self.wb.get_sheet(sheet)
		# if shifu == '':
		# 	#print('空')
		# 	self.ws.write(self.row, column+3, 0)
		# else:
		# 	#print(shifu)
		# 	self.ws.write(self.row, column+3, shifu)
		# if q_num==[]:
		# 	#print('空')
		# 	self.ws.write(self.row, column+1, 0)
		# else:
		# 	#print(q_num[0])
		# 	self.ws.write(self.row, column+1, q_num[0])

		#self.wb.Worksheets[sheet].Activate()
		if shifu == '':
			print('空')
			#self.wb.ActiveSheet.Cells(self.row, column+4).Value='0'
		else:
			print(shifu)
			#self.wb.ActiveSheet.Cells(self.row, column+4).Value=shifu
		if q_num==[]:
			print('空')
			#self.wb.ActiveSheet.Cells(self.row, column+2).Value='0'
		else:
			print(q_num[0])
			#self.wb.ActiveSheet.Cells(self.row, column+2).Value=q_num[0]

	def get_assign_unpaid(self, sheet, column, data):
		while True:
			req = self.req.post(self.assign_url, data=data, headers=self.headers, auth=self.auth)
			if req.status_code==200:
				break
			else:
				sleep(2)
		req_text = req.content.decode('GBK')
		q_num = re.findall(r'订单数量：(.*)</td>', req_text)

		# self.ws = self.wb.get_sheet(sheet)
		# if q_num==[]:
		# 	#print('空')
		# 	self.ws.write(self.row, column, 0)
		# else:
		# 	#print('非空')
		# 	self.ws.write(self.row, column, q_num[0])

		self.wb.Worksheets[sheet].Activate()
		self.wb.ActiveSheet.Cells(self.row, column+1).Value=q_num[0]
		# if q_num==[]:
		# 	#print('空')
		# 	self.wb.ActiveSheet.Cells(self.row, column+1).Value='0'
		# else:
		# 	#print('非空')
		# 	self.wb.ActiveSheet.Cells(self.row, column+1).Value=q_num[0]


	def get_assign_paid(self, sheet, column, data):
		while True:
			req = self.req.post(self.assign_url, data=data, headers=self.headers, auth=self.auth)
			if req.status_code==200:
				break
			else:
				sleep(2)
		req_text = req.content.decode('GBK')
		shifu = re.findall(r'订单金额：(.*)元', req_text)[0]
		q_num = re.findall(r'订单数量：(.*)</td>', req_text)

		# self.ws = self.wb.get_sheet(sheet)
		# if shifu == '':
		# 	#print('空')
		# 	self.ws.write(self.row, column+3, 0)
		# else:
		# 	#print(shifu)
		# 	self.ws.write(self.row, column+3, shifu)
		# if q_num==[]:
		# 	#print('空')
		# 	self.ws.write(self.row, column+1, 0)
		# else:
		# 	#print(q_num[0])
		# 	self.ws.write(self.row, column+1, q_num[0])

		self.wb.Worksheets[sheet].Activate()
		if shifu == '':
			#print('空')
			self.wb.ActiveSheet.Cells(self.row, column+4).Value='0'
		else:
			#print(shifu)
			self.wb.ActiveSheet.Cells(self.row, column+4).Value=shifu

		self.wb.ActiveSheet.Cells(self.row, column+2).Value=q_num[0]
		# if q_num==[]:
		# 	#print('空')
		# 	self.wb.ActiveSheet.Cells(self.row, column+2).Value='0'
		# else:
		# 	#print(q_num[0])
		# 	self.wb.ActiveSheet.Cells(self.row, column+2).Value=q_num[0]


	def test(self):
		#测试类
		if not self.tiezi_login():
			print('有问必答登陆失败')
			return
		self.reward_url = 'http://cadmin.xywy.com/ques_list.php?type=list'

		reward_pc_unpaid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',
			'question_type':'100',
			'id':'',
			'ques_from': '47',
			'order_from':'100',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'xitongfree':'1',
			'search':'搜索'.encode('gb2312')
			}
		reward_wx_jkwd_paid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '64',
			'order_from':'1',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}

		self.get_reward_unpaid(2, 37, data=reward_pc_unpaid)
		#self.get_reward_paid(2, 37, data=reward_wx_jkwd_paid)


	def get_data(self):
		#获取数据
		if not self.tiezi_login():
			print('有问必答登陆失败')
			return
		self.reward_url = 'http://cadmin.xywy.com/ques_list.php?type=list'
		self.assign_url = 'http://cadmin.xywy.com/pay_ques_list.php?type=list'

		#悬赏
		#PC
		reward_pc_unpaid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',
			'question_type':'100',
			'id':'',
			'ques_from': '47',
			'order_from':'100',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'xitongfree':'1',
			'search':'搜索'.encode('gb2312')
			}
		reward_pc_paid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '47',
			'order_from':'1',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		#3g
		reward_3g_unpaid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '51',
			'order_from':'100',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'xitongfree':'1',
			'search':'搜索'.encode('gb2312')
			}
		reward_3g_paid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '51',
			'order_from':'1',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		#xywyapp
		reward_xywyapp_unpaid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '52',
			'order_from':'100',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'xitongfree':'1',
			'search':'搜索'.encode('gb2312')
			}
		reward_xywyapp_paid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '52',
			'order_from':'1',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		#问医生app
		reward_askapp_unpaid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '59',
			'order_from':'100',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'xitongfree':'1',
			'search':'搜索'.encode('gb2312')
			}
		reward_askapp_paid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '59',
			'order_from':'1',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		#wx在线健康问答
		reward_wx_jkwd_unpaid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '64',
			'order_from':'100',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'xitongfree':'1',
			'search':'搜索'.encode('gb2312')
			}
		reward_wx_jkwd_paid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '64',
			'order_from':'1',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		#wx寻医问药
		reward_wx_xywy_unpaid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '65',
			'order_from':'100',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'xitongfree':'1',
			'search':'搜索'.encode('gb2312')
			}
		reward_wx_xywy_paid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '65',
			'order_from':'1',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		#支付宝生活号
		reward_zfb_unpaid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '67',
			'order_from':'100',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'xitongfree':'1',
			'search':'搜索'.encode('gb2312')
			}
		reward_zfb_paid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '67',
			'order_from':'1',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		#中荷人寿
		reward_zhrs_unpaid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '61',
			'order_from':'100',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'xitongfree':'1',
			'search':'搜索'.encode('gb2312')
			}
		reward_zhrs_paid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '61',
			'order_from':'1',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		#58
		reward_58_unpaid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '62',
			'order_from':'100',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'xitongfree':'1',
			'search':'搜索'.encode('gb2312')
			}
		reward_58_paid = {
			'subject_1':'-1',
			'subject_2':'-1',
			'table':'question',	
			'question_type':'100',
			'id':'',
			'ques_from': '62',
			'order_from':'1',
			'title':'',
			'pid':'',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}

		# try:
		# 	self.get_reward_unpaid(2, 13, data=reward_pc_unpaid)
		# 	self.get_reward_paid(2, 13, data=reward_pc_paid)

		# 	self.get_reward_unpaid(2, 19, data=reward_3g_unpaid)
		# 	self.get_reward_paid(2, 19, data=reward_3g_paid)

		# 	self.get_reward_unpaid(2, 25, data=reward_xywyapp_unpaid)
		# 	self.get_reward_paid(2, 25, data=reward_xywyapp_paid)

		# 	self.get_reward_unpaid(2, 31, data=reward_askapp_unpaid)
		# 	self.get_reward_paid(2, 31, data=reward_askapp_paid)

		# 	self.get_reward_unpaid(2, 37, data=reward_wx_jkwd_unpaid)
		# 	self.get_reward_paid(2, 37, data=reward_wx_jkwd_paid)

		# 	self.get_reward_unpaid(2, 43, data=reward_wx_xywy_unpaid)
		# 	self.get_reward_paid(2, 43, data=reward_wx_xywy_paid)

		# 	self.get_reward_unpaid(2, 49, data=reward_zfb_unpaid)
		# 	self.get_reward_paid(2, 49, data=reward_zfb_paid)

		# 	self.get_reward_unpaid(2, 55, data=reward_zhrs_unpaid)
		# 	self.get_reward_paid(2, 55, data=reward_zhrs_paid)

		# 	self.get_reward_unpaid(2, 61, data=reward_58_unpaid)
		# 	self.get_reward_paid(2, 61, data=reward_58_paid)

		# except Exception as e:
		# 	print(e)
		# 	print('帖子悬赏统计失败')
		# else:
		# 	print('帖子悬赏统计完成')

		self.get_reward_unpaid(2, 13, data=reward_pc_unpaid)
		self.get_reward_paid(2, 13, data=reward_pc_paid)

		self.get_reward_unpaid(2, 19, data=reward_3g_unpaid)
		self.get_reward_paid(2, 19, data=reward_3g_paid)

		self.get_reward_unpaid(2, 25, data=reward_xywyapp_unpaid)
		self.get_reward_paid(2, 25, data=reward_xywyapp_paid)

		self.get_reward_unpaid(2, 31, data=reward_askapp_unpaid)
		self.get_reward_paid(2, 31, data=reward_askapp_paid)

		self.get_reward_unpaid(2, 37, data=reward_wx_jkwd_unpaid)
		self.get_reward_paid(2, 37, data=reward_wx_jkwd_paid)

		self.get_reward_unpaid(2, 43, data=reward_wx_xywy_unpaid)
		self.get_reward_paid(2, 43, data=reward_wx_xywy_paid)

		self.get_reward_unpaid(2, 49, data=reward_zfb_unpaid)
		self.get_reward_paid(2, 49, data=reward_zfb_paid)

		self.get_reward_unpaid(2, 55, data=reward_zhrs_unpaid)
		self.get_reward_paid(2, 55, data=reward_zhrs_paid)

		self.get_reward_unpaid(2, 61, data=reward_58_unpaid)
		self.get_reward_paid(2, 61, data=reward_58_paid)

		#指定
		#PC
		assign_pc_unpaid =  {
			'sel':'0',
			'title':'',
			'id':'',	
			'ques_from':'1',
			'pid':'',
			'status': '3',
			'money':'',
			'isrep':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		assign_pc_paid = {
			'sel':'0',
			'title':'',
			'id':'',	
			'ques_from':'1',
			'pid':'',
			'status': '1',
			'money':'',
			'isrep':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		#3g
		assign_3g_unpaid = {
			'sel':'0',
			'title':'',
			'id':'',	
			'ques_from':'2',
			'pid':'',
			'status': '3',
			'money':'',
			'isrep':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		assign_3g_paid = {
			'sel':'0',
			'title':'',
			'id':'',	
			'ques_from':'2',
			'pid':'',
			'status': '1',
			'money':'',
			'isrep':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		#xywyapp
		assign_xywyapp_unpaid = {
			'sel':'0',
			'title':'',
			'id':'',	
			'ques_from':'3',
			'pid':'',
			'status': '3',
			'money':'',
			'isrep':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		assign_xywyapp_paid = {
			'sel':'0',
			'title':'',
			'id':'',	
			'ques_from':'3',
			'pid':'',
			'status': '1',
			'money':'',
			'isrep':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		#问医生app
		assign_askapp_unpaid = {
			'sel':'0',
			'title':'',
			'id':'',	
			'ques_from':'4',
			'pid':'',
			'status': '3',
			'money':'',
			'isrep':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		assign_askapp_paid = {
			'sel':'0',
			'title':'',
			'id':'',	
			'ques_from':'4',
			'pid':'',
			'status': '1',
			'money':'',
			'isrep':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		#wx在线健康问答
		assign_wx_jkwd_unpaid = {
			'sel':'0',
			'title':'',
			'id':'',	
			'ques_from':'7',
			'pid':'',
			'status': '3',
			'money':'',
			'isrep':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		assign_wx_jkwd_paid = {
			'sel':'0',
			'title':'',
			'id':'',	
			'ques_from':'7',
			'pid':'',
			'status': '1',
			'money':'',
			'isrep':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		#wx寻医问药
		assign_wx_xywy_unpaid = {
			'sel':'0',
			'title':'',
			'id':'',	
			'ques_from':'8',
			'pid':'',
			'status': '3',
			'money':'',
			'isrep':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		assign_wx_xywy_paid = {
			'sel':'0',
			'title':'',
			'id':'',	
			'ques_from':'8',
			'pid':'',
			'status': '1',
			'money':'',
			'isrep':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		#wx小程序
		assign_wx_xcx_unpaid = {
			'sel':'0',
			'title':'',
			'id':'',	
			'ques_from':'5',
			'pid':'',
			'status': '3',
			'money':'',
			'isrep':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		assign_wx_xcx_paid = {
			'sel':'0',
			'title':'',
			'id':'',	
			'ques_from':'5',
			'pid':'',
			'status': '1',
			'money':'',
			'isrep':'0',
			'start':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'end':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'search':'搜索'.encode('gb2312')
			}
		# try:
		# 	self.get_assign_unpaid(4, 13, data=assign_pc_unpaid)
		# 	self.get_assign_paid(4, 13, data=assign_pc_paid)

		# 	self.get_assign_unpaid(4, 19, data=assign_3g_unpaid)
		# 	self.get_assign_paid(4, 19, data=assign_3g_paid)

		# 	self.get_assign_unpaid(4, 25, data=assign_xywyapp_unpaid)
		# 	self.get_assign_paid(4, 25, data=assign_xywyapp_paid)

		# 	self.get_assign_unpaid(4, 31, data=assign_askapp_unpaid)
		# 	self.get_assign_paid(4, 31, data=assign_askapp_paid)

		# 	self.get_assign_unpaid(4, 37, data=assign_wx_jkwd_unpaid)
		# 	self.get_assign_paid(4, 37, data=assign_wx_jkwd_paid)

		# 	self.get_assign_unpaid(4, 43, data=assign_wx_xywy_unpaid)
		# 	self.get_assign_paid(4, 43, data=assign_wx_xywy_paid)

		# 	self.get_assign_unpaid(4, 49, data=assign_wx_xcx_unpaid)
		# 	self.get_assign_paid(4, 49, data=assign_wx_xcx_paid)

		# except Exception as e:
		# 	print(e)
		# 	print('帖子指定统计失败')
		# else:
		# 	print('帖子指定统计完成')

		self.get_assign_unpaid(4, 13, data=assign_pc_unpaid)
		self.get_assign_paid(4, 13, data=assign_pc_paid)

		self.get_assign_unpaid(4, 19, data=assign_3g_unpaid)
		self.get_assign_paid(4, 19, data=assign_3g_paid)

		self.get_assign_unpaid(4, 25, data=assign_xywyapp_unpaid)
		self.get_assign_paid(4, 25, data=assign_xywyapp_paid)

		self.get_assign_unpaid(4, 31, data=assign_askapp_unpaid)
		self.get_assign_paid(4, 31, data=assign_askapp_paid)

		self.get_assign_unpaid(4, 37, data=assign_wx_jkwd_unpaid)
		self.get_assign_paid(4, 37, data=assign_wx_jkwd_paid)

		self.get_assign_unpaid(4, 43, data=assign_wx_xywy_unpaid)
		self.get_assign_paid(4, 43, data=assign_wx_xywy_paid)

		self.get_assign_unpaid(4, 49, data=assign_wx_xcx_unpaid)
		self.get_assign_paid(4, 49, data=assign_wx_xcx_paid)


if __name__ == '__main__':
	#测试运行
	A = Statistics_Tiezi()
	#A.tiezi_login()
	A.test()
	#A.get_data()
