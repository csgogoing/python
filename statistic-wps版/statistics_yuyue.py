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

class Statistics_Yuyue(object):
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

	def yuyue_login(self):
		#获取加密参数与cookie
		self.url_login = 'http://fzadmin.z.xywy.com/login.php'
		self.req = requests.Session()
		self.req.cookies['ad_cookie_usergroup']='1'
		self.req.cookies['login_captcha_fz']=r'569ad05d858a524b472b6999fcb32dbb'
		self.req.cookies['PHPSESSID']=r'doaa2c4vhjo7vpatu0l27ibkf6'
		self.req.cookies['z_jixiao_id']=r'704'
		self.req.cookies['z_jixiao_yonghu']=r'dujun'
		data = {
		'backurl':'',
		'username':'dujun',
		'passwd':'I<0,&3h%k^~j',
		'img_code':'mspqm',
		'submit':'登陆'.encode('gb2312')
		}
		self.req.post(self.url_login, headers=self.headers, data=data)
		login_req = self.req.get('http://fzadmin.z.xywy.com/main.php', headers=self.headers).content.decode('GBK')
		if '欢迎进入' in login_req:
			return True
		else:
			return False

	def get_num(self, sheet, column, params):
		while True:
			req = self.req.post(self.url, params=params, headers=self.headers)
			if req.status_code==200:
				break
			else:
				sleep(2)		
		req_text = req.content.decode('GBK')
		elements = etree.HTML(req_text)
		q_all = elements.xpath('/html/body/table[2]/tr[3]/td[2]/text()')[0]
		q_pc = elements.xpath('/html/body/table[2]/tr[3]/td[3]/text()')[0]
		q_app = elements.xpath('/html/body/table[2]/tr[3]/td[4]/text()')[0]
		q_3g = elements.xpath('/html/body/table[2]/tr[3]/td[5]/text()')[0]
		q_wx = elements.xpath('/html/body/table[2]/tr[3]/td[6]/text()')[0]
		q_hujiao = elements.xpath('/html/body/table[2]/tr[3]/td[7]/text()')[0]
		q_hujiao_gy = elements.xpath('/html/body/table[2]/tr[3]/td[8]/text()')[0]
		q_xywyapp = elements.xpath('/html/body/table[2]/tr[3]/td[9]/text()')[0]
		q_askapp = elements.xpath('/html/body/table[2]/tr[3]/td[11]/text()')[0]
		q_others = elements.xpath('/html/body/table[2]/tr[3]/td[12]/text()')[0]

		self.wb.Worksheets(sheet).Activate
		self.wb.ActiveSheet.Cells(self.row, column+1).Value=q_all
		self.wb.ActiveSheet.Cells(self.row, column+2).Value=q_pc
		self.wb.ActiveSheet.Cells(self.row, column+3).Value=q_app
		self.wb.ActiveSheet.Cells(self.row, column+4).Value=q_3g
		self.wb.ActiveSheet.Cells(self.row, column+5).Value=q_wx
		self.wb.ActiveSheet.Cells(self.row, column+6).Value=q_hujiao
		self.wb.ActiveSheet.Cells(self.row, column+7).Value=q_hujiao_gy
		self.wb.ActiveSheet.Cells(self.row, column+8).Value=q_xywyapp
		self.wb.ActiveSheet.Cells(self.row, column+9).Value=q_askapp
		self.wb.ActiveSheet.Cells(self.row, column+10).Value=q_others

		# self.ws = self.wb.get_sheet(sheet)
		# self.ws.write(self.row, column, q_all)
		# self.ws.write(self.row, column+1, q_pc)
		# self.ws.write(self.row, column+2, q_app)
		# self.ws.write(self.row, column+3, q_3g)
		# self.ws.write(self.row, column+4, q_wx)
		# self.ws.write(self.row, column+5, q_hujiao)
		# self.ws.write(self.row, column+6, q_hujiao_gy)
		# self.ws.write(self.row, column+7, q_xywyapp)
		# self.ws.write(self.row, column+8, q_askapp)
		# self.ws.write(self.row, column+9, q_others)


	def get_data(self):
		#测试类
		if not self.yuyue_login():
			print('预约挂号登陆失败')
			return
		self.url = 'http://fzadmin.z.xywy.com/statistics.php'

		yuyue_param = {
			'type':'plus_state_source_statistics',
			'team':'0',
			'startdate':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'enddate':'%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			}

		# try:
		# 	self.get_num(8, 2, params=yuyue_param)
		# except Exception as e:
		# 	print(e)
		# 	print('预约挂号统计失败')
		# else:
		# 	print('预约挂号统计完成')
		self.get_num(8, 2, params=yuyue_param)


if __name__ == '__main__':
	#测试运行
	A = Statistics_Yuyue()
	print(A.yuyue_login())
	#A.get_data()
