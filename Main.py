# 17-模版使用 练习题
# 1、总结导入模块的几种方式，并自定义一个计算机程序（延时一秒再返回结果）
# 实现计算机程序执行的时间并打印出计算结果，程序进行开始时间（打印出年月日）及程序运行花费的时间。

# （1）、import语句
# 用法：import+模块名
# 如：importtime、importcsv
# 如何调用模块中的函数，变量
# 用法：模块名.函数；模块名.变量
# （2）、from....import语句
# 用法：从模块中导入一个指定的部分到当前模块（函数、变量、类名）
# 例子：from csv import*,默认将csv模块中的所有函数、变量进行全部导入
# （3）、if_name_=='_main_'
# 用法：当运行的文件是程序的入口时，则会执行if name=='main'下的语句，相反，当执行的文件作为模块是被其他程序导入时，代码if name=='main'
# # 下的代码则不会执行
# import time
# begintime=time.time()
# print('项目开始的时间')
# print(('%Y-%M-%d%H:%M:%S',time.localtime()))
# def yun():
#         time.sleep(1)
#         pass
# yun()
# end_time=time.time()
# print('项目结束时间')
# print(('%Y-%M-%d%H:%M:%S',time.localtime()))
# runtime=float(end_time)-float(begintime)
# print('运行时间')
# print(runtime)
#
# #2、定义几个列表（元素全部为数值）并将其按行全部写入csv文件，然后读取该文件，并打印
# import  csv
# with  open("mytest.csv",'w')    as  r:
#         writer  =  csv.writer(r)
#         writer.writerow([41,42,43])
#         writer.writerow([51,  52,  53])
#         writer.writerow([61,  62,  63])
# print("写入完毕！")
# file=open("mytest.csv",'r')
# file1=file.read()
# print(file1)
# file.close()

# 18-发送邮件-练习题
# 请根据课堂内容，实现发送邮件的功能，要求同时发送给多个用户且包含邮件头

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
# choice=''
# to_addr=[]
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr(( Header(name, 'utf-8').encode(), addr))
# # 输入Email地址和口令:
# from_addr = input('请输入发件人的邮箱号码From: ')
# password = input('请输入发件人的邮箱密码Password: ')
# # 输入SMTP服务器地址:
# smtp_server = input('请输入邮箱服务器地址SMTP server: ')
# # 输入收件人地址:
# while choice!='N':
#     x=input('请输入收件人邮箱地址To: ')
#     to_addr.append(x)
#     choice=input('需要继续输入，请按任意键。不需要则输入N：')
#
# content = '''
# 亲爱的学员朋友：
#     你好！群发邮件1次
#     恭喜大家学习坚持到现在!
#     开课吧只为赋能人才，小课让学习更轻松！
# '''
#
# msg = MIMEText(content, 'plain', 'utf-8')
# msg['From'] = _format_addr(u'开课吧 <%s>' % from_addr)
# msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
# msg['Subject'] = Header(u'来自小K的问候……', 'utf-8').encode()
#
# server = smtplib.SMTP_SSL(smtp_server, 465)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, to_addr, msg.as_string())
# server.quit()

# 关于python的基础知识部分，已经学完了，下⾯让我们⽤这些知识来做⼀个⼩项⽬~
# # 程序开始根据输⼊内容判断打印⽼师信息还是学⽣信息
# # 定义⼀个年级类，⽤来返回年级，定义⼀个班级类返回班级，定义⼀个⽼师类继承年级和班级
# # 类，
# # 在⽼师类中定义⼀个run⽅法，在调⽤时可以打印出⽼师所在的年级，班级，学科，姓名信
# # 息，定义⼀个学⽣类继承年级和班级类，在该类中定义⼀个run⽅法⽤来打印学⽣的姓名，年
# # 龄，年级，班级信息。

# class Grade():
#     def __init__(self,grade):
#         self.grade = grade
#     def run(self):
#         # self.grade3 = self.grade
#         return self.grade
#
# class Class():
#     def __init__(self,banji):
#         self.banji = banji
#
#     def run(self):
#         # self.banji3 = self.banji
#         return self.banji
# class Teacher(Grade,Class):
#     def __init__(self,name,subject,grade1,banji1):
#         Grade.__init__(self,grade1)
#         Class.__init__(self,banji1)
#         self.name = name
#         self.subject = subject
#
#     def run(self):
#         print('我是{}年级{}班教{}的{}老师'.format(self.grade,self.banji,self.subject,self.name))
#
# class Student(Grade,Class):
#     def __init__(self,name,age,grade1,banji1):
#         Grade.__init__(self,grade1)
#         Class.__init__(self,banji1)
#         self.name = name
#         self.age = age
#
#     def run(self):
#         print('我是{}年级{}班的{}，今年{}岁了'.format(self.grade,self.banji,self.name,self.age))
# num1 = input('请输入年级：')
# grade2 = Grade(num1).run()
# num2 = input('请输入班级：')
# # print(grade2)
# banji2 = Class(num2).run()
# # print(banji2)
#
# teacher = Teacher('周林','英语',grade2,banji2)
# teacher.run()
#
# student = Student('张三',25,grade2,banji2)
#
# student.run()

# import requests
# res = requests.get('https://xiaoke.kaikeba.com/example/gexu/tengwanggexu.txt')
# import requests
# res = requests.get('https://img.kaikeba.com/web/kkb_index/img_index_logo.png')
# print(type(res))
#打印变量res的数据类型
# import requests
# #from kkb_tools import open_file
#爬虫下载图片代码：
# res = requests.get('https://img.kaikeba.com/web/kkb_index/img_index_logo.png')
# #发出请求，并把返回的结果放在变量res中
# pic=res.content
# #把Reponse对象的内容以二进制数据的形式返回
# photo = open('logo.png','wb')
# #新建了一个文件logo.png，这里的文件没加路径，它会被保存在程序运行的当前目录下。
# #图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
# photo.write(pic)
# #获取pic的二进制内容
# photo.close()
#关闭文件

#open_file('logo.png')
import requests
# #from kkb_tools import open_file
#爬虫下载图片代码：
res = requests.get('https://www.233.com/shgzz/zhuanti/zhenti2019/')
#发出请求，并把返回的结果放在变量res中
pic=res.content
#把Reponse对象的内容以二进制数据的形式返回
photo = open('logo.png','wb')
#新建了一个文件logo.png，这里的文件没加路径，它会被保存在程序运行的当前目录下。
#图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
photo.write(pic)
#获取pic的二进制内容
photo.close()
#关闭文件

#open_file('logo.png')

# 1、题⽬要求：
# #  请使⽤requests爬取⽂章，开掘⼀座⽂学理论富矿。并要求使⽤BeautifulSoup4提取出⽂
# # 本数据，将所有的标签部分去掉。
# # 地址为： https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc

import requests
from bs4 import BeautifulSoup
res=requests.get('https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc')
soup=BeautifulSoup(res.text,'html.parser')
datas=soup.find_all(class_='bjh-p')
for data in datas:
    print(data.text)

# 2、题目要求：
# 爬取三国演义每回题目，将第一回到第一百一十九回的题目爬取到本地。
# 使用技术点引导
# 使用BeautifulSoup4解析器
# requests
# 地址为：http://www.shicimingju.com/book/sanguoyanyi.html
import requests
from bs4 import BeautifulSoup
res=requests.get('https://www.shicimingju.com/book/sanguoyanyi.html')
soup=BeautifulSoup(res.text,'html.parser')
titles=soup.find_all(class_="book-mulu")
for title in titles:
    print(title.text)

