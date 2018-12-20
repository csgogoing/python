import mysql.connector
from mytest import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER = settings.MYSQL_USER = 'root'
MYSQL_PASSWORD = settings.MYSQL_PASSWORD = 'test123'
MYSQL_PORT = settings.MYSQL_PORT = '3306'
MYSQL_DB = settings.MYSQL_DB = 'mytest'

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
cur = cnx.cursor()

class Sql:

	@classmethod
	def insert_lottery(cls, red_0, red_1, red_2, red_3, red_4, red_5, blue, m_date):
		sql = """INSERT INTO lottery(red_0,
								  red_1,
								  red_2,
								  red_3,
								  red_4,
								  red_5,
								  blue,
								  m_date)
						  VALUES (%(red_0)s,
						  		  %(red_1)s,
						  		  %(red_2)s,
						  		  %(red_3)s,
						  		  %(red_4)s,
						  		  %(red_5)s,
						  		  %(blue)s,
						  		  %(m_date)s)"""
		value = {
								'red_0' : red_0,
								'red_1' : red_1,
								'red_2' : red_2,
								'red_3' : red_3,
								'red_4' : red_4,
								'red_5' : red_5,
								'blue'  : blue,
								'm_date': m_date,
		}
		cur.execute(sql, value)
		cnx.commit()

	@classmethod
	def select_date(cls, m_date):
		sql = "SELECT count(*) FROM lottery WHERE m_date=%(m_date)s"
		value = {
			'm_date' : m_date
		}
		cur.execute(sql, value)
		return cur.fetchone()[0]


