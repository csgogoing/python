from .sql import Sql
from mytest.items import MytestItem

class my_piplines(object):
	"""docstring for my_piplines"""
	def process_item(self, item, spider):
		print(item)
		print(items)
		if isinstance(item, MytestItem):
			m_date = item['m_date']
			ret = Sql.select_date(m_date)
			print(ret)
			if ret:
				print('已经存在了')
				return
			else:
				red_0 = item['red_0']
				red_1 = item['red_1']
				red_2 = item['red_2']
				red_3 = item['red_3']
				red_4 = item['red_4']
				red_5 = item['red_5']
				blue  = item['blue']
				m_date= item['m_date']
				Sql.insert_lottery(red_0, red_1, red_2, red_3, red_4, red_5, blue, m_date)