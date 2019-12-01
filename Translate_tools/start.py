#coding=utf-8
import requests
import re
import os
from lxml import etree

#/html/body/div[3]/div[1]/div[3]/div[1]/div/a[15]
#//@class="listA"


def main():
	#test()
	urls = get_url()
	parse_url(urls)


def test():
	a = ['世界的方式结合地方 sfsdfsdfs', 'sfsdfsf 斯蒂芬斯蒂芬', 'sdfdsfds', '沙发上地方是', 'dsfds sdfsd 斯蒂芬斯蒂芬多少']
	for i in a:
		if re.search(r'[\u4e00-\u9fa5]',i) and re.search(r'[a-zA-Z]',i):
			print(i)



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


if __name__ == '__main__':
	main()