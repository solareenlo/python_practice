""" sqliteです. """
import sqlite3

# CONN = sqlite3.connect('test_sqlite.db')
CONN = sqlite3.connect(':memory:') # メモリ上にdbを仮に作ってくれる.テストしたい時に重宝する.

CURS = CONN.cursor()

# persons はtable name
CURS.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
CONN.commit() # dbのidとnameの様式を設定.

CURS.execute('INSERT INTO persons(name) values("Mike")')
CONN.commit() # name にMikeを入力. idは自動で割り振られる.

CURS.execute('SELECT * FROM persons')
print(CURS.fetchall()) # [(1, 'Mike')] と出力.

CURS.execute('INSERT INTO persons(name) values("Taro")')
CURS.execute('INSERT INTO persons(name) values("Jiro")')
CONN.commit() # TaroとJiroを入力. idは自動で割り振られる.
CURS.execute('SELECT * FROM persons')
print(CURS.fetchall()) #  [(1, 'Mike'), (2, 'Taro'), (3, 'Jiro')]と出力.

CURS.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')
CONN.commit() # 既存のデータを変更する
CURS.execute('SELECT * FROM persons')
print(CURS.fetchall()) # [(1, 'Michel'), (2, 'Taro'), (3, 'Jiro')]と出力.

CURS.execute('DELETE FROM persons WHERE name = "Michel"')
CONN.commit() # 既存のデータを削除する
CURS.execute('SELECT * FROM persons')
print(CURS.fetchall()) # [(2, 'Taro'), (3, 'Jiro')]と出力.

CURS.close()
CONN.close()

""" $ sqlite3 test_sqlite.db
$ .tables で, persons と出力される.
$ SELECT * from persons; で, 1|Mike と出力される.
"""
