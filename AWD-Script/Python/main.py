import re
import os
import sys
from datetime import datetime
import url
import attack
import ipfind




needlist = url.needlist

sqllist,xsslist,senlist = [],[],[]

otherurl,iplist = [],[]


[xssip,sqlip,senip,sqllist,xsslist,senlist,otherurl]=attack.find_attack(needlist)

xssip = list(set(xssip))

sqlip = list(set(sqlip))

senip = list(set(senip))

print('>>>>>>>检测出xss攻击'+str(len(xsslist))+'次'+'共计'+str(len(xssip))+'个ip')
print(xssip)
print('>>>>>>>检测出sql攻击'+str(len(sqllist))+'次'+'共计'+str(len(sqlip))+'个ip')
print(sqlip)
print('>>>>>>>检测出敏感目录扫描'+str(len(senlist))+'次'+'共计'+str(len(senip))+'个ip')
print(senip)

iplist = list(set(xssip+sqlip+senip))
print(len(iplist))

print('开始分析ip地理位置')
for i in iplist:

    ipfind.find_ipaddrs(str(i))