#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# main.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   :

import sqlite3


conn = sqlite3.connect("./test.db") # 创建sqlite.db数据库
conn.text_factory = str
conn.execute("drop table IF EXISTS category") # 删除表
conn.execute("drop table IF EXISTS book") # 删除表
# 创建表
conn.execute("""create table category
      (id int primary key, sort int, name text)""")

query = """create table book
      (id int primary key, 
       sort int, 
       name text, 
       price real, 
       category int,
       FOREIGN KEY (category) REFERENCES category(id))  
"""
conn.execute(query)
# 保存修改
conn.commit()
# 关闭与数据库的连接
conn.close()