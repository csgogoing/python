#coding=utf-8
from bs4 import BeautifulSoup
import re
class HtmlParser(object):


    def _get_new_data(self, soup):
        red = []
        blue = []
        mdate = []
        
        rdata = soup.find_all('em', class_="rr")
        for data in rdata:
            red.append(data.get_text())
        
        bdata = soup.find_all('em', class_="")
        for data in bdata:
            blue.append(data.get_text())
        
        mydate = soup.find_all('td', align='center')
        for edate in mydate:
            pattern = re.compile(r"[0-9]{7}")
            match = pattern.findall(edate.get_text())
            if match:
                mdate.append(match.pop())
        
        return red, blue, mdate
    
    def parse(self, html_cont):
        if  html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont,'html.parser', from_encoding='utf8')
        rdata, bdata, mdate = self._get_new_data(soup)
        return rdata, bdata, mdate
        
