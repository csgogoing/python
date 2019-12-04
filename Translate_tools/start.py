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
from lxml import etree

#/html/body/div[3]/div[1]/div[3]/div[1]/div/a[15]
#//@class="listA"
def test():
	a = ['1世界的方式结合地方 sfsdfsdfs', 'sfsdfsf 1斯蒂芬斯蒂芬', 'sdfdsfds', '沙发上地方是', 'dsfds sdfsd 斯蒂芬斯蒂芬多少']
	for i in a:
		if re.match(r'^([0-9]).*',i):
			print(i)


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






def get_url():
	host = 'http://www.dongao.com'
	headers = {} 
	#url_get = ['http://www.dongao.com/practice/kjyy/','http://www.dongao.com/practice/kjyy/List_2.shtml','http://www.dongao.com/practice/kjyy/List_1.shtml']
	url_get = ['http://www.dongao.com/practice/kjyy/']
	url_parse = []
	url_result = []
	for url in url_get:
		req = requests.get(url=url)
		req_text = req.content.decode('GBK')
		tree = etree.HTML(req_text)
		url_parse_t = tree.xpath('//a[@class="listA"]/@href')
		url_parse = url_parse + url_parse_t

	for url in url_parse:
		url_result.append(host+url)
	return(url_result)


def parse_url(urls):
	excel_path = os.getcwd()
	f = open(excel_path + '/a', 'w', encoding='utf-8')
	for url in urls:
		req = requests.get(url=url)
		req_text = req.content.decode('GBK')
		pattern = re.compile(r'<P>\u3000\u3000(.*)</P>')
		word = pattern.findall(req_text)
		for i in word:
			if re.search(r'[\u4e00-\u9fa5]',i) and re.search(r'[a-zA-Z]',i):
				f.write(i)
				f.write('\n')
	f.close()


def txt_to_excel():
	f = open('1.txt', 'r', encoding='gbk')
	excel_path=os.getcwd()+'\\ERP.xlsx'
	rb = xlwt.Workbook()  #新建一个Excel
	sheet = rb.add_sheet(u'translate',cell_overwrite_ok=True) #新建sheet
	row = 1
	while True:
		next = f.readline()
		if next != '' and re.match(r'^([0-9]).*',next):
			tmp = next.split(' ')
			re_chn = tmp[-1].strip('\n')
			re_eng = " ".join('%s' %id for id in tmp[1:-1])
			# print(re_chn)
			# print(re_eng)
			sheet.write(row,0,re_chn)
			sheet.write(row,1,re_eng)
			row = row + 1
		else:
			break
	rb.save(excel_path)
	
	#示例写入方法s


def main():
	#test()
	# urls = get_url()
	# parse_url(urls)
	# we = Write_Excel(excel_path)
	txt_to_excel()



if __name__ == '__main__':
	main()