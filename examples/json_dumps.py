#coding=utf-8
import json

if __name__ == '__main__':
	#测试运行
	data = [{
		"name" : "123"
	}]
	with open('data.josn', 'w', encoding='utf-8') as file:
		file.write(json.dumps(data,indent=2, ensure_ascii=False))