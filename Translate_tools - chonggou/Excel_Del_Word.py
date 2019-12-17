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
		ERP_path = os.getcwd()+'\\need_trans.xlsx'
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


	def replace_target(self):
		self.xlBook.Worksheets[0].Activate()
		self.sheet = self.xlBook.ActiveSheet

		#读取目标文件
		file_EE = open('E_to_E','r',encoding='utf-8')
		file_CE = open('C_to_E','r',encoding='utf-8')
		word_lists_EE=[]
		word_lists_CE=[]

		while file_EE.readline():
			word_line_EE = file_EE.readline().replace('\n','')
			if word_line_EE != '':
				words_kv_EE = word_line_EE.split('	')
				word_lists_EE.append(words_kv_EE)
		words_dict_EE = dict(word_lists_EE)
		while file_CE.readline():
			word_line_CE = file_CE.readline().replace('\n','')
			if word_line_CE != '':
				words_kv_CE = word_line_CE.split('	')
				word_lists_CE.append(words_kv_CE)
		words_dict_CE = dict(word_lists_CE)


		row = 2
		while self.sheet.Cells(row, 1).Value != None:
			print(row)
			target_C = str(self.sheet.Cells(row, 1).Value)
			target_E = str(self.sheet.Cells(row, 2).Value)
			if target_C in words_dict_CE.keys():
				print(target_C)
				self.sheet.Cells(row, 3).Value = target_E
				replaced_word = words_dict_CE[target_C]
			if target_E in words_dict_EE.keys():
				print(target_E)
				self.sheet.Cells(row, 3).Value = target_E
				replaced_word = words_dict_EE[target_E]

			result_word = self.replace_title(replaced_word)
			self.sheet.Cells(row, 2).Value = result_word
			row = row + 1

		file_CE.close()
		file_EE.close()


	def find_repeat(self):
		self.xlBook.Worksheets[0].Activate()
		self.sheet = self.xlBook.ActiveSheet

		#读取目标文件
		file_re = open('find_re','r',encoding='utf-8')
		word_lists_re=[]

		while file_re.readline():
			word_line_re = file_re.readline().replace('\n','')
			if word_line_re != '':
				#words_kv_re = word_line_re.split('	')
				word_lists_re.append(word_line_re)
		#words_dict_re = dict(word_lists_re)


		row = 2
		while self.sheet.Cells(row, 1).Value != None:
			print(row)
			target_e = str(self.sheet.Cells(row, 1).Value)
			if target_e in word_lists_re:
				print(target_e)
				self.sheet.Cells(row, 3).Value = '存在重复'

			row = row + 1

		file_re.close()



	def replace_title(self):

		self.xlBook.Worksheets[0].Activate()
		self.sheet = self.xlBook.ActiveSheet

		row = 2
		auxiliary = ['is','was','are','were','do','did','does','be']
		special_characters = ['% S', '% s', '%S', '\\ N', '\\N', '\\ n', '\\ R', '\\R','\\ r',\
							 '\\ T', '\\T', '\\ t', ' & ', '\'S', ' \\ ', ' / ']

		while self.sheet.Cells(row, 1).Value != None:
			print(row)
			is_sentense = 1
			need_write = 0
			trans_word = str(self.sheet.Cells(row, 2).Value)
			if trans_word == 'None':
				print('--------------------------------')
				row = row + 1
				continue
			#判断是否是句子
			if '.' not in trans_word and ',' not in trans_word and '!' not in trans_word and '?' not in trans_word:
				baidu_list = trans_word.split(' ')
				print(baidu_list)
				if len(baidu_list)>5:
					is_sentense = 1
				else:
					is_sentense = 0
					for aux in auxiliary:
						if aux in baidu_list:
							is_sentense = 1
							break
			#如果不是句子，首字母大写
			if is_sentense == 0:
				need_write = 1
				for i in range(len(baidu_list)):
					if re.search('[a-z]',baidu_list[i]):
						baidu_list[i]=baidu_list[i].title()
				up_word = ' '.join(baidu_list)
			else:
				need_write = 0
				up_word = trans_word
			# 翻译结果中的特殊符号替换成小写防止出错
			for characters in special_characters:
				if characters in up_word:
					need_write = 1
					up_word = up_word.replace('% S','%s')
					up_word = up_word.replace('% s','%s')
					up_word = up_word.replace('%S','%s')
					up_word = up_word.replace('\\ N','\\n')
					up_word = up_word.replace('\\N','\\n')
					up_word = up_word.replace('\\ n','\\n')
					up_word = up_word.replace('\\ R','\\r')
					up_word = up_word.replace('\\R','\\r')
					up_word = up_word.replace('\\ r','\\r')
					up_word = up_word.replace('\\ T','\\t')
					up_word = up_word.replace('\\T','\\t')
					up_word = up_word.replace('\\ t','\\t')
					up_word = up_word.replace(' & ','&')
					up_word = up_word.replace('\'S','\'s')
					up_word = up_word.replace(' / ','/')
					continue

			if need_write == 1:
				try:
					#self.sheet.Cells(row, 3).Value = trans_word
					self.sheet.Cells(row, 2).Value = up_word
					#self.sheet.Cells(row, 4).Value = '需要转换'
				except:
					self.sheet.Cells(row, 4).Value = '写入表格失败'
			row = row + 1


	def replace_word(self):

		self.xlBook.Worksheets[0].Activate()
		self.sheet = self.xlBook.ActiveSheet

		row = 2
		for i in range(row,1650):
			if self.sheet.Cells(row, 3).Value != None:
				try:
					self.sheet.Cells(row, 2).Value=self.sheet.Cells(row, 3).Value
					self.sheet.Cells(row, 4).Value='替换成功'
				except Exception as e:
					self.sheet.Cells(row, 2).Value= '\'' + self.sheet.Cells(row, 3).Value
					self.sheet.Cells(row, 4).Value='写入了\'符号'
				finally:
					row = row + 1
			else:
				row = row + 1

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
			# 翻译结果中的%S替换成%s防止出错
			if '%S' in baidu_word:
				baidu_word = baidu_word.replace('%S','%s')
			#判断是否是句子
			if '.' not in baidu_word and ',' not in baidu_word and '!' not in baidu_word and '%s' not in baidu_word and '%d' not in baidu_word:
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
	#tools.del_words()
	#tools.insert_words()
	#tools.replace_title()
	tools.find_repeat()
	#tools.replace_target()
	#tools.save_excel()