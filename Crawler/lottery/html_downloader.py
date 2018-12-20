#coding=utf-8
import urllib.request


class HtmlDownloader(object):
    #下载网页数据类
    def download(self, url):
        if url is None:
            return None
        
        response = urllib.request.urlopen(url)
        
        if response.getcode() != 200:
            return None
        
        return response.read()
        
