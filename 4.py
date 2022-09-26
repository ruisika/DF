import re,time
from config import eval_code,http_log_dir,eval_ip_dir


def sqlin_scan():
    eval_ip = []
    f = open(http_log_dir,'r')
    # print(f.readline())
    for i in f:
        if(re.findall(eval_code,i)):
            a = re.findall('^(.*?) -',i)[0]
            eval_ip.append(a)
            print('存在恶意字段，恶意ip为：'+str(a))
            #写入恶意ip
            with open(eval_ip_dir,'a') as xie:
                xie.write(str(a))
        else:
            print('无')

    print(eval_ip)

    f.close()


sqlin_scan()