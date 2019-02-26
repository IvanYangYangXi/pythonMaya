
import sqlite3
conn = sqlite3.connect('E:\Git_Res\pythonMaya\ContentBrowser\db\db.sqlite3')

cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
cursor.rowcount
cursor.close()
conn.commit()
conn.close()