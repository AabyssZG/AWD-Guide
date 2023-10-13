import re
import urllib.request

def url_open(ip):

    url = 'http://www.ip138.com/ips138.asp?ip='+ip

    response = urllib.request.urlopen(url)

    html = response.read().decode('gb2312')

    return html


def find_ip(html):

    a = r'本站数据.{20,}</li>'

    p = re.compile(a,re.I)

    response = re.findall(p,html)

    for i in response:

        b = i

    response = re.split(r'</li><li>',b)

    ipaddrs = str(response[0][5:])+','+str(response[1][6:])+','+str(response[2][6:-5])

    return ipaddrs


def find_ipaddrs(ip):

    

    html = url_open(ip)

    ipaddrs = find_ip(html)


    print(ip+' : '+ipaddrs)
