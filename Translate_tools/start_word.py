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
#from pyexcel import EasyExcel


class Translate_Excel():
	#主类
	def __init__(self):
		ERP_path = os.getcwd()+'\\ERP.xlsx'
		if os.path.exists(ERP_path):
			self.wpsApp = win32com.client.Dispatch("ket.Application")
			self.wpsApp.Visible = 1
			self.xlBook = self.wpsApp.Workbooks.Open(ERP_path, ReadOnly=0, Editable=1)
			print('已找到ERP表格')
		else:
			sys.exit('当前目录下未找到ERP表格')
		#翻译模块实例化
		self.tran_google = Py4Js()

	def save_excel(self):
		#保存Excel
		self.xlBook.SaveAs(os.getcwd()+'\\ERP_result.xlsx')
		self.xlBook.Close()
		self.wpsApp.Quit()
	
	def translate(self):
		self.xlBook.Worksheets[0].Activate()
		self.sheet = self.xlBook.ActiveSheet

		row = 2
		while self.sheet.Cells(row, 1).Value != None:
			sleep(1)
			print('当前第%s行'%(row))
			chn_word = str(self.sheet.Cells(row,1).Value)
			if not re.search(r'[\u4e00-\u9fa5]',chn_word):
				self.sheet.Cells(row, 3).Value=self.sheet.Cells(row, 2).Value
				row = row + 1
			else:
				result = str(self.tran_google.google_translate(chn_word))
				#result = str(self.test(chn_word))
				if result != '':
					self.sheet.Cells(row, 3).Value=result
					if re.search(r'[\u4e00-\u9fa5]',result):
						print('未完整翻译')
						self.sheet.Cells(row, 4).Value='未完整翻译'
				else:
					print('第%s行数据翻译失败'%row)
					self.sheet.Cells(row, 4).Value='未翻译'
					return
				row = row + 1




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