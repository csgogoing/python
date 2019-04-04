import datetime


if __name__ == '__main__':
	cur=datetime.datetime.now()
	pass_day = cur.timetuple().tm_yday
	print(pass_day)
	print(cur.year)
	print(cur.month)