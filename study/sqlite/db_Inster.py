#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# db_Inster
# @Author : Ivan-杨杨兮 (523166477@qq.com)
# @Link   : www.cgartech.com
# @Date   : 2019/2/28

import sqlite3


conn = sqlite3.connect("./test.db")
conn.text_factory = str

books = [(1, 1, 'Cook Recipe', 3.12, 1),
         (2, 3, 'Python Intro', 17.5, 2),
         (3, 2, 'OS Intro', 13.6, 2),
         ]
# 执行“插入”
conn.execute("insert into category VALUES (1, 1, 'kitchen')")

# 使用占位符
conn.execute("insert into category VALUES (?, ?, ?)", (2, 2, 'computer'))

# 执行多个命令
conn.executemany('insert into book VALUES (?, ?, ?, ?, ?)', books)

conn.commit()
conn.close()