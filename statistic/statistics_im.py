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
	'''
	def __init__(self, wb):
		self.wb = wb
		self.cur = datetime.datetime.now()
		self.pass_day = self.cur.timetuple().tm_yday
		self.row = int(4+(self.cur.month+2)/3+self.cur.month+self.pass_day)-1
		print('当前写入第%s行'%self.row+1)
		self.headers={
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
		}

	def im_login(self):
		#获取加密参数与cookie
		try:
			with open('im_cookies') as f:
				cookies_origin = f.read()
		except FileNotFoundError:
			print('请在当前目录下保存im_cookies文件与相应cookies内容')
		else:
			cookie_item = re.split(r'; |=', cookies_origin)
			self.cookies = {}
			for i in range(len(cookie_item)):
				if i%2 == 0:
					self.cookies[cookie_item[i]] = cookie_item[i+1]


	def get_data(self):
		self.im_login()
		url = "http://admin.d.xywy.com/order/question/index"
		#悬赏
		#寻医问药app
		reward_xywyapp_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '2',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_xywyapp_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '2',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#问医生app
		reward_askapp_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '11',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_askapp_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '11',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#百度熊掌号
		reward_bdxzh_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '16',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_bdxzh_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '16',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#熊掌号底bar
		reward_bdxzh_bar_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '22',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_bdxzh_bar_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '22',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#熊掌号mip
		reward_bdxzh_mip_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '23',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_bdxzh_mip_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '23',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#wap
		reward_3g_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '4',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_3g_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '4',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#微信小程序
		reward_weixin_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '25',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_weixin_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '25',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#百度
		reward_baidu_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '1',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_baidu_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '1',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#华夏保险
		reward_hxbx_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '19',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_hxbx_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '19',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#搜狗
		reward_sougou_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '26',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_sougou_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '26',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#快应用
		reward_kuaiyingyong_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '14',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		reward_kuaiyingyong_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '14',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		try:
			request_reward_xywyapp_unpaid = requests.get(url, params=reward_xywyapp_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(3, 14, request_reward_xywyapp_unpaid)
			request_reward_xywyapp_paid = requests.get(url, params=reward_xywyapp_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(3, 14, request_reward_xywyapp_paid)

			request_reward_askapp_unpaid = requests.get(url, params=reward_askapp_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(3, 20, request_reward_askapp_unpaid)
			request_reward_askapp_paid = requests.get(url, params=reward_askapp_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(3, 20, request_reward_askapp_paid)

			request_reward_bdxzh_unpaid = requests.get(url, params=reward_bdxzh_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(3, 26, request_reward_bdxzh_unpaid)
			request_reward_bdxzh_paid = requests.get(url, params=reward_bdxzh_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(3, 26, request_reward_bdxzh_paid)

			request_reward_bdxzh_bar_unpaid = requests.get(url, params=reward_bdxzh_bar_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(3, 32, request_reward_bdxzh_bar_unpaid)
			request_reward_bdxzh_bar_paid = requests.get(url, params=reward_bdxzh_bar_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(3, 32, request_reward_bdxzh_bar_paid)

			request_reward_bdxzh_mip_unpaid = requests.get(url, params=reward_bdxzh_mip_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(3, 38, request_reward_bdxzh_mip_unpaid)
			request_reward_bdxzh_mip_paid = requests.get(url, params=reward_bdxzh_mip_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(3, 38, request_reward_bdxzh_mip_paid)

			request_reward_3g_unpaid = requests.get(url, params=reward_3g_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(3, 44, request_reward_3g_unpaid)
			request_reward_3g_paid = requests.get(url, params=reward_3g_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(3, 44, request_reward_3g_paid)

			request_reward_weixin_unpaid = requests.get(url, params=reward_weixin_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(3, 50, request_reward_weixin_unpaid)
			request_reward_weixin_paid = requests.get(url, params=reward_weixin_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(3, 50, request_reward_weixin_paid)

			request_reward_baidu_unpaid = requests.get(url, params=reward_baidu_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(3, 56, request_reward_baidu_unpaid)
			request_reward_baidu_paid = requests.get(url, params=reward_baidu_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(3, 56, request_reward_baidu_paid)

			request_reward_hxbx_unpaid = requests.get(url, params=reward_hxbx_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(3, 61, request_reward_hxbx_unpaid)
			request_reward_hxbx_paid = requests.get(url, params=reward_hxbx_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(3, 61, request_reward_hxbx_paid)

			request_reward_sougou_unpaid = requests.get(url, params=reward_sougou_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(3, 66, request_reward_sougou_unpaid)
			request_reward_sougou_paid = requests.get(url, params=reward_sougou_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(3, 66, request_reward_sougou_paid)

			request_reward_kuaiyingyong_unpaid = requests.get(url, params=reward_kuaiyingyong_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(3, 71, request_reward_kuaiyingyong_unpaid)
			request_reward_kuaiyingyong_paid = requests.get(url, params=reward_kuaiyingyong_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(3, 71, request_reward_kuaiyingyong_paid)

		except Exception as e:
			print(e)
		else:
			print('IM悬赏统计完成')

		#指定
		#寻医问药app
		assign_xywyapp_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '2',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_xywyapp_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '2',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#问医生app
		assign_askapp_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '11',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_askapp_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '11',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#百度熊掌号
		assign_bdxzh_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '16',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_bdxzh_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '16',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#熊掌号底bar
		assign_bdxzh_bar_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '22',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_bdxzh_bar_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '22',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#熊掌号mip
		assign_bdxzh_mip_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '23',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_bdxzh_mip_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '23',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#wap
		assign_3g_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '4',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_3g_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '4',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#微信小程序
		assign_weixin_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '25',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_weixin_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '25',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#百度
		assign_baidu_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '1',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_baidu_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '1',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#华夏保险
		assign_hxbx_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '19',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_hxbx_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '19',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#搜狗
		assign_sougou_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '26',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_sougou_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '26',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		#快应用
		assign_kuaiyingyong_unpaid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '14',
			'QuestionOrderSearch[pay_status]' : '1',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		assign_kuaiyingyong_paid = {
			'QuestionOrderSearch[order_type]' : '2',
			'QuestionOrderSearch[pay_source]' : '14',
			'QuestionOrderSearch[pay_status]' : '2',
			'QuestionOrderSearch[pay_type]' : '',
			'QuestionOrderSearch[keyword_type]' : '',
			'QuestionOrderSearch[keyword]' : '',
			'QuestionOrderSearch[bgDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day),
			'QuestionOrderSearch[edDate]' : '%s-%s-%s'%(self.cur.year,self.cur.month,self.cur.day)
			}
		try:
			request_assign_xywyapp_unpaid = requests.get(url, params=assign_xywyapp_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(5, 14, request_assign_xywyapp_unpaid)
			request_assign_xywyapp_paid = requests.get(url, params=assign_xywyapp_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(5, 14, request_assign_xywyapp_paid)

			request_assign_askapp_unpaid = requests.get(url, params=assign_askapp_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(5, 20, request_assign_askapp_unpaid)
			request_assign_askapp_paid = requests.get(url, params=assign_askapp_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(5, 20, request_assign_askapp_paid)

			request_assign_bdxzh_unpaid = requests.get(url, params=assign_bdxzh_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(5, 26, request_assign_bdxzh_unpaid)
			request_assign_bdxzh_paid = requests.get(url, params=assign_bdxzh_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(5, 26, request_assign_bdxzh_paid)

			request_assign_bdxzh_bar_unpaid = requests.get(url, params=assign_bdxzh_bar_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(5, 32, request_assign_bdxzh_bar_unpaid)
			request_assign_bdxzh_bar_paid = requests.get(url, params=assign_bdxzh_bar_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(5, 32, request_assign_bdxzh_bar_paid)

			request_assign_bdxzh_mip_unpaid = requests.get(url, params=assign_bdxzh_mip_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(5, 38, request_assign_bdxzh_mip_unpaid)
			request_assign_bdxzh_mip_paid = requests.get(url, params=assign_bdxzh_mip_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(5, 38, request_assign_bdxzh_mip_paid)

			request_assign_3g_unpaid = requests.get(url, params=assign_3g_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(5, 44, request_assign_3g_unpaid)
			request_assign_3g_paid = requests.get(url, params=assign_3g_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(5, 44, request_assign_3g_paid)

			request_assign_kuaiyingyong_unpaid = requests.get(url, params=assign_kuaiyingyong_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(5, 50, request_assign_kuaiyingyong_unpaid)
			request_assign_kuaiyingyong_paid = requests.get(url, params=assign_kuaiyingyong_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(5, 50, request_assign_kuaiyingyong_paid)

			request_assign_baidu_unpaid = requests.get(url, params=assign_baidu_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(5, 55, request_assign_baidu_unpaid)
			request_assign_baidu_paid = requests.get(url, params=assign_baidu_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(5, 55, request_assign_baidu_paid)


			request_assign_sougou_unpaid = requests.get(url, params=assign_sougou_unpaid, headers=self.headers, cookies=self.cookies).text
			self.get_num_unpaid(5, 60, request_assign_sougou_unpaid)
			request_assign_sougou_paid = requests.get(url, params=assign_sougou_paid, headers=self.headers, cookies=self.cookies).text
			self.get_num_paid(5, 60, request_assign_sougou_paid)



		except Exception as e:
			print(e)
		else:
			print('IM指定统计完成')


	def get_num_unpaid(self, sheet, column, req_text):
		self.ws = self.wb.get_sheet(sheet)
		q_num = re.findall(r'共<b>(.*)</b>条数据.</div>', req_text)
		if q_num==[]:
			self.ws.write(self.row, column-1, 0)
		else:
			self.ws.write(self.row, column-1, q_num[0])

	def get_num_paid(self, sheet, column, req_text):
		self.ws = self.wb.get_sheet(sheet)
		shifu = re.findall(r'实付金额：(.*)元</span>', req_text)[0]
		q_num = re.findall(r'共<b>(.*)</b>条数据.</div>', req_text)
		self.ws.write(self.row, column+2, shifu)
		if q_num==[]:
			self.ws.write(self.row, column, 0)
		else:
			self.ws.write(self.row, column, q_num[0])

	def get_num_paid_l(self, sheet, column, req_text):
		self.ws = self.wb.get_sheet(sheet)
		shifu = re.findall(r'实付金额：(.*)元</span>', req_text)[0]
		q_num = re.findall(r'共<b>(.*)</b>条数据.</div>', req_text)
		self.ws.write(self.row, column+1, shifu)
		if q_num==[]:
			self.ws.write(self.row, column, 0)
		else:
			self.ws.write(self.row, column, q_num[0])

if __name__ == '__main__':
	#测试运行
	A = Statistics_Im()
	#A.get_data()
