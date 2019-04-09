class A():
	# def __new__(cls):
	# 	print("__new__A execute")
	# 	return super().__new__(cls)
	def __init__(self):
		self.tempX = 1
		print("__init__A execute")
	tempZ = 3
	print("A main execute")

	def login_B(self):
		if 'tempY' in globals():
			return
		else:
			global tempY
			tempY = 2
			print("tempB被赋值")
		print("login_B execute")

	def login_C(self):
		print("login_C execute")

class B(A):
	# def __new__(cls):
	# 	print("__new__B execute")
	# 	return super().__new__(cls)
	def __init__(self):
		print("__init__B execute")
	print("B main execute")

	def test_B(self):
		super().login_B()
		print(tempY)
		print(self.tempZ)
		print("test_B")

class C(A):
	# def __new__(cls):
	# 	print("__new__C execute")
	# 	return super().__new__(cls)
	def __init__(self):
		print("__init__C execute")
	print("C main execute")

	def test_C(self):
		super().login_B()
		print(tempY)
		print(self.tempZ)
		print("test_C")

if __name__ == '__main__':
	a = A()
	print(a.tempX)
	b = B().test_B()
	c = C().test_C()