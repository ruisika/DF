import re,os
from subprocess import getoutput

data3 = []
def get_tid(myth):
    data = getoutput('ps -au')
    data1 = re.split('\n',data)
    for i in range(len(data1)):
        if(myth in data1[i]):
            data2 = re.split(' ',data1[i])
            for i in data2:
                if(i == ''):
                    data2.remove('')
            data2.remove('')
            data3.append(data2[1])
    print(data3)
    getoutput('kill -9 {}'.format(data3[0]))

