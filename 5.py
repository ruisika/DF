from inspect import getcomments
from subprocess import getoutput
import re,requests,os,json
import time
from config import upfile_dir,safe_file_dir,eval_file_dir

def get_fname(upfile_dir):
    for root,dir,flist in os.walk(upfile_dir):
        return flist

def baiduscan_dirwebshell():
    fname = get_fname(upfile_dir)
    print(fname)
    print(len(fname))
    for i in range(len(fname)):
        print(fname[i])
        web_dir = 'curl https://scanner.baidu.com/enqueue -F archive=@'+upfile_dir+'/'+fname[i]
        #调用webdir的api 返回json
        get_url = getoutput(web_dir)
        #print(get_url)
        #对json进行筛选出返回结果的url
        re_geturl=re.findall(r'"url":"(.*)"',get_url)
        # print(re_geturl)
        if(not re_geturl):
            print("你输入的有误")
            continue

        re_geturl = re.sub(r"\\","",re_geturl[0])
        #获取结果
        # print(re_geturl)
        time.sleep(1)
        re_getdetect = re.findall(r'"detected":(.),',requests.get(re_geturl).text)
        time.sleep(1)


        if(re_getdetect[0] == '1'):
            print("存在恶意木马")
            # getoutput('mv ' + fname[i] + " " + eval_file_dir)
        else:
            print('检测为正常')
            # getoutput('mv ' + fname[i] + " " + safe_file_dir)

def weibuscanwebshell():
    hear = {'Host':'s.threatbook.cn','Cookie':'gr_user_id=54e001ce-6165-4e32-b774-b9caab4448e5;889930cec4eb8153_gr_session_id_04fb9378-c415-4be8-9b33-fca9cbd2edeb=true;889930cec4eb8153_gr_session_id=04fb9378-c415-4be8-9b33-fca9cbd2edeb;zg_did=%7B%22did%22%3A%20%22181a5502aa9998-041405f71cce82-c545421-1fa400-181a5502aaa70d%22%7D;zg_8ce95389de054b5c90bb62222cf45190=%7B%22sid%22%3A%201656335903404%2C%22updated%22%3A%201656335903413%2C%22info%22%3A%201656335903411%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22passport%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22s.threatbook.cn%22%7D','User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:101.0)Gecko/20100101Firefox/101.0','Accept':'application/json,text/plain,*/*','Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2','Accept-Encoding':'gzip,deflate','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','Te':'trailers'}
    #上传地址
    url1 = "https://api.threatbook.cn/v3/file/upload"
    fields = {
    #apikey更换自己的
    'apikey': '95dc6254297f4a9480ea4f333c3460aaa1e439e210c54be7b7bcf51601bf9d7a',
    'sandbox_type': 'win7_sp1_enx86_office2013',
    'run_time': 60
    }
    file_dir = '/root/bishe'
    file_name = '6.php'
    files = {
    'file' : (file_name, open(os.path.join(file_dir, file_name), 'rb'))
    }
    response = requests.post(url1, data=fields, files=files)
    get_dict = response.json()

    #结果地址  服务器没登陆微步无法获取结果只能登录查看
    # url2 = 'https://s.threatbook.cn/apis/sample/multi_engines/'+get_dict['data']['sha256']
    # a = requests.get(url2,headers=hear)
    # print(a.text)

def a():
    while(1):
        time.sleep(1)
        baiduscan_dirwebshell()
a()
