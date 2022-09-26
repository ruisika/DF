import pymysql,re
import datetime
import config

conn = pymysql.connect(host=config.db_host,user=config.db_user,password=config.db_password,database=config.db_dbs)

cur = conn.cursor()

def eyip(ip):
    sql = "insert into de_ip(ip) values({})".format(ip)
    cur.execute(sql)

    cur.close() #删除游标
    conn.close() #断开数据库连接

