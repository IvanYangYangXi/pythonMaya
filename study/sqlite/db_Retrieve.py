#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# db_Retrieve.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 2019/2/28 下午11:16:44


import sqlite3

conn = sqlite3.connect("./test.db")
conn.text_factory = str

c = conn.cursor()

# 检索一条记录
c.execute('SELECT name FROM category ORDER BY sort')
print(c.fetchone())
print(c.fetchone())

# 将所有记录检索为列表
c.execute('SELECT * FROM book WHERE book.category=1')
print(c.fetchall())

# 遍历记录
for row in c.execute('SELECT name, price FROM book ORDER BY sort'):
    print(row)

# 遍历记录方法2
results = c.execute('SELECT sort, price FROM book')
all_Results = results.fetchall()
for row in all_Results:
    print(row)