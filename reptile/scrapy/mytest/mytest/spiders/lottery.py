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
		if  response is None:
			return
		soup = BeautifulSoup(response.text,'html.parser')
		items = self._get_new_data(soup)
		return items
		
	def _get_new_data(self, soup):
		#根据页面元素匹配获取数字
		item = MytestItem()
		items = []

		r_balls = soup.find_all('em', class_="rr")
		b_ball = re.findall(r'<em>(\d{2})</em>', str(soup))
		mydate = re.findall(r'align="center">(\d{4}-\d{2}-\d{2})', str(soup))

		for i in range(len(r_balls)):
			temp = i%6
			item['red_%d'%temp]=(r_balls[i].get_text())
			if temp == 5:
				item['blue']=b_ball.pop(0)
				item['m_date']=mydate.pop(0)
				items.append(item)

		return item