import os
import sys
import url


sqllist,xsslist,senlist = [],[],[]

otherurl,xssip,sqlip,senip = [],[],[],[]

feifa = [] 
def find_attack(needlist):

    print('>>>>>>>开始检测攻击')

    sql = r'product.php|preg_\w+|execute|echo|print|print_r|var_dump|(fp)open|^eval$|file_get_contents|include|require|require_once|shell_exec|phpinfo|system|passthru|\(?:define|base64_decode\(|group\s+by.+\(|%20or%20|%20and%20|sleep|delay|nvarchar|exec|union|^select$|version|insert|information_schema|chr\(|concat|%bf|sleep\((\s*)(\d*)(\s*)\)|current|having|database'

    xss = r'alert|^script$|<|>|%3E|%3c|&#x3E|\u003c|\u003e|&#x'

    sen = r'\.{2,}|%2e{2,}|%252e{2,}|%uff0e{2,}0x2e{2,}|\./|\{FILE\}|%00+|json|\.shtml|\.pl|\.sh|\.do|\.action|zabbix|phpinfo|/var/|/opt/|/local/|/etc|/apache/|\.log|invest\b|\.xml|apple-touch-icon-152x152|\.zip|\.rar|\.asp\b|\.php|\.bak|\.tar\.gz|\bphpmyadmin\b|admin|\.exe|\.7z|\.zip|\battachments\b|\bupimg\b|uploadfiles|templets|template|data\b|forumdata|includes|cache|jmxinvokerservlet|vhost|bbs|host|wwwroot|\bsite\b|root|hytop|flashfxp|bak|old|mdb|sql|backup|^java$|class'

    

    for i in needlist:

        if i[2] == 'POST' or i[2] == 'HEAD' or i[2] == 'GET':

            response = re.findall(sql,i[3],re.I)

            if response == []:

                responsexss = re.findall(xss,i[3],re.I)

                if responsexss == []:

                    responsesen = re.findall(sen,i[3],re.I)

                    if responsesen == []:

                        otherurl.append(i)

                    else:

                        senlist.append(i)

                        senip.append(i[0])

                        print(responsesen)

                        print('检测出敏感目录扫描')

                        print(i)

                else:

                    xsslist.append(i)

                    xssip.append(i[0])

                    print(responsexss)

                    print('检测出xss攻击')

                    print(i)

            else:

                sqllist.append(i)

                sqlip.append(i[0])

                print(responsexss)

                print('检测出sql攻击')

                print(i)

        else:

            feifa.append(i[0])

    print('非法请求:'+str(len(feifa))+'次'+str(len(list(set(feifa))))+'个ip')

    print('>>>>>>>攻击检测完毕')

    return [xssip,sqlip,senip,sqllist,xsslist,senlist,otherurl]