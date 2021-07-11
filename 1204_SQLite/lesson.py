import sqlite3


conn = sqlite3.connect('test_sqlite.db')

# テーブル作成
curs = conn.cursor()

# SQL文
#curs.execute(
#    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)') 

# データベースに実際に書き込む
#onn.commit()

# Mikeという名前のpersonを追加してみる
#curs.execute(
#    'INSERT INTO persons(name) values("Mike")'
#)
#conn.commit()

curs.execute(
    'SELECT * FROM persons'
)
print(curs.fetchall())


#curs.execute(
#    'INSERT INTO persons(name) values("Nancy")'
#)
#curs.execute(
#    'INSERT INTO persons(name) values("Jun")'
#)
#conn.commit()

curs.execute(
    'UPDATE persons set name = "Michel" WHERE name = "Mike"'
)
conn.commit()

curs.execute(
    'SELECT * FROM persons'
)
print(curs.fetchall())

conn.close()
