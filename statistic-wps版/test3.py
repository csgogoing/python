from win32com.client import Dispatch  
import win32com.client


#下面是一些测试代码。  
if __name__ == "__main__":  
	wpsApp=win32com.client.Dispatch("ket.Application")
	#设置界面可见
	wpsApp.Visible=0
	#新建一个wps工作簿
	xlBook = wpsApp.Workbooks.Open(r"C:\Users\Administrator\Desktop\statistic\1.xls",ReadOnly=0,Editable=1)
	cell = xlBook.ActiveSheet.Cells(1,1)
	cell.Value='one'
	xlBook.SaveAs(r"C:\Users\Administrator\Desktop\statistic\2.xls")
	xlBook.Close()

	#选定工作簿中活动工作表的某个单元格
	# cell = xlBook.ActiveSheet.Cells(1,1)
	# #设置单元格的值
	# cell.Value='one'
	# #保存工作簿
	# xlBook.SaveAs(r"c:/HelloWorld.xls")
	# xlBook.Close()