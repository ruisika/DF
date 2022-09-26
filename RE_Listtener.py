from scapy.all import *
import re,de_ip
from config import eval_ip_dir,iface_info,eval_code_dir
import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='blog', charset='utf8')
cur = conn.cursor()

def packet_callback(packet):
    #print(packet.show())
    re_1 = bytes(eval_code_dir,encoding='utf-8')
    data=bytes(packet[TCP].payload)
    #print(data)
    if b'Host' in data:
        for info in data.split(b'\r\n'):
            #print(info)
            if re.findall(re_1,info):
                print('恶意')
                de_ip.de_ip()
                with open(eval_ip_dir,'a') as xie:
                    xie.write(packet[IP].src)
                sql = 'insert into de_ip(ip) values({})'.format(str(packet[IP].src))
                cur.execute(sql)
                
                with open(eval_code_dir,'a') as xie:
                    xie.write(str(packet[IP].src)+str(data))

                sql2 = "insert into eyjl(ip,datatime,evalcode) VALUES('{}',SYSDATE(),'{}');".format(str(packet[IP].src),str(data))
                conn.commit()
                cur.close()

# count：抓包的数量，0表示无限制；
# store：保存抓取的数据包或者丢弃，1保存，0丢弃
# offline：从 pcap 文件读取数据包，而不进行嗅探，默认为None
# prn：为每一个数据包定义一个函数，如果返回了什么，则显示。例如：prn = lambda x: x.summary()； （  packct.summar()函数返回的是对包的统计性信息 ）
# filter：过滤规则，使用wireshark里面的过滤语法
# L2socket：使用给定的 L2socket
# timeout：在给定的时间后停止嗅探，默认为 None
# opened_socket：对指定的对象使用 .recv() 进行读取；
# stop_filter：定义一个函数，决定在抓到指定数据包后停止抓包，如：stop_filter = lambda x: x.haslayer(TCP)；
# iface：指定抓包的接口 
# https://blog.csdn.net/hxzmjx/article/details/121104800

def a():
    sniff(filter='tcp port 80',iface=iface_info
,prn=packet_callback,store=0)
    #sniff(filter="icmp",count=5,prn=lambda x : x.sprintf("{IP:%IP.src%-> %IP.dst%}"))
