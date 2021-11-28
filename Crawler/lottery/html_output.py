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
        red_oden = []
        statistic_red_oden = {}
        statistic_red_num = {}
        statistic_red_oden_write = []
        statistic_red_num_write = []
        statistic_blue_num = {}
        statistic_blue_num_write = []
        total_oddeven_red = {'odd':0,'even':0}
        total_oddeven_blue = {'odd':0,'even':0}
        while self.rdatas:
            rrow = self.rdatas.pop()
            while rrow:
                row_r = []
                for i in range(0,6):
                    redball = int(rrow.pop())
                    if redball in statistic_red_num.keys():
                        statistic_red_num[redball]+=1
                    else:
                        statistic_red_num[redball]=1
                    row_r.append(redball)
                self.rrows.append(row_r)
            
        while self.bdatas:
            brow = self.bdatas.pop()
            while brow:
                row_b = []
                for j in range(0,1):
                    blueball = int(brow.pop())
                    #统计个数
                    if blueball in statistic_blue_num.keys():
                        statistic_blue_num[blueball]+=1
                    else:
                        statistic_blue_num[blueball]=1
                    #统计奇偶
                    if blueball%2 == 1:
                        total_oddeven_blue['odd']+=1
                    else:
                        total_oddeven_blue['even']+=1
                    row_b.append(blueball)
                self.brows.append(row_b)

        while self.mydates:
            date = self.mydates.pop()
            while date:
                row_d = []
                for k in range(0,1):
                    row_d.append(date.pop())
                self.mydate.append(row_d)        

        
        red_f = open("rcsv.csv", 'w', newline='')
        blue_f = open("bcsv.csv", 'w', newline='')
        date_f = open("dcsv.csv", 'w', newline='')
        
        rwriter = csv.writer(red_f, dialect='excel')
        bwriter = csv.writer(blue_f, dialect='excel')
        dwriter = csv.writer(date_f, dialect='excel')
        
        #处理红球Excel
        headers_red = ['序号','平均值','号码','号码出现次数','奇偶比','奇偶比出现次数','总的奇数','总的偶数']
        rdictwriter = csv.DictWriter(red_f,headers_red)
        rdictwriter.writeheader()

        count_red = 0
        for r in self.rrows:
            count_red+=1
            #添加平均值
            avg = sum(r)/len(r)

            #添加奇偶值
            odd_num = 0
            even_num = 0
            for item in r:
                if item%2 == 1:
                    odd_num+=1
                    total_oddeven_red['odd']+=1
                else:
                    even_num+=1
                    total_oddeven_red['even']+=1
            if odd_num == 6:
                odd_even = 6
            else:
                odd_even = odd_num/even_num
            red_oden.append(odd_even)
            rwriter.writerow([count_red,avg])

        #统计红球号码出现次数
        rwriter.writerow(['统计号码出现次数'])
        for red_num in statistic_red_num:
            statistic_red_num_write.append({"号码":red_num,"号码出现次数":statistic_red_num[red_num]})
        rdictwriter.writerows(statistic_red_num_write)

        #统计红球奇偶比出现次数
        rwriter.writerow(['统计奇偶比出现次数'])
        for num in red_oden:
            if num in statistic_red_oden.keys():
                statistic_red_oden[num]+=1
            else:
                statistic_red_oden[num]=1
        for red_oden in statistic_red_oden:
            statistic_red_oden_write.append({"奇偶比":red_oden,"奇偶比出现次数":statistic_red_oden[red_oden]})
        rdictwriter.writerows(statistic_red_oden_write)

        #统计红球总的奇偶比
        rwriter.writerow(['统计总的奇偶比'])
        rdictwriter.writerows([{'总的奇数':total_oddeven_red['odd'],'总的偶数':total_oddeven_red['even']}])

        #-----------------------------------------------------------------------------------------------------
        #处理蓝球Excel
        headers_blue = ['号码','号码出现次数','总的奇数','总的偶数']
        bdictwriter = csv.DictWriter(blue_f,headers_blue)
        bdictwriter.writeheader()

        #统计篮球号码出现次数
        for blue_num in statistic_blue_num:
            statistic_blue_num_write.append({"号码":blue_num,"号码出现次数":statistic_blue_num[blue_num]})
        bdictwriter.writerows(statistic_blue_num_write)

        #统计蓝球总的奇偶比
        bwriter.writerow(['统计总的奇偶比'])
        bdictwriter.writerows([{'总的奇数':total_oddeven_blue['odd'],'总的偶数':total_oddeven_blue['even']}])


        red_f.close()
        blue_f.close()
        date_f.close()
