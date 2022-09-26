# df

df是一个基于python制作的入侵检测防御系统。df推荐部署在linux主机上。它配备了7个模块，分别为日志入侵检测(基于机器学习)、ssh入侵检测、webshell在线查杀、sql或xss日志检测、webshell防护、sqlxss防护、封禁ip模块还有一个企业微信提醒模块，当检测到入侵行为时及时发现。

### 安装：

```sql
git clone
pip3 install requests.txt
修改config.py
```



### 使用:

当使用命令行使用时输入python3 123.py

进入界面：

![image-20220926084120677](C:\Users\jwf\AppData\Roaming\Typora\typora-user-images\image-20220926084120677.png)

输入对应的编号则进入相应的模块进行使用



#### 1.日志入侵检测

```sql
该模块具有检测linux用户使用命令是否存在异常的功能。需要保存用户的历史记录来使用。
#使用该模块需要修改config.py文件

#用户命令的位置
ML_file = 
#用户目标值位置：
ML_file1 =
#第几个目标值这是ad-lda的样本
ML_id =
```



#### 2.ssh入侵检测

```sql
该模块检测主机是否存在被ssh爆破。如果有则把相应的ip记录到恶意ip文件中。
#使用该模块需要修改config.py文件

#存放恶意ip的文件
eval_ip_dir = 
#ssh登录记录文件位置：
ssh_dir = 
```



#### 3.webshell检测

```sql
该模块是检测用户上传文件是否为恶意文件，如果为恶意文件则移送到木马文件中（木马文件目录权限全部为最低权限），正常文件则移送到正常的文件上传目录。
#使用该模块需要修改config.py文件

#文件上传目录：
upfile_dir = ''
#木马文件目录：
eval_file_dir = ''
#安全文件目录：
safe_file_dir = ''
```



### 4.sql|xss检测

```sql
该模块是检测web服务日志，查看日志中是否存在恶意的攻击行为。如果有则记录ip到恶意ip文件中。
#使用该模块需要修改config.py文件
eval_code,http_log_dir,eval_ip_dir
#日志文件位置
http_log_dir = 
#sql|xss注入字段：
eval_code = 
#恶意ip存放位置
eval_ip_dir = 
```



#### 5.webshell防护

```sql
该模块webshell持续检测，持续检测是否存在恶意文件。如果存在则会在企业微信上提示。
```



#### 6.sql|xss检测模块

```sql
该模块为持续检测，发现恶意命令直接封禁ip地址，并在企业微信上提示。
```



#### 7.封禁ip

```sql
该模块是封禁存放恶意ip文件中的ip地址的模块。
```



## 当使用web来操作时：

需要配置php、mysql环境

登录界面：

![image-20220926092043587](C:\Users\jwf\AppData\Roaming\Typora\typora-user-images\image-20220926092043587.png)

后台界面：

![image-20220926092604081](C:\Users\jwf\AppData\Roaming\Typora\typora-user-images\image-20220926092604081.png)