from bs4 import BeautifulSoup
import requests
import re

url_login='http://test.admin.d.xywy.com/admin/user/login'
url="http://test.admin.d.xywy.com/question/default/index"
headers={
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}


req=requests.get(url_login)
cookies=req.cookies.get_dict()
soup=BeautifulSoup(req.text,'lxml')  
utf8_value=soup.select_one('form input[name=_csrf]').attrs['value']

data={
'_csrf':utf8_value,
'Login[username]':'admin',
'Login[password]':'123456',
'Login[verifyCode]':'testme'
}
reqs=requests.post(url_login,data=data,cookies=cookies)
a_cookies=reqs.cookies.get_dict()
print(a_cookies)

request_ele=requests.get(url,cookies=a_cookies)
k = request_ele.text
table_forms=re.findall(r'<td>(\d{5})</td>', k)
print(table_forms)