#coding=utf-8
from .base import Page
import time
from time import sleep
from urllib import request, parse

class Ask(object):
	'''
	提问类
	'''
	self.msg_id_origin = 0

	def persue(self, qid, resource_id, user_id):
		#追问接口
		headers = {
			'Connection': 'keep-alive',
			'Content-Type': 'application/x-www-form-urlencoded'
		}

		data = {
			'qid': qid,
			'resource_id': resource_id,
			'user_id': user_id,
			#'expert_id': '68258667',
			'content': '{"type":"text","text":"测试显示%d" %(self.msg_id_origin)}',
			'msg_id': '%s' %(self.msg_id_origin),
			'atime': '%d' %(int(time.time())),
			'sign': '123'
		}
		self.msg_id_origin = self.msg_id_origin + 1
		data = parse.urlencode(data).encode('utf-8')
		req = request.Request('http://test.d.xywy.com/socket/ask', headers=headers, data=data)
		try:
			page = request.urlopen(req).read()
			page = page.decode('utf-8')
		except error.HTTPError as e:
			print(e.code())
			print(e.read()).devode('utf-8')
		return page

	def baidu_page(self, q_type, uid=456654, doctor_ids=68258667, pay_amount=300, firset_dep='内科', second_dep='呼吸内科'):
		#百度来源提问
		now_time = int(time.time())
		headers = {
			'Connection': 'keep-alive',
			'Content-Type': 'application/x-www-form-urlencoded'
		}

		data = {
			'qid': '%d'%(now_time),
			'resource_id': 200002,
			'user_id': uid,
			'patient_name': '张三',
			'patient_sex': 1,
			'patient_age': 20,
			'patient_age_month': 0,
			'patient_age_day': 0,
			'patient_phone': 17888888888,
			'content': '百度感冒怎么办%d' %(self.msg_id_origin),
			'pic_urls': '',
			'q_type': q_type,
			'order_id': 'rtqa_%d' %(now_time),
			'doctor_ids': doctor_ids,
			'pay_type': 1,
			'pay_amount': pay_amount,
			'firset_dep': firset_dep,
			'second_dep': second_dep
		}
		if data['q_type'] == 3:
			del data['pay_amount']
			data['price'] = pay_amount
		data = parse.urlencode(data).encode('utf-8')
		req = request.Request(url, headers=headers, data=data)
		try:
			page = request.urlopen(req).read()
			page = page.decode('utf-8')
		except error.HTTPError as e:
			print(e.code())
			print(e.read()).devode('utf-8')
		return page

	def other_page(self, resource_id, uid=456654, q_type=2, doctor_ids=68258667, pay_type=1):
		#其他来源提问
		now_time = int(time.time())
		headers = {
			'Connection': 'keep-alive',
			'Content-Type': 'application/x-www-form-urlencoded'
		}

		data = {
			'qid': '%d'%(now_time),
			'source': resource_id,
			'uid': uid,
			'patient_name': '张三',
			'patient_sex': 1,
			'patient_age': 20,
			'patient_age_month': 0,
			'patient_age_day': 0,
			'patient_phone': 17888888888,
			'content': '%s感冒怎么办%d' %(resource_id, self.msg_id_origin),
			'pic_urls': '',
			'q_type': q_type,
			'order_id': 'rtqa_%d' %(now_time),
			'doctor_ids': doctor_ids,
			'pay_type': 1,
			'pay_amount': 300,
			'title': 'title',
			'intent': 'intent',
			'hospital': 0
		}
		data = parse.urlencode(data).encode('utf-8')
		req = request.Request(url, headers=headers, data=data)
		try:
			page = request.urlopen(req).read()
			page = page.decode('utf-8')
		except error.HTTPError as e:
			print(e.code())
			print(e.read()).devode('utf-8')
		return page

	def sougou_page():
		pass
if __name__ == '__main__':
	#测试运行
	A = Ask()
	#A.baidu_page('http://test.d.xywy.com/socket/ask')
	A.other_page('http://test.api.d.xywy.com/user/question/ask?safe_source_tag_wws=DJWE23_oresdf@ads')
	now_time = int(time.time())
	data = {'qid': '%d'%(now_time)}
