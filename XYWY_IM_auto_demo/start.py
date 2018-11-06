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
			if result == False:
				return
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
					self.my_doctor.answer_ques_20(i+2)
					sleep(1)
			else:
				print('times输入错误')
		
		else:
			result, order_id = self.my_ask.other_page(resource_id=source, q_type=q_type)
			if result == False:
				return
			qid = int(self.my_doctor.get_id(user_id))
			print(qid)
			self.my_doctor.take_question(qid)
			if times <= 1:
				self.my_doctor.answer_question(qid, is_summary)
			elif 1 < times < 21:
				self.my_doctor.answer_question(qid, is_summary)
				for i in range(times-1):
					self.my_ask.persue(qid, source, user_id)
					sleep(1)
					self.my_doctor.answer_ques_20(qid, i+2)
					sleep(1)
			else:
				print('times输入错误')

	def quit():
		self.driver.quit()



if __name__ == '__main__':
	A = Im_Test()

	#百度悬赏
	#A.run_test(source=200002, q_type=2, times=20, is_summary=1)
	#百度指定
	#A.run_test(source=200002, q_type=3, times=20, is_summary=1)
	#其他悬赏
	A.run_test(source='xywyapp', q_type=2, times=20, is_summary=1)
	A.quit()

	#下一步，区分来源，获取用户输入
	# "xywyapp"寻医问药APP
	# "pc"PC
	# "200002"百度
	# "xiaomi"小米
	# "hlwyy"互联网医院
	# "ywb"英威诺
	# "sgjk"搜狗健康

	while True:
		try:
			choose = int(input('''
				1：仅创建问题
				2：创建问题+回答
				3：创建问题+问答自定义轮次
				4：创建问题+问答20轮次
				其他：退出
请选择：'''))
		except:
			exit('感谢使用')
		else:
			my_ask = Ask()
			while True:
				if choose == 1:
					try:
						m_source = int(input('''
				问题类型：
					1：寻医问药APP
					2：PC
					3：百度
					4：小米
					5：互联网医院
					6：英威诺
					7：搜狗健康（暂时不支持）
					其他：退出
请选择：'''))
					except:
						exit('感谢使用')
					else:
						try:
							m_q_type = int(input('''
				问题类型：
					1：免费
					2：悬赏
					3：指定(医生ID：117333219)
					其他：退出
请选择：'''))			
						except:
							exit('感谢使用')
						else:
							if m_source == 1:
								source = 200002
								my_ask.baidu_page(m_q_type)

							elif m_source == 2:
								source = "xywyapp"
								my_ask.other_page(self, resource_id, uid=456654, q_type=2, doctor_ids=117333219, pay_type=1)

							elif m_source == 3:
								source = "pc"

							elif m_source == 4:
								source = "xiaomi"

							elif m_source == 5:
								source = "hlwyy"

							elif m_source == 6:
								source = "ywb"

							elif m_source == 7:
								print('暂不支持搜狗')

							else:
								break

				elif choose == 2:
					m_source = input('''
			问题类型：
				1：寻医问药APP
				2：PC
				3：百度
				4：小米
				5：互联网医院
				6：英威诺
				7：搜狗健康（暂时不支持）
				其他：退出
			免费悬赏指定：
				1：免费
				2：悬赏
				3：指定
	请选择：''')
				else:
					exit('感谢使用')