import xlrd
from xlutils.copy import copy

class write_result():
	def __init__(self, file):
		rb = xlrd.open_workbook(file)
		self.wb = copy(rb)
		self.ws = self.wb.get_sheet(0)
		self.ws.write(0, 10, '问题ID')
		self.ws.write(0, 11, '执行结果')
		self.wb.save('result.xls')

	def write_in(self, sheet, row, column, result):
		self.ws.write(row, column, '%s'%result)

	def save(self, sheet, row, column, result):
		self.wb.save('result.xls')
