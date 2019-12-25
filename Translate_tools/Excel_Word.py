#coding=utf-8
import requests
import re
import os
import sys
import random
import xlrd
import xlwt
import time
import json
import win32com.client
from xlutils.copy import copy
from time import sleep
from Mysql_Use import Mysql
from Google_Translate import Google_translate


class Translate_Excel():
	#主类
	def __init__(self, file_name, sheet):
		ERP_path = os.getcwd()+'\\Excel\\' + file_name
		#ERP_path = os.getcwd()+'\\ERP6-9.xls'
		if os.path.exists(ERP_path):
			self.wpsApp = win32com.client.Dispatch("Excel.Application")
			self.wpsApp.Visible = 1
			self.xlBook = self.wpsApp.Workbooks.Open(ERP_path, ReadOnly=0, Editable=1)
			print('已找到ERP表格')
		else:
			sys.exit('当前目录下未找到ERP表格')
		self.xlBook.Worksheets[sheet].Activate()
		self.sheet = self.xlBook.ActiveSheet


	def save_excel(self):
		#保存Excel
		self.xlBook.Save()
		self.xlBook.Close(True)
		self.wpsApp.Quit()


	def replace_title(self, word):
		auxiliary = ['is','was','are','were','do','did','does','be']
		special_characters = ['% S', '% s', '%S', '% d','% D','%D', '\\ N', '\\N', '\\ n', '\\ R', '\\R','\\ r',\
							 '\\ T', '\\T', '\\ t', ' & ', '\'S', ' \\ ', ' / ', ' Of ', '-Of-'\
							 , ' And ', '-And-', '：', '，', '。', '！', '？', '\\ "', '% 1', '% 2','% 3']

		is_sentense = 1
		need_write = 0
		trans_word = str(word)

		if trans_word == 'None':
			return(need_write,trans_word)

		# 翻译结果中的特殊内容替换成小写防止出错
		for characters in special_characters:
			if characters in trans_word:
				need_write = 1
				trans_word = trans_word.replace('% S','%s')
				trans_word = trans_word.replace('% s','%s')
				trans_word = trans_word.replace('%S','%s')
				trans_word = trans_word.replace('% D','%d')
				trans_word = trans_word.replace('% d','%d')
				trans_word = trans_word.replace('%D','%d')
				trans_word = trans_word.replace('\\ N','\\n')
				trans_word = trans_word.replace('\\N','\\n')
				trans_word = trans_word.replace('\\ n','\\n')
				trans_word = trans_word.replace('\\ R','\\r')
				trans_word = trans_word.replace('\\R','\\r')
				trans_word = trans_word.replace('\\ r','\\r')
				trans_word = trans_word.replace('\\ T','\\t')
				trans_word = trans_word.replace('\\T','\\t')
				trans_word = trans_word.replace('\\ t','\\t')
				trans_word = trans_word.replace('\'S','\'s')
				trans_word = trans_word.replace(' Of ','of')
				trans_word = trans_word.replace('-Of-','of')
				trans_word = trans_word.replace(' And ',' and ')
				trans_word = trans_word.replace('-And-','-and-')

				continue
		#判断是否是句子
		if '.' not in trans_word and ',' not in trans_word and '!' not in trans_word and '?' not in trans_word:
			#没有句子符号，进行切分判断
			trans_list = trans_word.split(' ')
			if len(trans_list)>5:
				is_sentense = 1
			else:
				is_sentense = 0
				for aux in auxiliary:
					if aux in trans_list:
						is_sentense = 1
						break
		#如果不是句子，首字母大写
		if is_sentense == 0:
			need_write = 1
			for i in range(len(trans_list)):
				if re.search('[a-z]',trans_list[i]):
					trans_list[i]=trans_list[i].title()
			up_word = ' '.join(trans_list)
		else:
			up_word = trans_word
		# 替换结果中的特殊内容替换成小写防止出错
		for characters in special_characters:
			if characters in up_word:
				need_write = 1
				up_word = up_word.replace('% S','%s')
				up_word = up_word.replace('% s','%s')
				up_word = up_word.replace('%S','%s')
				up_word = up_word.replace('% D','%d')
				up_word = up_word.replace('% d','%d')
				up_word = up_word.replace('%D','%d')
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
				up_word = up_word.replace(' And ',' and ')
				up_word = up_word.replace('-And-','-and-')
				up_word = up_word.replace('：',':')
				up_word = up_word.replace('，',', ')
				up_word = up_word.replace('。','. ')
				up_word = up_word.replace('！','! ')
				up_word = up_word.replace('？','? ')
				up_word = up_word.replace('？','? ')
				up_word = up_word.replace('\\ "','\\"')
				up_word = up_word.replace('% 1','%1')
				up_word = up_word.replace('% 2','%2')
				up_word = up_word.replace('% 3','%3')

				continue
		# %s前增加空格
		if '%s' in up_word and ' %s' not in up_word and '<%s' not in up_word and '(%s' not in up_word \
			and '-%s' not in up_word and ':%s' not in up_word and '[%s' not in up_word and '"%s' not in up_word:
			need_write = 1
			up_word = up_word.replace('%s',' %s')

		# of后面紧跟着大写字母的，在of两侧加空格
		def of_space(tar):
			word = tar.group()
			return word.replace('of',' of ')
		if re.search(r'\Bof[A-Z]',up_word):
			need_write = 1
			print(up_word)
			up_word = re.sub(r'\Bof[A-Z]', of_space, up_word)
			print(up_word)

		return(need_write,up_word)


	def excel_replace_title(self, col=2, row=2):
		while self.sheet.Cells(row, 1).Value != None:
			print(row)
			trans_word = str(self.sheet.Cells(row, col).Value)
			is_trans = self.replace_title(trans_word)
			up_word = is_trans[1]
			if is_trans[0] == 1:
				try:
					if re.match(r'^\'',up_word):
						self.sheet.Cells(row, col).Value= '\'' + up_word
					else:
						self.sheet.Cells(row, col).Value=up_word
				except:
					self.sheet.Cells(row, col+2).Value = '写入表格失败'
			row = row + 1


	def excel_translate_google(self, needc=1, toc=2, row=2):
		#实例化翻译类
		self.tran_google = Google_translate()

		#找到当前未翻译的位置
		while self.sheet.Cells(row, toc).Value != None:
			row = row + 1
		
		while self.sheet.Cells(row, needc).Value != None:
			sleep(1)
			print('当前第%s行'%(row))
			chn_word = str(self.sheet.Cells(row,needc).Value)
			if not re.search(r'[\u4e00-\u9fa5]',chn_word):
				try:
					self.sheet.Cells(row, toc).Value= ''
				except Exception as e:
					self.sheet.Cells(row, toc).Value= '\''
					self.sheet.Cells(row, toc+1).Value='写入了\'符号'
				finally:
					row = row + 1
			else:
				result = str(self.tran_google.google_translate(chn_word))
				#result = str(self.test(chn_word))
				if result != '':
					try:
						if re.search(r'[\u4e00-\u9fa5]',result):
							print('未完整翻译')
							self.sheet.Cells(row, toc+1).Value='未完整翻译'
						else:
							pass
						if re.match(r'^\'',result):
							print(result)
							self.sheet.Cells(row, toc).Value= '\'' + result
						else:
							self.sheet.Cells(row, toc).Value=result
					except Exception as e:
						self.sheet.Cells(row, toc).Value= '\'' + result
						self.sheet.Cells(row, toc+1).Value='写入了\'符号'
				else:
					print('第%s行数据翻译失败'%row)
					self.sheet.Cells(row, toc+1).Value='未翻译'
				row = row + 1


	def replace_target(self, file_name, ori_r=1, bac_r=3, row=2):

		#读取目标文件
		file_OT = open(file_name,'r',encoding='utf-8')
		word_lists_OT=[]

		while file_OT.readline():
			word_line_OT = file_OT.readline().replace('\n','')
			if word_line_OT != '':
				words_kv_OT = word_line_OT.split('	')
				word_lists_OT.append(words_kv_OT)
		words_dict_OT = dict(word_lists_OT)

		while self.sheet.Cells(row, ori_r).Value != None:
			print(row)
			target_E = str(self.sheet.Cells(row, ori_r).Value)
			if target_E in words_dict_OT.keys():
				self.sheet.Cells(row, bac_r).Value = target_E
				replaced_word = words_dict_OT[target_E]

			result_word = self.replace_title(replaced_word)
			self.sheet.Cells(row, ori_r).Value = result_word
			row = row + 1

		file_OT.close()


	def find_repeat(self, file_name, tar_r, res_r, row=2):

		#读取目标文件
		file_re = open(file_name,'r',encoding='utf-8')
		word_lists_re=[]

		while file_re.readline():
			word_line_re = file_re.readline().replace('\n','')
			if word_line_re != '':
				word_lists_re.append(word_line_re)

		while self.sheet.Cells(row, tar_r).Value != None:
			print(row)
			target_e = str(self.sheet.Cells(row, tar_r).Value)
			if target_e in word_lists_re:
				print(target_e)
				self.sheet.Cells(row, 3).Value = '存在重复'

			row = row + 1
		file_re.close()


	def mysql_del_words(self):
		mysql = Mysql('multilang')

		row = 2
		while self.sheet.Cells(row, 1).Value != None:
			need_del_word = self.sheet.Cells(row, 1).Value
			#select_sql = 'update common_words set id=%d, chn_word="%s", baidu_word="%s");'%(id,chn_word,baidu_word)

			update_sql = 'DELETE FROM common_words WHERE chn_word="%s";'%(need_del_word)
			print(update_sql)
			result = mysql.exec(update_sql)
			row = row + 1


	def mysql_insert_words(self):
		mysql = Mysql('multilang')

		#找到当前未翻译的位置
		row = 2

		while self.sheet.Cells(row, 1).Value != None:
			print('当前写入第%s行'%(row))
			id = row -1
			chn_word = str(self.sheet.Cells(row,1).Value)
			baidu_word = str(self.sheet.Cells(row,2).Value)
			up_result = self.replace_title(baidu_word)

			sql = 'insert into common_words(id, chn_word, baidu_word) values(%d,"%s","%s");'%(id,chn_word,up_result[1])
			print(sql)
			result = mysql.exec(sql)
			if result == 'wrong':
				sql = "insert into common_words(id, chn_word, baidu_word) values(%d,'%s','%s');"%(id,chn_word,up_result[1])
				print(sql)
				result = mysql.exec(sql)
				if result == 'wrong':
					self.sheet.Cells(row, 4).Value='写入数据库失败'
			row = row + 1


	def mysql_select_write_words(self):
		mysql = Mysql('multilang')

		#找到当前未翻译的位置
		row = 2

		while self.sheet.Cells(row, 1).Value != None:
			print('当前写入第%s行'%(row))
			chn_word = str(self.sheet.Cells(row,1).Value)

			sql = 'select from common_words where chn_word="%s");'%(chn_word)
			#加个判断在这里
			result = mysql.query(sql)
			if result == None:
				sql = "select from common_words where chn_word='%s');"%(chn_word)
				result = mysql.query(sql)
				if result == None:
					self.sheet.Cells(row, 4).Value='查询不到数据'
			row = row + 1


	def find_target(self, tar, col=2, row=2):
		while self.sheet.Cells(row, 1).Value != None:
			print(row)
			word = str(self.sheet.Cells(row, col).Value)
			if tar in word:
				self.sheet.Cells(row, col+2).Value = '匹配目标'
				result = self.replace_title(word)
				self.sheet.Cells(row, col+1).Value = result[1]
			row = row + 1




if __name__ == '__main__':
	tools = Translate_Excel('need_trans_1225.xlsx',sheet=0)
	#tools.mysql_insert_words()
	#tools.find_target(tar='?', col=2, row=2)
	#记得表格设置成文本格式
	#tools.excel_translate_google(needc=1, toc=2, row=2)
	tools.excel_replace_title(col=2, row=2)

	# tools.replace_target('C_to_E', ori_r=1, bac_r=3, row=2):
	# tools.find_repeat('find_re', ori_r=1, bac_r=3, row=2)

	#tools.save_excel()