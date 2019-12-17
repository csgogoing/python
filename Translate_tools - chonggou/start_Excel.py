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
from Translate import Py4Js
from time import sleep
#from pyexcel import EasyExcel


class Translate_Excel():
	#主类
	def __init__(self):
		ERP_path = os.getcwd()+'\\need_trans_2.xlsx'
		#ERP_path = os.getcwd()+'\\ERP6-9.xls'
		if os.path.exists(ERP_path):
			self.wpsApp = win32com.client.Dispatch("Excel.Application")
			self.wpsApp.Visible = 1
			self.xlBook = self.wpsApp.Workbooks.Open(ERP_path, ReadOnly=0, Editable=1)
			print('已找到ERP表格')
		else:
			sys.exit('当前目录下未找到ERP表格')

		#翻译模块实例化
		self.tran_google = Py4Js()

	def save_excel(self):
		#保存Excel
		self.xlBook.Save()
		self.xlBook.Close(True)
		self.wpsApp.Quit()
	
	def translate(self):
		self.xlBook.Worksheets[0].Activate()
		self.sheet = self.xlBook.ActiveSheet

		#记得表格设置成文本格式

		row = 2
		#找到当前未翻译的位置
		while self.sheet.Cells(row, 3).Value != None:
			row = row + 1
		
		while self.sheet.Cells(row, 1).Value != None:
			sleep(1)
			print('当前第%s行'%(row))
			chn_word = str(self.sheet.Cells(row,1).Value)
			if not re.search(r'[\u4e00-\u9fa5]',chn_word):
				try:
					self.sheet.Cells(row, 3).Value=self.sheet.Cells(row, 2).Value
				except Exception as e:
					self.sheet.Cells(row, 3).Value= '\'' + self.sheet.Cells(row, 2).Value
					self.sheet.Cells(row, 4).Value='写入了\'符号'
				finally:
					row = row + 1
			else:
				result = str(self.tran_google.google_translate(chn_word))
				#result = str(self.test(chn_word))
				if result != '':
					try:
						self.sheet.Cells(row, 3).Value=result
						if re.search(r'[\u4e00-\u9fa5]',result):
							print('未完整翻译')
							self.sheet.Cells(row, 4).Value='未完整翻译'
					except Exception as e:
						self.sheet.Cells(row, 3).Value= '\'' + result
						self.sheet.Cells(row, 4).Value='写入了\'符号'
				else:
					print('第%s行数据翻译失败'%row)
					self.sheet.Cells(row, 4).Value='未翻译'
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