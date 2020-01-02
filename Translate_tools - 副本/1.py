import re

def main():
	a = None
	print(str(a))



#f = open('E_to_E','r',encoding='utf-8')
# f = open('C_to_E','r',encoding='utf-8')
# c=[]
# while f.readline():
# 	a = f.readline().replace('\n','')
# 	if a != '':
# 		b = a.split('	')
# 		c.append(b)
# d = dict(c)
# print(d.keys())
# a = '科目余额表'
# if a in d.keys():
# 	print(d[a])

# auxiliary = ['is','was','are','were','do','did','does','be']

# is_sentense = 1
# baidu_word = 'sdfsdf %Sfsdfsdfd'
# #判断是否是句子
# if '%S' in baidu_word:
# 	baidu_word = baidu_word.replace('%S','%s')
# if '.' not in baidu_word and ',' not in baidu_word and '!' not in baidu_word and '%s' not in baidu_word and '%d' not in baidu_word:
# 	baidu_list = baidu_word.split(' ')
# 	if len(baidu_list)>5:
# 		is_sentense = 1
# 	else:
# 		is_sentense = 0
# 		for tar in auxiliary:
# 			if tar in baidu_list:
# 				is_sentense = 1
# 				break
# #如果不是句子，首字母大写
# if is_sentense == 0:
# 	for i in range(len(baidu_list)):
# 		if re.search('[a-z]',baidu_list[i]):
# 			baidu_list[i]=baidu_list[i].title()
# 	baidu_word = ' '.join(baidu_list)
# print(baidu_word)


# id = 1
# chnword = '1'
# baidu_word = '1'
# sql = 'DELETE FROM table_name WHERE chn_word="%s";'%(baidu_word)
# print(sql)


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


if __name__ == '__main__':
	main()