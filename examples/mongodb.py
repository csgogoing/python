#coding=utf-8
import sys
from time import sleep
import pymongo

class My_Mongo(object):
	"""docstring for mongo"""
	def __init__(self, data_name, collection_name):
		client = pymongo.MongoClient(host='localhost', port=27017)
		db = client[data_name]
		self.collection = db[collection_name]

	def insert(self, data):
		if type(data) == dict:
			result = self.collection.insert_one(data)
		elif type(data) == list:
			result = self.collection.insert_many(data)
		else:
			print('插入数据错误')
		return result.inserted_id

	def find(self, query):
		results = []
		result = self.collection.find(query)
		print(result)
		for i in result:
			print(i)
			print(type(i))
			results.append(i)
		return results


if __name__ == '__main__':
	#测试运行
	m_monge = My_Mongo('test', 'students')
	student = {
	'id':'20170101',
	'name':'kk',
	'age':20
	}
	abd = {"name":"kk"}
	#print(type(student) == dict)

	print(m_monge.find(abd))