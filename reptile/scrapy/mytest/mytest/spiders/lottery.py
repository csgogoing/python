# -*- coding: utf-8 -*-
import scrapy
from ..items import MytestItem
from bs4 import BeautifulSoup
import re

class LotterySpider(scrapy.Spider):
	name = 'lottery'
	allowed_domains = ['kaijiang.zhcw.com']
	#start_urls = ['http://kaijiang.zhcw.com/']

	def start_requests(self):
	#主爬虫
		for i in range(1,2):
			url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%d.html' % i
			yield scrapy.Request(url=url, callback=self.parse)
 
	def parse(self, response):
		print(response)
		if  response is None:
			return
		soup = BeautifulSoup(response.text,'html.parser')
		self._get_new_data(soup)
		
	def _get_new_data(self, soup):
		#根据页面元素匹配获取数字
		item = MytestItem()
		
		r_balls = soup.find_all('em', class_="rr")

		for i in range(len(r_balls)):
			temp = i%6
			item['red_%d'%temp]=(r_balls[i].get_text())
		
		b_ball = soup.find_all('em', class_="")
		for data in b_ball:
			item['blue']=(data.get_text())
			print(item['blue'])
		
		mydate = soup.find_all('td', align='center')
		for edate in mydate:
			pattern = re.compile(r"[0-9]{7}")
			match = pattern.findall(edate.get_text())
			if match:
				item['m_date']=(match.pop())
		
		print(item['blue'])

		return item