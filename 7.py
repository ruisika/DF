import ipaddress
import os,re
from subprocess import getoutput
from config import eval_ip_dir

import pymysql
 

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='blog', charset='utf8')
'''
    常用方法：
    1、cursor()使用当前连接创建并返回游标
    2、commit()提交当前事务
    3、rollback()回滚当前事务
    4、close()关闭当前连接
'''
cur = conn.cursor()
cur.execute('select ip from de_ip')

deip = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}",str(cur.fetchall()))

for i in deip:
    payload = 'iptables -I INPUT -s '+ str(i) +' -j DROP'
    getoutput(payload)
