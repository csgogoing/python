import requests


#下面是一些测试代码。  
if __name__ == "__main__":  
	url = 
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
	}
	for i in range(2):
		req = requests.get(self.url_login, headers=self.headers, auth=HTTPBasicAuth('XyWy_wenKANG_C199','A3ci1UvKUk'))
		f = open('%d.jpg'%i, 'w') # 若是'wb'就表示写二进制文件
		f.write(req.content)
		f.close()