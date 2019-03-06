#coding=utf-8
import time
import requests
import re
import sys
import json
import datetime
from requests.auth import HTTPBasicAuth
from time import sleep
from urllib import request,parse
from lxml import etree

class Statistics_Tiezi(object):
	'''
	'''
	def __init__(self):
		self.wb = wb
		self.cur = datetime.datetime.now()
		self.pass_day = self.cur.timetuple().tm_yday-1
		self.row = int(4+(self.cur.month+2)/3+self.cur.month+self.pass_day)-1
		print(self.row+1)
		self.headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
		}

	def tiezi_login(self):
		#获取加密参数与cookie
		url_login = 'http://cadmin.xywy.com/login.php'
		url='http://cadmin.xywy.com/ques_list.php?type=list'
		self.req = requests.Session()
		self.req.get(url_login, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk'))
		self.req.cookies['clubsid']=r'f6rSPMffrC%252Ble7VLt20eDcqB2F%252F77K7NzylLzC8pWGQYhDIHJKX%252FguL%252FwmAmLrySLs2FaHGRg1LPDgveGoYX83V2WjyXS5%252FiK3vqAYhyaoyrI5aLImsWjXsjE1hTDo05g%252B1lwiOCql2sIpxOqDB2iazOUFDmOHgZ'
		data = {
		'backurl' : '',
		'username' : 'dujun',
		'passwd' : 'zCbCyIZDd0o4',
		'submit' : '登陆'.encode('gb2312')
		}
		self.req.post(url_login, headers=self.headers, data=data, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk'))

	def test(self):
		#测试类
		self.tiezi_login()
		url='http://cadmin.xywy.com/ques_list.php?type=list'

		#悬赏
		#PC
		reward_pc_unpaid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '47',
			'order_from' : '2',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		reward_pc_paid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '47',
			'order_from' : '1',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		request_reward_pc_unpaid = self.req.post(url, data=reward_pc_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
		self.get_num_unpaid(3, 14, request_reward_pc_unpaid)
		request_reward_pc_paid = self.req.post(url, data=reward_pc_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
		self.get_num_paid(3, 14, request_reward_pc_paid)


	def get_data(self):
		self.tiezi_login()
		url='http://cadmin.xywy.com/ques_list.php?type=list'

		#悬赏
		#PC
		reward_pc_unpaid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '47',
			'order_from' : '2',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		reward_pc_paid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '47',
			'order_from' : '1',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		#3g
		reward_3g_unpaid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '4',
			'order_from' : '2',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		reward_3g_paid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '4',
			'order_from' : '1',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		#xywyapp
		reward_xywyapp_unpaid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '45',
			'order_from' : '2',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		reward_xywyapp_paid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '45',
			'order_from' : '1',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		#问医生app
		reward_askapp_unpaid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '47',
			'order_from' : '2',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		reward_askapp_paid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '47',
			'order_from' : '1',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		#wx在线健康问答
		reward_wx_jkwd_unpaid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '64',
			'order_from' : '2',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		reward_wx_jkwd_paid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '64',
			'order_from' : '1',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		#wx寻医问药
		reward_wx_xywy_unpaid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '65',
			'order_from' : '2',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		reward_wx_xywy_paid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '65',
			'order_from' : '1',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		#支付宝生活号
		reward_zfb_unpaid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '67',
			'order_from' : '2',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		reward_zfb_paid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '67',
			'order_from' : '1',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		#中荷人寿
		reward_zhrs_unpaid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '61',
			'order_from' : '2',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		reward_zhrs_paid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '61',
			'order_from' : '2',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		#58
		reward_58_unpaid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '62',
			'order_from' : '100',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		reward_58_paid = {
			'subject_1' : '-1',
			'subject_2' : '-1',
			'table' : 'question',	
			'question_type' : '100',
			'id' : '',
			'ques_from': '62',
			'order_from' : '1',
			'title' : '',
			'pid' : '',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}

		try:
			request_reward_pc_unpaid = self.req.post(url, data=reward_pc_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(2, 13, request_reward_pc_unpaid)
			request_reward_pc_paid = self.req.post(url, data=reward_pc_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(2, 13, request_reward_pc_paid)

			request_reward_3g_unpaid = self.req.post(url, data=reward_3g_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(2, 19, request_reward_3g_unpaid)
			request_reward_3g_paid = self.req.post(url, data=reward_3g_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(2, 19, request_reward_3g_paid)

			request_reward_xywyapp_unpaid = self.req.post(url, data=reward_xywyapp_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(2, 25, request_reward_xywyapp_unpaid)
			request_reward_xywyapp_paid = self.req.post(url, data=reward_xywyapp_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(2, 25, request_reward_xywyapp_paid)

			request_reward_askapp_unpaid = self.req.post(url, data=reward_askapp_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(2, 31, request_reward_askapp_unpaid)
			request_reward_askapp_paid = self.req.post(url, data=reward_askapp_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(2, 31, request_reward_askapp_paid)

			request_reward_wx_jkwd_unpaid = self.req.post(url, data=reward_wx_jkwd_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(2, 37, request_reward_wx_jkwd_unpaid)
			request_reward_wx_jkwd_paid = self.req.post(url, data=reward_wx_jkwd_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(2, 37, request_reward_wx_jkwd_paid)

			request_reward_wx_xywy_unpaid = self.req.post(url, data=reward_wx_xywy_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(2, 43, request_reward_wx_xywy_unpaid)
			request_reward_wx_xywy_paid = self.req.post(url, data=reward_wx_xywy_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(2, 43, request_reward_wx_xywy_paid)

			request_reward_zfb_unpaid = self.req.post(url, data=reward_zfb_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(2, 49, request_reward_zfb_unpaid)
			request_reward_zfb_paid = self.req.post(url, data=reward_zfb_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(2, 49, request_reward_zfb_paid)

			request_reward_zhrs_unpaid = self.req.post(url, data=reward_zhrs_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(2, 55, request_reward_zhrs_unpaid)
			request_reward_zhrs_paid = self.req.post(url, data=reward_zhrs_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(2, 55, request_reward_zhrs_paid)

			request_reward_58_unpaid = self.req.post(url, data=reward_58_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(2, 61, request_reward_58_unpaid)
			request_reward_58_paid = self.req.post(url, data=reward_58_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(2, 61, request_reward_58_paid)

		except Exception as e:
			print(e)
			print('帖子悬赏统计失败')
		else:
			print('帖子悬赏统计完成')

		#指定
		#PC
		assign_pc_unpaid =  {
			'sel' : '0',
			'title' : '',
			'id' : '',	
			'ques_from' : '1',
			'pid' : '',
			'status': '3',
			'money' : '',
			'isrep' : '0',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		assign_pc_paid = {
			'sel' : '0',
			'title' : '',
			'id' : '',	
			'ques_from' : '1',
			'pid' : '',
			'status': '1',
			'money' : '',
			'isrep' : '0',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		#3g
		assign_3g_unpaid = {
			'sel' : '0',
			'title' : '',
			'id' : '',	
			'ques_from' : '2',
			'pid' : '',
			'status': '3',
			'money' : '',
			'isrep' : '0',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		assign_3g_paid = {
			'sel' : '0',
			'title' : '',
			'id' : '',	
			'ques_from' : '2',
			'pid' : '',
			'status': '1',
			'money' : '',
			'isrep' : '0',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		#xywyapp
		assign_xywyapp_unpaid = {
			'sel' : '0',
			'title' : '',
			'id' : '',	
			'ques_from' : '3',
			'pid' : '',
			'status': '3',
			'money' : '',
			'isrep' : '0',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		assign_xywyapp_paid = {
			'sel' : '0',
			'title' : '',
			'id' : '',	
			'ques_from' : '3',
			'pid' : '',
			'status': '1',
			'money' : '',
			'isrep' : '0',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		#问医生app
		assign_askapp_unpaid = {
			'sel' : '0',
			'title' : '',
			'id' : '',	
			'ques_from' : '4',
			'pid' : '',
			'status': '3',
			'money' : '',
			'isrep' : '0',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		assign_askapp_paid = {
			'sel' : '0',
			'title' : '',
			'id' : '',	
			'ques_from' : '4',
			'pid' : '',
			'status': '1',
			'money' : '',
			'isrep' : '0',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		#wx在线健康问答
		assign_wx_jkwd_unpaid = {
			'sel' : '0',
			'title' : '',
			'id' : '',	
			'ques_from' : '7',
			'pid' : '',
			'status': '3',
			'money' : '',
			'isrep' : '0',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		assign_wx_jkwd_paid = {
			'sel' : '0',
			'title' : '',
			'id' : '',	
			'ques_from' : '7',
			'pid' : '',
			'status': '1',
			'money' : '',
			'isrep' : '0',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		#wx寻医问药
		assign_wx_xywy_unpaid = {
			'sel' : '0',
			'title' : '',
			'id' : '',	
			'ques_from' : '8',
			'pid' : '',
			'status': '3',
			'money' : '',
			'isrep' : '0',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		assign_wx_xywy_paid = {
			'sel' : '0',
			'title' : '',
			'id' : '',	
			'ques_from' : '8',
			'pid' : '',
			'status': '1',
			'money' : '',
			'isrep' : '0',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		#wx小程序
		assign_wx_xcx_unpaid = {
			'sel' : '0',
			'title' : '',
			'id' : '',	
			'ques_from' : '5',
			'pid' : '',
			'status': '3',
			'money' : '',
			'isrep' : '0',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		assign_wx_xcx_paid = {
			'sel' : '0',
			'title' : '',
			'id' : '',	
			'ques_from' : '5',
			'pid' : '',
			'status': '1',
			'money' : '',
			'isrep' : '0',
			'start' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'end' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day-1),
			'search':'搜索'.encode('gb2312')
			}
		try:
			request_assign_pc_unpaid = self.req.post(url, data=assign_pc_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(4, 13, request_assign_pc_unpaid)
			request_assign_pc_paid = self.req.post(url, data=assign_pc_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(4, 13, request_assign_pc_paid)

			request_assign_3g_unpaid = self.req.post(url, data=assign_3g_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(4, 19, request_assign_3g_unpaid)
			request_assign_3g_paid = self.req.post(url, data=assign_3g_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(4, 19, request_assign_3g_paid)

			request_assign_xywyapp_unpaid = self.req.post(url, data=assign_xywyapp_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(4, 25, request_assign_xywyapp_unpaid)
			request_assign_xywyapp_paid = self.req.post(url, data=assign_xywyapp_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(4, 25, request_assign_xywyapp_paid)

			request_assign_askapp_unpaid = self.req.post(url, data=assign_askapp_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(4, 31, request_assign_askapp_unpaid)
			request_assign_askapp_paid = self.req.post(url, data=assign_askapp_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(4, 31, request_assign_askapp_paid)

			request_assign_wx_jkwd_unpaid = self.req.post(url, data=assign_wx_jkwd_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(4, 37, request_assign_wx_jkwd_unpaid)
			request_assign_wx_jkwd_paid = self.req.post(url, data=assign_wx_jkwd_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(4, 37, request_assign_wx_jkwd_paid)

			request_assign_wx_xywy_unpaid = self.req.post(url, data=assign_wx_xywy_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(4, 43, request_assign_wx_xywy_unpaid)
			request_assign_wx_xywy_paid = self.req.post(url, data=assign_wx_xywy_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(4, 43, request_assign_wx_xywy_paid)

			request_assign_wx_xcx_unpaid = self.req.post(url, data=assign_wx_xcx_unpaid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_unpaid(4, 49, request_assign_wx_xcx_unpaid)
			request_assign_wx_xcx_paid = self.req.post(url, data=assign_wx_xcx_paid, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk')).content.decode('GBK')
			self.get_num_paid(4, 49, request_assign_wx_xcx_paid)

		except Exception as e:
			print(e)
			print('帖子指定统计失败')
		else:
			print('帖子指定统计完成')



	def get_num_unpaid(self, sheet, column, req_text):
		self.ws = self.wb.get_sheet(sheet)
		shifu = re.findall(r'总悬赏金额：(.*)元', req_text)[0]
		q_num = re.findall(r'总计: (.*) 条', req_text)
		if q_num==[]:
			self.ws.write(self.row, column, 0)
		else:
			self.ws.write(self.row, column, q_num[0])

	def get_num_paid(self, sheet, column, req_text):
		self.ws = self.wb.get_sheet(sheet)
		shifu = re.findall(r'总悬赏金额：(.*)元', req_text)[0]
		q_num = re.findall(r'总计: (.*) 条', req_text)
		if shifu == '':
			self.ws.write(self.row, column+3, 0)
		else:
			self.ws.write(self.row, column+3, shifu)
		if q_num==[]:
			self.ws.write(self.row, column+1, 0)
		else:
			self.ws.write(self.row, column+1, q_num[0])

if __name__ == '__main__':
	#测试运行
	A = Statistics_Tiezi()
	#A.tiezi_login()
	#A.test()
	#A.get_data()
