#coding=utf-8
import html_downloader
import html_parser
import html_output


class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()

    def craw(self):
        for i in range(1,114):
            url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%d.html' % i
            print('craw %d :%s' % (i, url))
            html_cont = self.downloader.download(url)
            rdata, bdata, mdate = self.parser.parse(html_cont)
            self.output.collect_data(rdata ,bdata, mdate)

        self.output.output_text()

if __name__ == '__main__':
    obj_spider = SpiderMain()
    obj_spider.craw()
