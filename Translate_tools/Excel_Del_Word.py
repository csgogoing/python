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
from time import sleep
from Mysql_Use import Mysql


class Translate_Excel():
	#主类
	def __init__(self):
		ERP_path = os.getcwd()+'\\need_del.xlsx'
		#ERP_path = os.getcwd()+'\\ERP6-9.xls'
		if os.path.exists(ERP_path):
			self.wpsApp = win32com.client.Dispatch("Excel.Application")
			self.wpsApp.Visible = 1
			self.xlBook = self.wpsApp.Workbooks.Open(ERP_path, ReadOnly=0, Editable=1)
			print('已找到ERP表格')
		else:
			sys.exit('当前目录下未找到ERP表格')


	def save_excel(self):
		#保存Excel
		self.xlBook.Save()
		self.xlBook.Close(True)
		self.wpsApp.Quit()

	def del_words(self):
		mysql = Mysql('multilang')

		self.xlBook.Worksheets[0].Activate()
		self.sheet = self.xlBook.ActiveSheet

		row = 2
		while self.sheet.Cells(row, 1).Value != None:
			need_del_word = self.sheet.Cells(row, 1).Value
			#select_sql = 'update common_words set id=%d, chn_word="%s", baidu_word="%s");'%(id,chn_word,baidu_word)

			update_sql = 'DELETE FROM common_words WHERE chn_word="%s";'%(need_del_word)
			print(update_sql)
			result = mysql.exec(update_sql)
			row = row + 1



	def re_insert_words(self):
		mysql = Mysql('multilang')

		self.xlBook.Worksheets[0].Activate()
		self.sheet = self.xlBook.ActiveSheet
		#找到当前未翻译的位置
		row = 2
		auxiliary = ['is','was','are','were','do','did','does','be']

		while self.sheet.Cells(row, 1).Value != None:
			print('当前写入第%s行'%(row))
			id = row -1
			is_sentense = 1
			chn_word = str(self.sheet.Cells(row,1).Value)
			baidu_word = str(self.sheet.Cells(row,2).Value)
			#判断是否是句子
			if '.' not in baidu_word or ',' not in baidu_word or '!' not in baidu_word:
				baidu_list = baidu_word.split(' ')
				if len(baidu_list)>5:
					is_sentense = 1
				else:
					is_sentense = 0
					for tar in auxiliary:
						if tar in baidu_list:
							is_sentense = 1
							break
			#如果不是句子，首字母大写
			if is_sentense == 0:
				for i in range(len(baidu_list)):
					if re.search('[a-z]',baidu_list[i]):
						baidu_list[i]=baidu_list[i].title()
				baidu_word = ' '.join(baidu_list)

			sql = 'insert into test_1(id, chn_word, baidu_word) values(%d,"%s","%s");'%(id,chn_word,baidu_word)
			print(sql)
			result = mysql.exec(sql)
			if result == 'wrong':
				self.sheet.Cells(row, 4).Value='写入数据库失败'
			row = row + 1

	def insert_words(self):
		mysql = Mysql('multilang')

		self.xlBook.Worksheets[0].Activate()
		self.sheet = self.xlBook.ActiveSheet
		#找到当前未翻译的位置
		row = 2
		auxiliary = ['is','was','are','were','do','did','does','be']

		while self.sheet.Cells(row, 1).Value != None:
			print('当前写入第%s行'%(row))
			id = row -1
			is_sentense = 1
			chn_word = str(self.sheet.Cells(row,1).Value)
			baidu_word = str(self.sheet.Cells(row,2).Value)
			#判断是否是句子
			if '.' not in baidu_word:
				baidu_list = baidu_word.split(' ')
				if len(baidu_list)>7:
					is_sentense = 1
				else:
					is_sentense = 0
					for tar in auxiliary:
						if tar in baidu_list:
							is_sentense = 1
							break
			#如果不是句子，首字母大写
			if is_sentense == 0:
				for i in range(len(baidu_list)):
					if re.search('[a-z]',baidu_list[i]):
						baidu_list[i]=baidu_list[i].title()
				baidu_word = ' '.join(baidu_list)

			sql = 'insert into test_1(id, chn_word, baidu_word) values(%d,"%s","%s");'%(id,chn_word,baidu_word)
			#加个判断在这里
			print(sql)
			result = mysql.exec(sql)
			if result == 'wrong':
				self.sheet.Cells(row, 4).Value='写入数据库失败'
			row = row + 1

	def test(self, word):
		if word < 10:
			word = word * 2
			return word
		else:
			return ''

if __name__ == '__main__':
	tools = Translate_Excel()
	tools.del_words()
	#tools.insert_words()
	tools.save_excel()