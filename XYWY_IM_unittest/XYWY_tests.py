#coding=utf-8

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time, os


def send_mail(file_new):
	#发送邮件
	f = open(file_new, 'rb')
	mail_body = f.read()
	f.close()
	msg = smtplib.SMTP()
	smtp.connect("www.126.com")
	smtp.login("csgogoing@126.com","1234455")
	smtp.sendmail("","",msg.as_string())
	smtp.quit()
	print('email has sent')

def new_report(test_report):
	#文件排序
	lists = os.listdir(test_report)
	lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" +fn))
	file_new = os.path.join(test_report, lists[-1])
	print(file_new)
	return file_new

if __name__ == '__main__':
	#启动类
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = './xywy/report/' + now +'-result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(stream=fp,
							title = u'自动化测试报告',
							description=u'环境：windows7 浏览器：Firefox')
	discover = unittest.defaultTestLoader.discover('./xywy/test_case',
													pattern='*sta.py')
	runner.run(discover)
	fp.close()
	file_path = new_report('./xywy/report/')
