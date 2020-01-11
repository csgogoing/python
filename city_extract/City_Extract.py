import requests
import re
import os
import sys
import xlrd
import xlwt
import time
import json
import win32com.client
from lxml import etree


from time import sleep


class City_extract():
	#主类
	def __init__(self):
		pass


	def open_excel(self, file_name, sheet=0):
		self.wpsApp = win32com.client.Dispatch("Excel.Application")
		self.wpsApp.Visible = 1
		ERP_path = os.getcwd() + '\\' + file_name
		if os.path.exists(ERP_path):
			self.xlBook = self.wpsApp.Workbooks.Open(ERP_path, ReadOnly=0, Editable=1)
			print('已找到ERP表格')
		else:
			sys.exit('当前目录下未找到ERP表格')
		self.xlBook.Worksheets[sheet].Activate()
		self.sheet = self.xlBook.ActiveSheet


	def Search_IATA(self, Three_code):
		#Search_IATA，并返回结果
		url = 'https://www.iata.org/AirportCodesSearch/Search?currentBlock=314384&currentPage=12572&search=%s'%Three_code
		req = requests.get(url)
		elements = etree.HTML(req.text)
		try:
			city_name = elements.xpath('//tbody/tr[1]/td[1]/text()')[0]
			city_code = elements.xpath('//tbody/tr[1]/td[2]/text()')[0]
			air_code = elements.xpath('//tbody/tr[1]/td[4]/text()')[0]
		except IndexError:
			return('','无数据')
		else:
			if city_code == Three_code:
				return(city_name,'城市')
			elif air_code == Three_code:
				return(city_name,'机场')
			else:
				return('','错误')



	def Handle_data(self, needc=4, tcol=10, row=2):
		#读取数据,调用Search_IATA，读取结果，并写入
		while self.sheet.Cells(row, needc).Value != None:
			print('当前替换第%s行'%(row))
			t_code = str(self.sheet.Cells(row, needc).Value)
			result = self.Search_IATA(t_code)
			self.sheet.Cells(row, tcol).Value= result[1]
			self.sheet.Cells(row, tcol+1).Value= result[0]
			row = row + 1



if __name__ == '__main__':

	tools = City_extract()

	tools.open_excel('City_List.xlsx')
	tools.Handle_data(needc=4, tcol=10, row=8214)

	#tools.save_excel()
