# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:13:38 2018

@author: 1871
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import pymysql
#commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作。每一个方法都开始了一个新的事务。
# 打开数据库连接:参数顺序为数据库IP、数据库用户名、密码、数据库名称：
db = pymysql.connect("localhost", "root", "123456", "test")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data) #打印输出数据库版本%s表示字符串格式

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE") # 删除一个表格

# 使用预处理语句创建表: 建立了5个字段firstname,lastname,age,gender,income
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         Gender CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
#执行插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, Gender, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# SQL 插入语句得第二种方法
#sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#      LAST_NAME, AGE, Gender, INCOME) \
#       VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
#      ('Mac', 'Mohan', 20, 'M', 2000)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()


## SQL 查询语句语句： 找出工资income大于1000得情况
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % (1000)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
       # 打印结果：多个变量同时输出方式“% \”字符
      print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fetch data")


# SQL 更新修改数据库语句、内容：修改年龄+1岁
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE Gender = '%c'" % ('M')
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

## SQL 删除语句功能
sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (25)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()