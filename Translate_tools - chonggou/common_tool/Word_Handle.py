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


class Word_handle():
	#工具类
	def __init__(self):
		pass


	def replace_title(self, word):
		auxiliary = ['is','was','are','were','do','did','does','be']
		special_characters = ['% S', '% s', '%S', '\\ N', '\\N', '\\ n', '\\ R', '\\R','\\ r',\
							 '\\ T', '\\T', '\\ t', ' & ', '\'S', ' \\ ', ' / ', ' Of ', '-Of-']

		is_sentense = 1
		need_write = 0
		trans_word = str(word)
		if trans_word == 'None':
			print('--------------------------------')
			return(need_write,trans_word)
		#判断是否是句子
		if '.' not in trans_word and ',' not in trans_word and '!' not in trans_word and '?' not in trans_word:
			#没有句子符号，进行切分判断
			tans_list = trans_word.split(' ')
			if len(tans_list)>5:
				is_sentense = 1
			else:
				is_sentense = 0
				for aux in auxiliary:
					if aux in tans_list:
						is_sentense = 1
						break
		#如果不是句子，首字母大写
		if is_sentense == 0:
			need_write = 1
			for i in range(len(tans_list)):
				if re.search('[a-z]',tans_list[i]):
					tans_list[i]=tans_list[i].title()
			up_word = ' '.join(tans_list)
		else:
			need_write = 0
			up_word = trans_word
		# 翻译结果中的特殊内容替换成小写防止出错
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
				up_word = up_word.replace(' Of ','of')
				up_word = up_word.replace('-Of-','of')
				continue
		return(need_write,up_word)



	def replace_target(self, sheet):
		self.sheet = sheet

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



	def find_repeat(self, key_file):
		self.xlBook.Worksheets[0].Activate()
		self.sheet = self.xlBook.ActiveSheet

		#读取目标文件
		file_re = open(key_file,'r',encoding='utf-8')
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



	def replace_excel_title(self, sheet, colomn):
		self.sheet = sheet

		row = 2


		while self.sheet.Cells(row, 1).Value != None:
			print(row)
			trans_word = str(self.sheet.Cells(row, colomn).Value)
			is_trans = self.replace_title(trans_word)
			up_word = is_trans[1]
			if is_trans[0] == 1:
				try:
					#self.sheet.Cells(row, 3).Value = trans_word
					self.sheet.Cells(row, colomn).Value = up_word
					#self.sheet.Cells(row, 4).Value = '需要转换'
				except:
					self.sheet.Cells(row, colomn+2).Value = '写入表格失败'
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
				tans_list = baidu_word.split(' ')
				if len(tans_list)>5:
					is_sentense = 1
				else:
					is_sentense = 0
					for tar in auxiliary:
						if tar in tans_list:
							is_sentense = 1
							break
			#如果不是句子，首字母大写
			if is_sentense == 0:
				for i in range(len(tans_list)):
					if re.search('[a-z]',tans_list[i]):
						tans_list[i]=tans_list[i].title()
				baidu_word = ' '.join(tans_list)

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
				tans_list = baidu_word.split(' ')
				if len(tans_list)>7:
					is_sentense = 1
				else:
					is_sentense = 0
					for tar in auxiliary:
						if tar in tans_list:
							is_sentense = 1
							break
			#如果不是句子，首字母大写
			if is_sentense == 0:
				for i in range(len(tans_list)):
					if re.search('[a-z]',tans_list[i]):
						tans_list[i]=tans_list[i].title()
				baidu_word = ' '.join(tans_list)

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
	tools = Word_handle()
	#tools.del_words()
	#tools.insert_words()
	#tools.replace_title()
	print(tools.replace_title('sdfssf sdfss sdfs ooos sdf s'))
	#tools.replace_target()
	#tools.save_excel()