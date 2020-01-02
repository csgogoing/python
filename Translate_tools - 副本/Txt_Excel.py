def txt_to_excel():
	f = open('ERP.txt', 'r', encoding='gbk')
	excel_path=os.getcwd()+'\\ERP.xls'
	rb = xlwt.Workbook()  #新建一个Excel
	sheet = rb.add_sheet(u'translate',cell_overwrite_ok=True) #新建sheet
	row = 1
	while True:
		next = f.readline()
		if next == '':
			break
		elif re.match(r'^([0-9]).*',next):
			tmp = next.split(' ')
			re_chn = tmp[-1].strip('\n')
			re_eng = " ".join('%s' %id for id in tmp[1:-1])
			print(re_chn)
			print(re_eng)
			sheet.write(row,0,re_chn)
			sheet.write(row,1,re_eng)
			row = row + 1
		else:
			pass
	rb.save(excel_path)

if __name__ == '__main__':
	txt_to_excel()