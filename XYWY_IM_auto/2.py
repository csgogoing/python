import xlrd
from xlutils.copy import copy

class write_result():
	def __init__(self, file):
		rb = xlrd.open_workbook(file)
		self.wb = copy(rb)
		self.ws = self.wb.get_sheet(0)

	def conclude(self, row, qid, result='问答流程正常结束'):
		self.ws.write(row, 10, '%s'%qid)
		self.ws.write(row, 11, '%s'%result)
		self.wb.save('result.xls')
