#coding=utf-8
import requests
import re
import os
import sys
import random
import time
from time import sleep
from Mysql_Use import Mysql


class Mysql_word(object):
	"""docstring for Mysql_word"""
	def __init__(self, table):
		self.mysql = Mysql(table)
		

	def mysql_replace_target(sef, file_name):
		#读取目标文件
		file_OT = open(file_name,'r',encoding='utf-8')
		word_lists_OT=[]

		while file_OT.readline():
			word_line_OT = file_OT.readline().replace('\n','')
			if word_line_OT != '':
				words_kv_OT = word_line_OT.split('	')
				word_lists_OT.append(words_kv_OT)
		words_dict_OT = dict(word_lists_OT)

		search_sql = 'select from common_words where chn_word="%s"'
		update_sql = 'update common_words set baidu_word="%s" where chn_word="%s");'
		for target_E in words_dict_OT.keys():
			s_sql = search_sql.format(target_E)
			search_result = self.mysql.query(s_sql)
			if search_result:
				u_sql = update_sql.format(words_dict_OT[target_E],target_E)
				update_result = self.mysql.exec(u_sql)
				if update_result=='wrong':
					print(target_E)







if __name__ == '__main__':
	a = Mysql_word('multilang')
	a.mysql_replace_target('find_re')