import time
import datetime
def Which_Day(year,month,day):
    dt = datetime.date(year,month,day)
    cur = datetime.datetime.now()
    dn2 = cur.timetuple().tm_yday
    print(dn2)

if __name__ == '__main__':
    Which_Day(2019,3,5)