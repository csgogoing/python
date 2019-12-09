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
import win32com.client
from xlutils.copy import copy
from lxml import etree
from translate import Py4Js
from time import sleep
from pyexcel import EasyExcel


class Translate_Excel():
	#主类
	def __init__(self):
		ERP_path = os.getcwd()+'\\ERP.xlsx'
		if os.path.exists(ERP_path):
			self.wpsApp = win32com.client.Dispatch("Excel.Application")
			self.wpsApp.Visible = 1
			self.xlBook = self.wpsApp.Workbooks.Open(ERP_path, ReadOnly=0, Editable=1)
			print('已找到ERP表格')
		else:
			sys.exit('当前目录下未找到ERP表格')
		#翻译模块实例化
		#self.tran_google = Py4Js()

	def save_excel(self):
		#保存Excel
		self.xlBook.SaveAs('ERP_result.xls')
		self.xlBook.Close()
		self.wpsApp.Quit()
	
	def translate(self):
		self.sheet = self.xlBook.Worksheets[0].Activate()

		row = 10
		nrows = self.sheet.Columns(2) - 1
		print('共%s行'%nrows)
		list_need = self.sheet.Columns(2).Value
		print(list_need)
		for word_need in list_need:
			print('当前第%s行'%row)
			#result = str(self.tran_google.google_translate(word_need))
			result = str(self.test(word_need))
			if result != '':
				self.xlBook.ActiveSheet.Cells(row, 2).Value=result
				if re.search(r'[\u4e00-\u9fa5]',result):
					print('未完整翻译')
					self.xlBook.ActiveSheet.Cells(row, 3).Value='未完整翻译'
				row = row + 1
			else:
				print('第%s行翻译失败'%row)
				break

	def test(self, word):
		if word < 10:
			word = word * 2
			return word
		else:
			return ''

if __name__ == '__main__':
	tools = Translate_Excel()
	tools.translate()
	tools.save_excel()