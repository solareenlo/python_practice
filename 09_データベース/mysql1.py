""" mySQLの練習
まず,
$ pip install mysql-connector-python
で, mysql.connectorを使えるようにする.
次に,
$ brew services start mysql
で, mysqlを走らせる.
mysqlと対話するときは,
$ mysql -u root
すると, mysqlとの対話モードに突入.
mysqlを終わらすには,
$ brew services stop mysql
"""
import mysql.connector

# databaseを作る
# CONN = mysql.connector.connect(host='127.0.0.1', user='root')
# CURSOR = CONN.cursor()
# CURSOR.execute('CREATE DATABASE test_mysql_database')
# CURSOR.close()
# CONN.close()
# mysql> show databases; で, どんなdatabaaseがあるか見れる

CONN = mysql.connector.connect(host='127.0.0.1', user='root',
                               database='test_mysql_database')
CURSOR = CONN.cursor()

# databaseの様式を指定
# CURSOR.execute('CREATE TABLE persons('
#                'id int NOT NULL AUTO_INCREMENT,'
#                'name varchar(14) NOT NULL,'
#                'PRIMARY KEY(id))')
# CONN.commit()
# mysql> use test_mysql_database; で, databaseをchangeして,
# mysql> show create table persons; で, 様式が見える

# dataを挿入
CURSOR.execute('INSERT INTO persons(name) values("Mike")')
CONN.commit()

# dataの中身を閲覧
CURSOR.execute('SELECT * FROM persons')
for row in CURSOR:
    print(row) # (1, 'Mike') と表示
# mysql> SELECT * FROM persons; で, databaseの中身が見れる

# "Mike"を"Michel"に変更する
# CURSOR.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')
# CONN.commit()

# "Michel"を削除する
CURSOR.execute('DELETE FROM persons WHERE name = "Michel"')
CONN.commit()

CURSOR.close()
CONN.close()
