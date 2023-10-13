import re
import os
import sys
from datetime import datetime


dt = datetime.now()

date = str(dt.date())



loglist = []   #   
iplist = []    #   ip统计
urllist = []   #    url统计列表
needlist = []   #    需要统计的
errorlist = []   #    格式错误的列表
ipdict,urldict = {},{}  


rizhi = str(input('请输入要分析的日志文件名'))

def find_log():

    print('>>>>>>>开始解析日志')

    with open(rizhi,'r',encoding='UTF-8',errors='ignore') as f:

        #loglist = f.readlines()

        for i in f.readlines():   #

            if i[0] != '#':

                b = re.split(' ',i)

                iplist.append(b[10])

                urllist.append(b[6])

                try:

                    needlist.append([b[10],b[1],b[5],b[6],b[15]])

                except:

                    errorlist.append(i)

    print('>>>>>>>日志解析完毕')

def count(iplist,urllist):    #统计ip url访问量函数

    print('>>>>>>>开始分析url与ip访问量')

    global ipdict,urldict

    for i in set(iplist):

        ipdict[i] = iplist.count(i)

    for i in set(urllist):

        urldict[i] = urllist.count(i)


    ipdict = sorted(ipdict.items(),key=lambda d: d[1], reverse=True)    

    urldict = sorted(urldict.items(),key=lambda d: d[1], reverse=True)

    print(type(urldict))

    iplist = list(ipdict)

    urllist = list(urldict)

    ipdict,urldict = {},{}

    print('>>>>>url与ip分析完毕.......')


    return [iplist,urllist]

def save_count():

    print('>>>>>>>正在保存分析结果')

    ipname = 'ip-'+date+'.txt'

    urlname = 'url-'+date+'.txt'

    with open(ipname,'w') as f:

        for i in iplist:

            f.write(str(list(i))+'\n')

    with open(urlname,'w') as f:

        for i in urllist:

            f.write(str(list(i))+'\n')

    print('>>>>>>>分析结果保存完毕')

find_log()

[iplist,urllist] = count(iplist,urllist)

save_count()