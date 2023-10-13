import platform
import sys
import os
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

iplist = []
def get_os():
    os = platform.system()
    if os == "Windows":
        return "n"
    else:
        return "c"

def ping_ip(ip_str):
    cmd = ["ping", "-{op}".format(op=get_os()),
           "1", ip_str]
    output = os.popen(" ".join(cmd)).readlines()

    flag = False
    for line in list(output):
        if not line:
            continue
        if str(line).upper().find("TTL") >=0:
            flag = True
            break
    if flag:
        print "ip: %s is ok ***"%ip_str
    #else:
        #print "ip: %s is fail ***"%ip_str

def find_ip(ip_prefix):
    for i in range(1,256):
        ip = '%s.%s'%(ip_prefix,i)
        iplist.append(ip)

if __name__ == "__main__":
    start_time = time.time()
    commandargs = sys.argv[1:]
    args = "".join(commandargs)

    ip_prefix = '.'.join(args.split('.')[:-1])
    find_ip(ip_prefix)
    #pool = ThreadPool(50)
    pool = Pool(50)
    pool.map(ping_ip,iplist)
    pool.close()
    pool.join()
    print time.time()-start_time