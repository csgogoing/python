#处理get请求，不传data，则为get请求
import urllib
from urllib.request import urlopen
from urllib.parse import urlencode
url='http://127.0.0.1:1990/login'
data={"username":"admin","password":123456}
req_data=urlencode(data)#将字典类型的请求数据转变为url编码
res=urlopen(url+'?'+req_data)#通过urlopen方法访问拼接好的url
res=res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
print(res)

#处理post请求,如果传了data，则为post请求
import urllib
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
url='http://127.0.0.1:1990/login'
headers = {
				'Connection': 'keep-alive',
				'Content-Type': 'application/x-www-form-urlencoded',
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
			}
data={"username":"admin","password":123456}
data=urlencode(data)#将字典类型的请求数据转变为url编码
data=data.encode('ascii')#将url编码类型的请求数据转变为bytes类型
req_data=Request(url,headers=headers,data=data)#将url和请求数据处理为一个Request对象，供urlopen调用
with urlopen(req_data) as res:
res=res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
print(res)

复制代码


相比较urllib模块，requests模块要简单很多，具体用法如下：
复制代码

# get请求
import requests
url='http://127.0.0.1:1990/login'
data={"username":"admin","password":123456}
res=requests.get(url,data)#直接用requests.get(url,data)即可，其中.get表示为get方法，不需要对字典类型的data进行处理
#res=res.text#text方法是获取到响应为一个str，也不需要对res进行转换等处理
res=res.json()#当返回的数据是json串的时候直接用.json即可将res转换成字典
print(res)

#post请求
import requests
url='http://127.0.0.1:1990/login'
data={"username":"admin","password":123456}
res=requests.post(url,data)#直接用requests.post(url,data)即可，其中.post表示为post方法，不需要对字典类型的data进行处理
#res=res.text#text方法是获取到响应为一个str，也不需要对res进行转换等处理
res=res.json()#当返回的数据是json串的时候直接用.json即可将res转换成字典
print(res)

#当传参格式要求为json串时
import requests
url='http://127.0.0.1:1990/login'
data={"username":"admin","password":123456}
res=requests.post(url,json=data)#只需要在这里指定data为json即可
#res=res.text#text方法是获取到响应为一个str，也不需要对res进行转换等处理
res=res.json()#当返回的数据是json串的时候直接用.json即可将res转换成字典
print(res)

#传参含cookie
import requests
url='http://127.0.0.1:1990/login'
data={"username":"admin","password":123456}
cookie={"sign":"123abc"}
res=requests.post(url,json=data,cookies=cookie)#只需要在这里指定cookies位cookie即可，headers，files等类似
res=res.json()
print(res)