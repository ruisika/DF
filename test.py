from base64 import encode
import re
from config import iface_info

a = []
with open('d:/eval_ip','r') as f:
    data = f.read()

print(list(set(re.split('\n',data))))
# b = bytes('sele',encoding='utf-8')
# print(type(b))

# print(b)
# def e():
#     if(1==1):
#         exit()
#     print(11)

# e()
# x = '123|36|444|select'
# str = '36.150.60.24 - - [19/Jul/2022:20:52:26 +0800] "GET /select HTTP/1.1" 200 217 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.27 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/601.1.27"'
# x = []
# a = re.findall('^(.*?) -',str)[0]
# x.append(a)
# print(x)
# x = []
# with open(r'd:/hist','r',encoding='utf-8') as f:
#     data = f.read()
#     data1 = re.split('\n',data)
#     data2 = data1[::2]
#     data3 = data2[-100:]
# data4 = []
# for i in range(len(data3)):
#     a = re.split(' ',data3[i])
#     data4.append(a[0])
# print(data4) 