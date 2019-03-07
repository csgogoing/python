import requests
from time import sleep
def aa():
	url = 'http://api.wws.xywy.com/api.php/doctor/doctorCommon/perfectDoctor'
	headers = {
		"Yimai-Token":"",
		"Yimai-Code":"E06A49E2-AEFB-4F4E-B5CB-6C8C2A7F4A94",
		"User-Agent":"DoctorPlatForm/5.9.9 (iPhone; iOS 11.4.1; Scale/2.00)",
		"Yimai-Request":"AWSuUHVNTIpy61qczEFqw/Mr94G4ugrpSecMYd/ScfCWUVt2vasDhONlfi8yAqwkDxBNnc3E0ty+aCKH0sdYm3GbMQQCki7ppNWs4zebk47RE497hstDwV9cWjQk0hxF5RVf8XZbLjT7aHf4MZzZX8mb+3zIAhRTPiyvNC/VxXo="
	}
	cookies={}
	cookies['sto-id']='AIAEBEAK'
	cookies['sto-id-20480']='AGAEBEAKFAAA'
	cookies['Yimai-Request']=r'XOfc15DHyJj93E7rpDghXH/pI0IQZXoUViVupyE9hg7lsnggmNJZvFypnk/i+o7YWDmVdmPEg/5bR+JaoSQ7dJVPAjLp74jha+YSpa8js4CT+D9Rv3ewq8gEgW0SY0SvRFjX0uSQdFyUv8EChjXGzK1gsciBHxtmInNuyJ0SI+g='
	params = {
		'api':'1617',
		'sign':'7284dca29361df57a14dac6a6018d0ca',
		'os':'ios',
		'source':'yimai',
		'pro':'xywyf32l24WmcqquqqTdhXZ4kg',
		'version':'1.0',
	}

	data = {
		'be_good_at':'新疆加德满都快点快点快点快点快点开',
		'city':'1107',
		'clinic':'4',
		'doctor_id':'172801060',
		'hospital_name':'石景山医院',
		'introduce':'西南交大觉得你点解点解点解点解的',
		'photo':'http://xs3.op.xywy.com/club.xywy.com/doc/20190307/e87fc579c0fe40.jpg',
		'province':'11',
		'real_name':'测试你',
		'sex':'1',
		'shf_image':'http://xs3.op.xywy.com/club.xywy.com/doc/20190307/1c1da5c42cc5bc.jpg|http://xs3.op.xywy.com/club.xywy.com/doc/20190307/06e49b36ab5631.jpg',
		'subject_first':'内科',
		'subject_phone':'010-69742578',
		'subject_second':'呼吸内科',
		'user_type':'1',
		'zhch_image':'http://xs3.op.xywy.com/club.xywy.com/doc/20190307/0b02714cfcc97e.jpg',
		'zhy_image':'http://xs3.op.xywy.com/club.xywy.com/doc/20190307/7bfea9ef439922.jpg'
	}

	r = requests.post(url,data=data,params=params,cookies=cookies)
	print(r.text)
	print('------------------------------------------------------------------')


if __name__ == '__main__':
	for i in range(20):
		aa()
		#sleep(0.5)