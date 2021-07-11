import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1')
#conn = mysql.connector.connect(host='127.0.0.1', user='root', password='/5kIbxed(i)!')

cursor = conn.cursor()

cursor.execute(
    'CREATE DATABASE test_mysql_database'
)

cursor.close()
conn.close()
