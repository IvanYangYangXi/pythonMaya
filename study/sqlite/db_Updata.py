#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# db_Updata.py
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 2019/2/28 下午11:36:01


import sqlite3


conn = sqlite3.connect("test.db")
c = conn.cursor()

# 更新
c.execute('UPDATE book SET price=? WHERE id=?',(1000, 1))
# 删除
c.execute('DELETE FROM book WHERE id=2')

conn.commit()
conn.close()