from time import sleep
from base import Page
from im_ask import Ask
from im_doc_answer import login

class Im_Test():
	u'''寻医问药IM提问测试'''
	my_doctor = login()
	my_doctor.login_doctor()
	my_ask = Ask()

	def run_test(self, source=200002, user_id=456654, q_type=2, pay_amount=300, times=20):
		if source==200002:
			result = self.my_ask.baidu_page(q_type)
			if 'Success!' in result:
				print('提问成功')
			else:
				print('提问失败')
				return
		print(user_id)
		qid = self.my_doctor.get_id(user_id)
		sleep(2)
		self.my_doctor.take_question(qid)
		if times <= 1:
			self.my_doctor.answer_question(qid)
		elif times > 1:
			self.my_doctor.answer_question(qid)
			for i in range(times-1):
				self.my_ask.persue(qid, source, user_id)
				sleep(1)
				self.my_doctor.answer_ques_20(qid, i+2)
				sleep(1)
		else:
			print('times输入错误')

	def test_baidu(self):
		u'''测试百度来源IM提问'''
		Ask.baidu_page(q_type, uid=456654, doctor_ids=68258667, pay_amount=300, firset_dep='内科', second_dep='呼吸内科')
		po = login(self.driver)
		self.assertEqual(po.error_hint(), u"请输入用户名和密码!")
		function.insert_image(self.driver, 'baidu_result.jpg')







if __name__ == '__main__':
	A = Im_Test()
	A.run_test(source=200002, q_type=2, times=3)
