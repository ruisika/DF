import re,os
from subprocess import getoutput
from config import eval_ip_dir
from config import ssh_dir

# str = 'cat {} | grep "Failed password for" | grep "root" | cut -d " " -f 11 |sort -nr|uniq -c'.format(ssh_dir)
# str = 'cat /var/log/auth.log | grep "Failed password for" | cut -d " " -f 11 |sort -nr|uniq -c'
# cat /var/log/secure | grep "Failed password for" | cut -d " " -f 11 |sort -nr|uniq -c
# str = '''cat /var/log/auth.log | grep "Failed password for" | grep "root" | grep -Po'(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])(\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)){3}' |sort|uniq -c|sort -nr'''


def scan_ssh():
    data = getoutput('''cat {} | grep "Failed password for" | cut -d " " -f 11 |sort -nr|uniq -c'''.format(ssh_dir))
    print(data)
    user_load = {}
    data1 = re.findall('(((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3})',data)
    data1_1 = re.findall(' ([\d]) ',data)
    # print(data1_1)
    ssh_eval_ip = []
    for i in range(len(data1)):
        user_load[data1[i][0]] = data1_1[i]
        if(int(data1_1[i])>3):
            ssh_eval_ip.append(data1[i][0])
            with open(eval_ip_dir,'a') as f:
                f.write(str(data1[i][0]))
    print(ssh_eval_ip)

