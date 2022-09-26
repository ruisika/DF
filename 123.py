import RE_Listtener,RE_sql,de_ip,ML_history,RE_ssh,RE_webshell,kill_gid
import threading

x1_1 = 0
x2_1 = 0

while(1):
    x = [['webshell防护','webshell防护----开启'],['sqlxss防护','sqlxss防护----开启']]

    x1 = x[0][x1_1]
    x2 = x[1][x2_1]
    print("1.日志入侵检测(基于机器学习)\n2.ssh入侵检测(基于规则)\n3.webshell在线查杀\n4.sql或xss日志检测\n5.{}\n6.{}\n7.封禁ip".format(x1,x2))
    user_input = int(input("输入序列"))
    if(user_input==1):
        # x1 += 10
        # x1 = x1%2
        # print(x[0][x1])
        print('\n\n')
        s1 = threading.Thread(target = ML_history.a())
        s1.start()
        print('\n\n')
    elif(user_input==2):
        # x2 += 1
        # x2 = x2%2
        # print(x[1][x2])
        print('\n\n')
        s2 = threading.Thread(target=RE_ssh.scan_ssh())
        s2.start()
        print('\n\n')
    elif(user_input==3):
        # x3 += 1
        # x3 = x3%2
        # print(x[2][x3])
        print('\n\n')
        s3 = threading.Thread(target=RE_webshell.baiduscan_dirwebshell())
        s3.start()
        print('\n\n')
    elif(user_input==4):
        print('\n\n')
        RE_sql.sqlin_scan()
        print('\n\n')
    elif(user_input==5):
        print('\n\n')
        x1_1 = (x1_1+1)%2
        print(x1_1)
        if(x1_1==0):
            kill_gid.get_tid('RE_webshell')
            print("成功关闭")
        RE_webshell.a()
        print('\n\n')
    elif(user_input==6):
        print('\n\n')
        if(x1_1==0):
            kill_gid.get_tid('RE_Listtener')
            print("成功关闭")
        x2_1 = (x2_1+1)%2
        RE_Listtener.a()
        print('\n\n')
    elif(user_input==7):
        print('\n\n')
        de_ip.de_ip()
        print('\n\n')
    else:
        print('有误从新输入')