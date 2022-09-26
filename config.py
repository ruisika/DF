#日志文件位置：
from sklearn.neural_network import MLPClassifier
#日志文件位置
http_log_dir = '/log.txt'

#sql|xss注入字段：
eval_code = 'select|aa3|36'

eval_ip_dir = 'd:/eval_ip'

#文件上传目录：
upfile_dir = ''

#木马文件目录：
eval_file_dir = ''

#安全文件目录：
safe_file_dir = ''

#网卡信息：
iface_info = 'eth0'
#过滤规则在RE.listte文件最后 可自行修改

#恶意代码目录：
eval_code_dir = ''

#ssh登录记录文件位置：
ssh_dir = '/var/log/secure'

#ip白名单：
all_ip = ''


#######机器学习文件
#用户样本的位置：
ML_file = "d:/User3"

#用户目标值位置：
ML_file1 = "d:/label.txt"

#第几个目标值这是ad-lda的样本
ML_id = 2


#数据库信息：地址 用户名 密码 数据库
db_host = "127.0.0.1"
db_user = "root"
db_password = "root"
db_dbs = "blog"