from statistics_im import Statistics_Im
#from statistics_tiezi import Statistics_Tiezi
#from Statistics_dianhua import Statistics_Dianhua
#from statistics_jiating import Statistics_Jiating
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
	#主类
	def __init__(self, file):
		rb = xlrd.open_workbook(file, formatting_info=True)
		self.wb = copy(rb)
 
	def save(self):
		self.wb.save('2019年统计数据_基础服务&后台组-%d月%d日改.xls'%(cur.month,cur.day))
	
	#示例写入方法s
	def write(self, sheet, row, column, result):
		ws = self.wb.get_sheet(0)
		ws.write(row, column, result)


if __name__ == '__main__':
	cur=datetime.datetime.now()
	excel_path=os.getcwd()+'\\2019年统计数据_基础服务&后台组-%d月%d日改.xls'%(cur.month,cur.day-1)
	we = Write_Excel(excel_path)
	Statistics_Im(we.wb).get_data()
	#Statistics_Tiezi(we.wb)
	#Statistics_Dianhua(we.wb)
	#Statistics_Jiating(we.wb)
	#Statistics_Yuyue(we.wb)
	we.save()
	# except Exception as e:
	# 	print('请检查当前目录下存在前一日的xls文件，并关闭此文件')
	# 	sleep(2)
	# 	sys.exit()
	# else:
	# 	pass