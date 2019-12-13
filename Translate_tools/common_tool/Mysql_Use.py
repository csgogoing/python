import pymysql

class Mysql(object):
	def __init__(self,db,charset='utf8'):
		"""初始化mysql连接"""
		try:
			host = '127.0.0.1'
			port = 3306
			user = 'root'
			passwd = 'test123'
			self.conn = pymysql.connect(host,user,passwd,db,int(port))
		except pymysql.Error as e:
			errormsg = 'Cannot connect to server\nERROR(%s):%s' % (e.args[0],e.args[1])
			print(errormsg)
			exit(2)
		self.cursor = self.conn.cursor()

	def exec(self,sql):
		"""执行dml,ddl语句"""
		# self.cursor.execute(sql)
		# self.conn.commit()
		
		try:
			self.cursor.execute(sql)
			self.conn.commit()
		except pymysql.err.IntegrityError:
			return
			self.conn.rollback()
		except Exception as e:
			print(e)
			self.conn.rollback()
			return 'wrong'


	def query(self,sql):
		"""查询数据"""
		self.cursor.execute(sql)
		return self.cursor.fetchall()

	def __del__(self):
		""" 关闭mysql连接 """
		self.conn.close()
		self.cursor.close()

if __name__ == '__main__':
	db = Mysql('multilang')
	id = 1
	chn_word = '2'
	baidu_word = '1'
	sql = "insert into common_words(id, chn_word, baidu_word) values(%d,%s,%s);"%(id,chn_word,baidu_word)
	db.exec(sql)

	#db.query("select * from common_words")