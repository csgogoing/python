#coding=utf-8
from statistics_im import Statistics_Im
from statistics_tiezi import Statistics_Tiezi
from statistics_dianhua import Statistics_Dianhua
from statistics_jiating import Statistics_Jiating
from statistics_yuyue import Statistics_Yuyue
from statistics_yhq import Statistics_Yhq
from statistics_jsdh import Statistics_Jsdh
from xlutils.copy import copy
from win32com.client import Dispatch  
import win32com.client
import re
import sys
import random
import os
import xlrd
import time
import datetime
from time import sleep

class Write_Excel():
	#表格处理类
	def __init__(self):
		day = 7
		cur=datetime.datetime.now()
		self.datetime_need=[]
		for i in range(day):
			cur = cur-datetime.timedelta(days=1)
			self.datetime_need.append(cur)
			excel_path = os.getcwd()+'\\%d年统计数据_基础服务&后台组-%d月%d日.xlsx'%(cur.year, cur.month, cur.day)
			if os.path.exists(excel_path):
				self.wpsApp = win32com.client.Dispatch("ket.Application")
				self.wpsApp.Visible = 0
				self.xlBook = self.wpsApp.Workbooks.Open(excel_path,ReadOnly=0, Editable=1)
				print('已找到%d年%d月%d日的统计表格'%(cur.year, cur.month, cur.day))
				break
			else:
				if i == day-1:
					sys.exit('当前目录下未找到7日内的统计表格')
 
	def save(self):
		save_path = os.getcwd()+'\\%d年统计数据_基础服务&后台组-%d月%d日.xlsx'%(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
		if os.path.exists(save_path):
			os.remove(save_path)
		self.xlBook.SaveAs(save_path)
		self.xlBook.Close()
		self.wpsApp.Quit()

	#根据所选日期进行统计
	def statistics(self):
		for date_time in self.datetime_need:
			print('开始统计%s-%s-%s的数据'%(date_time.year,date_time.month,date_time.day))
			# wps版本column从1开始
			Statistics_Yhq(self.xlBook, date_time).get_data()
			Statistics_Jsdh(self.xlBook, date_time).get_data()
			Statistics_Im(self.xlBook, date_time).get_data()
			Statistics_Tiezi(self.xlBook, date_time).get_data()
			Statistics_Dianhua(self.xlBook, date_time).get_data()
			Statistics_Jiating(self.xlBook, date_time).get_data()
			Statistics_Yuyue(self.xlBook, date_time).get_data()

			# excel版本column从0开始
			#Statistics_Im(self.wb, date_time).get_data()
			#Statistics_Tiezi(we.wb, date_time).get_data()
			#Statistics_Dianhua(we.wb, date_time).get_data()
			#Statistics_Jiating(self.wb, date_time).get_data()
			#Statistics_Yuyue(self.wb, date_time).get_data()
			#Statistics_Yhq(self.wb, date_time).get_data()
			#Statistics_Jsdh(self.wb, date_time).get_data()

if __name__ == '__main__':
	we = Write_Excel()
	we.statistics()
	we.save()