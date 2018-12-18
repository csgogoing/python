import xlrd
from xlutils.copy import copy

class write_result():
	def __init__(self, file):
		rb = xlrd.open_workbook(file)
		self.wb = copy(rb)
		self.ws = self.wb.get_sheet(0)
		self.ws.write(0, 9, '问题ID')
		self.ws.write(0, 10, '执行结果')
		self.wb.save('result.xls')

	def conclude(self, row, qid, result='流程正常结束'):
		self.ws.write(row, 9, '%s'%qid)
		self.ws.write(row, 10, '%s'%result)
		self.wb.save('result.xls')
