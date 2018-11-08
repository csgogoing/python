from time import sleep
from base import Page
from im_ask import Ask
from im_doc_answer import login
import re

class Im_Test():
	def __init__(self, did=117333219):
		my_doctor = login()
		my_doctor.login_doctor(did)
		my_ask = Ask()

	def run_test(self, source=200002, q_type=2, pay_amount=300, times=20, is_summary=0, user_id=456654):
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
		elif source == 7:
			print('不支持搜狗来源')
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
	#百度悬赏
	#A.run_test(source=200002, q_type=2, times=20, is_summary=1)
	#百度指定
	#A.run_test(source=200002, q_type=3, times=20, is_summary=1)
	#其他悬赏
	#A.run_test(source='xywyapp', q_type=2, times=20, is_summary=1)
	#A.quit()

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
				3：创建问题+问答20轮次
				4：创建问题+问答自定义
				其他：退出
请选择：'''))
		except:
			exit('感谢使用')
		else:
			while True:
				#选择为1
				if choose == 1:
					my_ask = Ask()
					try:
						m_source = int(input('''
				问题类型：
					1：百度
					2：寻医问药APP
					3：PC
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
				提问类型：
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
								my_ask.baidu_page(m_q_type, user_id=456654, doctor_ids=117333219, pay_amount=300, firset_dep='内科', second_dep='呼吸内科')

							elif m_source == 2:
								source = "xywyapp"
								my_ask.other_page(self, source, uid=456654, q_type=m_q_type, doctor_ids=117333219, pay_type=1)

							elif m_source == 3:
								source = "pc"
								my_ask.other_page(self, source, uid=456654, q_type=m_q_type, doctor_ids=117333219, pay_type=1)

							elif m_source == 4:
								source = "xiaomi"
								my_ask.other_page(self, source, uid=456654, q_type=m_q_type, doctor_ids=117333219, pay_type=1)

							elif m_source == 5:
								source = "hlwyy"
								my_ask.other_page(self, source, uid=456654, q_type=m_q_type, doctor_ids=117333219, pay_type=1)

							elif m_source == 6:
								source = "ywb"
								my_ask.other_page(self, source, uid=456654, q_type=m_q_type, doctor_ids=117333219, pay_type=1)

							elif m_source == 7:
								print('暂不支持搜狗')

							else:
								break

				#选择为2
				elif choose ==2:
					try:
						m_source = int(input('''
				问题类型：
					1：百度
					2：寻医问药APP
					3：PC
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
				提问类型：
					1：免费
					2：悬赏
					3：指定(医生ID：117333219)
					其他：退出
请选择：'''))			
						except:
							exit('感谢使用')
						else:
							test_2 =  Im_Test()
							if m_source == 1:
								source = 200002
								test_2.run_test(source=source, user_id=456654, q_type=m_q_type, pay_amount=300, times=1, is_summary=0)

							elif m_source == 2:
								source = "xywyapp"
								test_2.run_test(source=source, user_id=456654, q_type=m_q_type, pay_amount=300, times=1, is_summary=0)

							elif m_source == 3:
								source = "pc"
								test_2.run_test(source=source, user_id=456654, q_type=m_q_type, pay_amount=300, times=1, is_summary=0)

							elif m_source == 4:
								source = "xiaomi"
								test_2.run_test(source=source, user_id=456654, q_type=m_q_type, pay_amount=300, times=1, is_summary=0)

							elif m_source == 5:
								source = "hlwyy"
								test_2.run_test(source=source, user_id=456654, q_type=m_q_type, pay_amount=300, times=1, is_summary=0)

							elif m_source == 6:
								source = "ywb"
								test_2.run_test(source=source, user_id=456654, q_type=m_q_type, pay_amount=300, times=1, is_summary=0)

							elif m_source == 7:
								print('暂不支持搜狗')

							else:
								break

				elif choose == 3:
					try:
						m_source = int(input('''
				问题类型：
					1：百度
					2：寻医问药APP
					3：PC
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
				提问类型：
					1：免费
					2：悬赏
					3：指定(医生ID：117333219)
					其他：退出
请选择：'''))			
						except:
							exit('感谢使用')
						else:
							try:
								is_summary = int(input('''
				是否写总结：
					0：不写总结
					非0数字：写总结
					非数字：退出
请选择：'''))			
							except:
								exit('感谢使用')
							else:
								test_3 =  Im_Test()
								if m_source == 1:
									source = 200002
									test_3.run_test(source=source, user_id=456654, q_type=m_q_type, pay_amount=300, times=20, is_summary=is_summary)

								elif m_source == 2:
									source = "xywyapp"
									test_3.run_test(source=source, user_id=456654, q_type=m_q_type, pay_amount=300, times=20, is_summary=is_summary)

								elif m_source == 3:
									source = "pc"
									test_3.run_test(source=source, user_id=456654, q_type=m_q_type, pay_amount=300, times=20, is_summary=is_summary)

								elif m_source == 4:
									source = "xiaomi"
									test_3.run_test(source=source, user_id=456654, q_type=m_q_type, pay_amount=300, times=20, is_summary=is_summary)

								elif m_source == 5:
									source = "hlwyy"
									test_3.run_test(source=source, user_id=456654, q_type=m_q_type, pay_amount=300, times=20, is_summary=is_summary)

								elif m_source == 6:
									source = "ywb"
									test_3.run_test(source=source, user_id=456654, q_type=m_q_type, pay_amount=300, times=20, is_summary=is_summary)

								elif m_source == 7:
									print('暂不支持搜狗')

								else:
									break

				elif choose == 4:
					try:
						m_source = input('''
				一.问题类型：
					1：百度
					2：寻医问药APP
					3：PC
					4：小米
					5：互联网医院
					6：英威诺
					7：搜狗健康（暂时不支持）
					其他：退出
				二.提问类型：
					1：免费
					2：悬赏
					3：指定
					其他：退出
				三.金额(数字，单位分，默认300)
				四.问答轮次(数字，默认1)
				五.医生ID(数字，默认117333219)
				六.是否写总结(默认不写总结)
					0：不写总结
					非0数字：写总结
					非数字：退出
				七.患者ID(数字，默认456654)

			请以逗号分隔，输入所有内容，需按顺序输入，可以为空
			如(1,2,,15)表示百度-悬赏-问答15轮次
请输入：''')
					pat = re.split(r'[,，]',m_source)  
					except:
						exit('感谢使用')
					else:
						#初始化赋值
						source = 200002
						q_type = 2
						pay_amount = 300
						times = 20
						did = 117333219
						is_summary = 0
						user_id = 456654
						#循环赋值
						for i in range(len(pat))
							if i == 0:
								source = pat[i]
							elif i == 1:
								q_type = pat[i]
							elif i == 2:
								pay_amount = pat[i]
							elif i == 3:
								times = pat[i]
							elif i == 4:
								did = pat[i]
							elif i == 5:
								is_summary = pat[i]
							elif i == 6:
								user_id = pat[i]

							test_4 =  Im_Test(did)
							test_4.run_test(source=source, q_type=q_type, pay_amount=pay_amount, times=times, is_summary=is_summary, user_id=user_id)

							else:
								break

				else:
					exit('感谢使用')