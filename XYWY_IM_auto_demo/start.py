from time import sleep
from base import Page
from im_ask import Ask
from im_doc_answer import login

class Im_Test():
	u'''寻医问药IM提问测试'''
	my_doctor = login()
	my_doctor.login_doctor()
	my_ask = Ask()

	def run_test(self, source=200002, user_id=456654, q_type=2, pay_amount=300, times=20, is_summary=0):
		if source==200002:
			result, order_id = self.my_ask.baidu_page(q_type)
			if 'Success!' in result:
				print('提问成功')
			else:
				print('提问失败')
				return
			print(user_id)
			qid = int(self.my_doctor.get_id(user_id))
			print(qid)
			if q_type in (1,2):
				self.my_doctor.take_question(qid)
			if times <= 1:
				self.my_doctor.answer_question(qid, is_summary)
			elif 1 < times < 21:
				self.my_doctor.answer_question(qid, is_summary)
				for i in range(times-1):
					self.my_ask.persue(order_id, source, user_id)
					sleep(1)
					self.my_doctor.answer_ques_20(qid, i+2)
					sleep(1)
			else:
				print('times输入错误')
		
		else:
			result = self.my_ask.other_page(resource_id=source, q_type=q_type)
			if 'Success!' in result:
				print('提问成功')
			else:
				print('提问失败')
				return
			print(user_id)
			qid = int(self.my_doctor.get_id(user_id))
			print(qid)
			self.my_doctor.take_question(qid)
			if times <= 1:
				self.my_doctor.answer_question(qid, is_summary)
			elif 1 < times < 21:
				self.my_doctor.answer_question(qid, is_summary)
				for i in range(times-1):
					self.my_ask.persue(order_id, source, user_id)
					sleep(1)
					self.my_doctor.answer_ques_20(qid, i+2)
					sleep(1)
			else:
				print('times输入错误')




if __name__ == '__main__':
	A = Im_Test()
	#百度悬赏
	#A.run_test(source=200002, q_type=2, times=20, is_summary=1)
	#百度指定
	#A.run_test(source=200002, q_type=3, times=20, is_summary=1)
	#小米悬赏
	#A.run_test(source=200002, q_type=2, times=20, is_summary=1)

	#下一步，区分来源，获取用户输入
	# "xywyapp"寻医问药APP
	# "pc"PC
	# "200002"百度
	# "xiaomi"小米
	# "hlwyy"互联网医院
	# "ywb"英威诺
	# "sgjk"搜狗健康