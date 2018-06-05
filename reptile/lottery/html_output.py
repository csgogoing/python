#coding=utf-8
import csv

class HtmlOutput(object):
    
    def __init__(self):
        self.rdatas = []
        self.bdatas = []
        self.mydates = []
        
        self.rrows = []
        self.brows = []
        self.mydate = []

    def collect_data(self, rdata ,bdata, mdate):
        #每行6个红球，1个蓝球和1个日期
        if rdata is None and bdata is None and mdate is None:
            return 
        self.rdatas.append(rdata)
        self.bdatas.append(bdata)
        self.mydates.append(mdate)

    
    def output_text(self):
        while self.rdatas:
            rrow = self.rdatas.pop()
            while rrow:
                row_r = []
                for i in range(0,6):
                    row_r.append(rrow.pop())
                self.rrows.append(row_r)
            
        while self.bdatas:
            brow = self.bdatas.pop()
            while brow:
                row_b = []
                for j in range(0,1):
                    row_b.append(brow.pop())
                self.brows.append(row_b)

        while self.mydates:
            date = self.mydates.pop()
            while date:
                row_d = []
                for k in range(0,1):
                    row_d.append(date.pop())
                self.mydate.append(row_d)        

        
        red_f = open("rcsv.csv", 'wb')
        blue_f = open("bcsv.csv", 'wb')
        date_f = open("dcsv.csv", 'wb')
        
        rwriter = csv.writer(red_f, dialect='excel')
        bwriter = csv.writer(blue_f, dialect='excel')
        dwriter = csv.writer(date_f, dialect='excel')
        
        for r in self.rrows:
            rwriter.writerow(r)
        
        for b in self.brows:
            bwriter.writerow(b)
            
        for d in self.mydate:
            dwriter.writerow(d)

        red_f.close()
        blue_f.close()
        date_f.close()
