#coding=utf-8
import time
import os
import xlrd

testvar = 1
for i in range(3):
	if 'testvar' in dir():
		print('有定义')
		del testvar
	else:
		print('没定义')



#if __name__ == '__main__':
