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

class Statistics_Jsdh(object):
	'''
	jsdh统计类
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
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
		}

	def jsdh_login(self):
		#获取加密参数与cookie
		# try:
		# 	with open('jsdh_cookies') as f:
		# 		cookies_origin = f.read()
		# except FileNotFoundError:
		# 	print('请在当前目录下保存jsdh_cookies文件与相应cookies内容')
		# else:
		# 	cookie_item = re.split(r'; |=', cookies_origin)
		# 	self.cookies = {}
		# 	for i in range(len(cookie_item)):
		# 		if i%2 == 0:
		# 			self.cookies[cookie_item[i]] = cookie_item[i+1]
				#获取加密参数与cookie
		self.url_login_detect = 'http://admin.jisudianhua.xywy.com/'
		self.req = requests.Session()
		# data = {
		# '_csrf':r'd3ZZUXpxb0YcLhUBLUBbLSMZOwUsHwJrFhAaK0pEWi5CByM8EwAeNQ==',
		# 'Login[username]':'',
		# 'Login[password]':'',
		# 'Login[verifyCode]':'wefe',
		# 'Login[rememberMe]':'0',
		# 'Login[rememberMe]':'1',
		# 'login-button':''
		# }
		self.req.cookies['_csrf']=r'3278db58468bd5e8ce03caa6e40e98cae9859caa4ea81bec02cc79cddaa0c6e3a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22d5z8OLInvmtIWeUowXIVkCyZZGIRoMPd%22%3B%7D'
		self.req.cookies['PHPSESSID']=r'pfekh1657aasnedttilt3rm931'
		self.req.cookies['_identity']=r''
		try:
			req_login = self.req.get(self.url_login_detect, headers=self.headers)
			if 'Welcome!' in req_login.text:
				return True
			else:
				return False
		except Exception as e:
			print(e)
			print('请检查网络是否通畅')

	def get_num_jsdh(self, sheet, column, params):
		while True:
			req = self.req.get(self.url, params=params, headers=self.headers)
			if req.status_code==200:
				break
			else:
				sleep(2)
		# self.ws = self.wb.get_sheet(sheet)
		# q_num = re.findall(r'共<b>(.*)</b>条数据.</div>', req.text)
		# if q_num==[]:
		# 	self.ws.write(self.row, column, 0)
		# else:
		# 	self.ws.write(self.row, column, q_num[0])

		self.wb.Worksheets[sheet].Activate()
		q_num = re.findall(r'共<b>(.*)</b>条数据.</div>', req.text)
		if q_num==[]:
			#print(00)
			self.wb.ActiveSheet.Cells(self.row, column+1).Value='0'
		else:
			#print(q_num[0])
			self.wb.ActiveSheet.Cells(self.row, column+1).Value=q_num[0]

	def get_num_pay(self, sheet, column, params):
		while True:
			req = self.req.get(self.url, params=params, headers=self.headers)
			if req.status_code==200:
				break
			else:
				sleep(2)
		# self.ws = self.wb.get_sheet(sheet)
		# q_num = re.findall(r'共<b>(.*)</b>条数据.</div>', req.text)
		# if q_num==[]:
		# 	self.ws.write(self.row, column, 0)
		# else:
		# 	self.ws.write(self.row, column, q_num[0])

		self.wb.Worksheets[sheet].Activate()
		q_num = re.findall(r'共<b>(.*)</b>条数据.</div>', req.text)
		if q_num==[]:
			#print(00)
			self.wb.ActiveSheet.Cells(self.row, column+1).Value='0'
			self.wb.ActiveSheet.Cells(self.row, column+4).Value='0'
		else:
			#print(q_num[0])
			self.wb.ActiveSheet.Cells(self.row, column+1).Value=q_num[0]
			self.wb.ActiveSheet.Cells(self.row, column+4).Value=int(q_num[0])*29

	def get_data(self):
		if not self.jsdh_login():
			print('jsdh登陆失败')
			return

		self.url = "http://admin.jisudianhua.xywy.com/question/default/index"

		#送心意
		jsdh_all = {
			'QuestionOrderSearch[bdate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		jsdh_paid = {
			'QuestionOrderSearch[bdate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[status]':'10'
			}
		jsdh_unpaid = {
			'QuestionOrderSearch[id]':'',
			'QuestionOrderSearch[order_id]':'',
			'QuestionOrderSearch[status]':'2',
			'QuestionOrderSearch[patient_phone]':'',
			'QuestionOrderSearch[depa_pid]':'',
			'QuestionOrderSearch[did]':'',
			'QuestionOrderSearch[doctor_phone]':'',
			'QuestionOrderSearch[source]':'',
			'QuestionOrderSearch[bdate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edate]':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		try:
			self.get_num_jsdh(0, 64, jsdh_all)
			self.get_num_jsdh(0, 66, jsdh_unpaid)
			#pay需要顺便计算总金额
			self.get_num_pay(0, 65, jsdh_paid)

		except Exception as e:
			print(e)
			print('极速电话统计失败')
		else:
			print('极速电话统计完成')
		
		# self.get_num_jsdh(0, 64, jsdh_all)
		# self.get_num_jsdh(0, 66, jsdh_unpaid)
		# #pay需要顺便计算总金额
		# self.get_num_pay(0, 65, jsdh_paid)


if __name__ == '__main__':
	#测试运行
	A = Statistics_Jsdh()
	A.get_data()
