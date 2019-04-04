class A:
	# def __new__(cls):
	# 	print("__new__A方法被执行")
	# 	return super().__new__(cls)
	def __init__(self):
		self.tempA = 1
		print("__init__A方法被执行")

	def login_B(self):
		if 'tempB' in globals():
			return
		else:
			global tempB
			tempB = 2
			print("tempB被赋值")
		print("login_B方法被执行")

	def login_C(self):
		print("login_C方法被执行")

class B(A):
	# def __new__(cls):
	# 	print("__new__B方法被执行")
	# 	return super().__new__(cls)
	def __init__(self):
		print("__init__B方法被执行")

	def test_B(self):
		super().login_B()
		print(tempB)
		print("test_B")

class C(A):
	# def __new__(cls):
	# 	print("__new__C方法被执行")
	# 	return super().__new__(cls)
	def __init__(self):
		print("__init__C方法被执行")

	def test_C(self):
		super().login_B()
		print(tempB)
		print("test_C")

#a = A()
b = B().test_B()
c = C().test_C()