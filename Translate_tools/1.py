a = [
	[
		["Stubborn child", "顽固子弟", 'null', 'null', 3, 'null', 'null', 'null', [
			[
				["2d872eccc9e3cd77b6198222b546ff3f", "zh_en_2019q4.md"]
			]
		]],
		['null', 'null', 'null', "Wángù zǐdì"]
	], 'null', "zh-CN", 'null', 'null', [
		["顽固子弟", 'null', [
				["Stubborn child", 0, 1, 0],
				["Stubborn children", 0, 1, 0]
			],
			[
				[0, 4]
			], "顽固子弟", 0, 0
		]
	], 1.0, ["\u003cem\u003e纨绔\u003c/em\u003e子弟", "纨绔子弟", [1], 'null', 'null', 0],
	[
		["zh-CN"], 'null', [1.0],
		["zh-CN"]
	], 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', ['null', 2]
]

b = [
	[
		['Activity Based Management', '基于作业活动管理', None, None, 3, None, None, None, [
			[
				['2d872eccc9e3cd77b6198222b546ff3f', 'zh_en_2019q4.md']
			]
		]],
		[None, None, None, 'Jīyú zuòyè huódòng guǎnlǐ']
	], None, 'zh-CN', None, None, 
	[
		['基于作业活动管理', None, [
				['Activity Based Management', 0, True, False],
				['Activity - based management', 0, True, False]
			],
			[
				[0, 8]
			], '基于作业活动管理', 0, 0
		]
	], 1.0, [],
	[
		['zh-CN'], None, [1.0],
		['zh-CN']
	]
]

print(a[7][0].replace('<em>','').replace('</em>',''))
print(b[7]==[])



# a = [1,2,3,4]
# b = '.'.join(a)
# print(b)

# def get_url():
# 	host = 'http://www.dongao.com'
# 	headers = {} 
# 	#url_get = ['http://www.dongao.com/practice/kjyy/','http://www.dongao.com/practice/kjyy/List_2.shtml','http://www.dongao.com/practice/kjyy/List_1.shtml']
# 	url_get = ['http://www.dongao.com/practice/kjyy/']
# 	url_parse = []
# 	url_result = []
# 	for url in url_get:
# 		req = requests.get(url=url)
# 		req_text = req.content.decode('GBK')
# 		tree = etree.HTML(req_text)
# 		url_parse_t = tree.xpath('//a[@class="listA"]/@href')
# 		url_parse = url_parse + url_parse_t

# 	for url in url_parse:
# 		url_result.append(host+url)
# 	return(url_result)


# def parse_url(urls):
# 	excel_path = os.getcwd()
# 	f = open(excel_path + '/a', 'w', encoding='utf-8')
# 	for url in urls:
# 		req = requests.get(url=url)
# 		req_text = req.content.decode('GBK')
# 		pattern = re.compile(r'<P>\u3000\u3000(.*)</P>')
# 		word = pattern.findall(req_text)
# 		for i in word:
# 			if re.search(r'[\u4e00-\u9fa5]',i) and re.search(r'[a-zA-Z]',i):
# 				f.write(i)
# 				f.write('\n')
# 	f.close()
