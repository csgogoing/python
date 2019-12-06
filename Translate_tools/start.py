#coding=utf-8
import requests
import re
import os
import sys
import random
import xlrd
import xlwt
import time
import datetime
import json
from xlutils.copy import copy
from lxml import etree
from translate import Py4Js


class Translate_Excel():
	#主类
	def __init__(self, file):
		self.rb = xlrd.open_workbook(file, formatting_info=True)
		self.table = self.rb.sheets()[0]

		self.wb = copy(self.rb)
		self.sheet = self.wb.get_sheet(0)

		self.tran_google = Py4Js()
 
	def save_excel(self):
		self.wb.save('translate_result.xls')
	
	def translate(self):
		row = 1
		nrows = self.table.nrows
		print('共%s行'%nrows)
		list_need = self.table.col_values(0, start_rowx=1, end_rowx=None)
		for word_need in list_need:

			result = self.tran_google.google_translate(word_need)
			print('当前第%s行'%row)
			self.sheet.write(row, 2, result)
			if re.search(r'[\u4e00-\u9fa5]',result):
				print('未完整翻译')
				self.sheet.write(row, 3, '未完整翻译')
			row = row + 1
			# if row == 8:
			# 	break


if __name__ == '__main__':
	ERP_path = os.getcwd()+'\\ERP.xls'
	tools = Translate_Excel(ERP_path)
	tools.translate()
	tools.save_excel()