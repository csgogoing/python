#coding=utf-8

from selenium import webdriver
import os


def insert_image(driver, file_name):
	#保留截图
	base_dir = os.path.abspath(__file__)
	base_dir = str(base_dir)
	base_dir = base_dir.replace('\\','/')
	base = base_dir.split('/test_case')[0]
	file_path = base + '/report/image/' + file_name
	driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
	#测试截图功能
	driver = webdriver.Chrome()
	driver.get("http://www.baidu.com")
	insert_image(driver, 'test_baidu.jpg')
	driver.quit()
