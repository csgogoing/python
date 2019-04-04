#coding=utf-8
from urllib.parse import parse_qs

result = parse_qs('http://admin.d.xywy.com/order/question/index?QuestionOrderSearch%5Border_type%5D=2&QuestionOrderSearch%5Bpay_source%5D=23&QuestionOrderSearch%5Bpay_status%5D=2&QuestionOrderSearch%5Bpay_type%5D=&QuestionOrderSearch%5Bkeyword_type%5D=&QuestionOrderSearch%5Bkeyword%5D=&QuestionOrderSearch%5BbgDate%5D=2019-03-03&QuestionOrderSearch%5BedDate%5D=2019-03-03')
print(result)