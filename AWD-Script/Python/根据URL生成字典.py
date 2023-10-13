#coding=utf-8
 
# 根据URL生成特定目标网站备份文件猜测字典
 
suffixList = ['.rar','.zip','.sql','.gz','.tar','.bz2','.tar.gz','.bak','.dat','.mdb','.env','.config','.md','.js','.json','.ini','.inf','.py','.txt','.doc','.docx','.xml','.swp','.yaml','.yml','.log','.conf','.ssh','.lock','.sqlite','.sqlite3','.info']
 
keyList=['install','admin','sa','back','backup','说明','install','INSTALL','index','INDEX','wwwroot','WWWROOT','www','WWW','root','ROOT','web','WEB','备份','新建文件夹','config','readme','setup','SETUP']
 
# 请输入目标URL
 
print "Please input the url:"
url = raw_input()
 
if (url[:5] == 'http:'):
    url = url[7:].strip()
 
if (url[:6] == 'https:'):
    url = url[8:].strip()
 
numT = url.find('/')
 
if(numT != -1):
    url = url - url[:numT]
 
# 根据URL，推测一些针对性的文件名:
 
num1 = url.find('.')
num2 = url.find('.',num1 + 1)
 
keyList.append(url[num1 + 1:num2])
keyList.append(url[num1 + 1:num2].upper())
 
keyList.append(url)  # www.test.com
keyList.append(url.upper())
 
keyList.append(url.replace('.','_'))  # www_test_com
keyList.append(url.replace('.','_').upper())
 
keyList.append(url.replace('.',''))  # wwwtestcom
keyList.append(url.replace('.','').upper())
 
keyList.append(url[num1 + 1:])   # test.com
keyList.append(url[num1 + 1:].upper())   
 
keyList.append(url[num1 + 1:].replace('.','_'))  # test_com
keyList.append(url[num1 + 1:].replace('.','_').upper())
 
# 生成字典列表，并写入txt文件:
 
tempList =[]
 
for key in keyList:
    for suff in suffixList:
        tempList.append(key + suff)
 
fobj = open("success.txt",'w')
 
for each in tempList:
    each ='/' + each
    fobj.write('%s%s' %(each,'\n'))
    fobj.flush()
 
print 'OK!'