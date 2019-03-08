from statistics_im import Statistics_Im
from statistics_tiezi import Statistics_Tiezi
from statistics_dianhua import Statistics_Dianhua
from statistics_jiating import Statistics_Jiating
#from statistics_yuyue import Statistics_Yuyue
from xlutils.copy import copy
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
		cur=datetime.datetime.now()
		self.datetime_need=[]
		for i in range(7):
			try:
				cur = cur-datetime.timedelta(days=1)
				self.datetime_need.append(cur)
				excel_path=os.getcwd()+'\\%d年统计数据_基础服务&后台组-%d月%d日改.xls'%(cur.year,cur.month,cur.day)
				file = xlrd.open_workbook(excel_path, formatting_info=True)
			except FileNotFoundError:
				pass
			else:
				print('已找到%d年%d月%d日的统计表格'%(cur.year,cur.month,cur.day))
				break
		self.wb = copy(file)
 
	def save(self):
		self.wb.save('2019年统计数据_基础服务&后台组-%d月%d日改.xls'%(datetime.datetime.now().month,datetime.datetime.now().day))
	
	#根据所选日期进行统计
	def statistics(self):
		for date_time in self.datetime_need:
			print('开始统计%s-%s-%s的数据'%(date_time.year,date_time.month,date_time.day))
			#Statistics_Im(self.wb, date_time).get_data()
			#Statistics_Tiezi(we.wb, date_time).get_data()
			#Statistics_Dianhua(we.wb, date_time).get_data()
			#Statistics_Jiating(we.wb, date_time).get_data()
			Statistics_Yuyue(we.wb, date_time).get_data()


if __name__ == '__main__':
	we = Write_Excel()
	we.statistics()
	we.save()
	# except Exception as e:
	# 	print('请检查当前目录下存在前一日的xls文件，并关闭此文件')
	# 	sleep(2)
	# 	sys.exit()
	# else:
	# 	pass