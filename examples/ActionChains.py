from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

fp = webdriver.FirefoxProfile()
fp.set_preference("general.useragent.override",'toutiao')

driver = webdriver.Firefox(firefox_profile=fp)
driver.get('http://test.admin.d.xywy.com/admin/user/login')
driver.find_element_by_xpath('//*[@id="login-username"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="login-password"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="login-verifycode"]').send_keys('testme')
driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/div[2]/button').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div/aside[1]/section/ul/li[5]/a').click()
sleep(0.5)
driver.find_element_by_xpath('/html/body/div/aside[1]/section/ul/li[5]/ul/li[1]/a/span').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[12]').click()
while True:
	try:
		driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[22]/a[2]').click()
	except:
		ActionChains(driver).key_down(Keys.ARROW_RIGHT).perform()
