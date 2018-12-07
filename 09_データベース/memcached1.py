""" memcached の基礎練
memcachedとは, データとオブジェクトをメモリ内にキャッシュする機能.
そうすることで, データベースから読み出しを行う回数を減少させ,
データベースを用いた Web サイトを高速化するために良く用いられる。
$ brew install memcached で, インストールして,
$ pip install python-memcached で, ライブラリをインストールして,
$ memcached -vv で, memcachedを起動しながら何してるか見れる.
"""
import sqlite3
import time

import memcache

DB = memcache.Client(['127.0.0.1:11211'])

DB.set('web_page', 'value1', time=3) # time にキャッシュ内に保存しておく時間を指定できる
time.sleep(1)
print(DB.get('web_page')) # value1 と表示

DB.set('counter', 0)
DB.incr('counter', 1) # counter のvalueを1増やす. という意味.
DB.incr('counter', 1)
DB.incr('counter', 1)
DB.incr('counter', 1)
print(DB.get('counter')) # 4 と表示

conn = sqlite3.connect('test_sqlite2.db')
curs = conn.cursor()
# # テーブルを作成
# curs.execute('CREATE TABLE persons(employ_id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
# # テーブルにデータを挿入
# curs.execute('INSERT INTO persons(name) values("Mike")')
# conn.commit()
# conn.close()

def get_employ_id(name): # 社員番号を検索する関数
    employ_id = DB.get(name) # キャッシュから検索するぞ.
    if employ_id: # idがキャッシュにあればTrueが返ってくるので, 以下を実行
        return employ_id # idを返す
    # キャッシュにidがないのであれば, DBにアクセスして探してくる.
    curs.execute('SELECT * FROM persons WHERE name = "{}"'.format(name))
    person = curs.fetchone()
    if not person: # DBにアクセスして(fechone()), idがなかったら,
        raise Exception('No employ')
    employ_id, name = person # personというtupleをunpackingしている.
    DB.set(name, employ_id, time=60) # で, 取ってきたnameをkeyとして, キャッシュに60秒保管してあげる.
    return employ_id
    # なので, 1回目実行したときは, DBから取得して, 2回目実行したときは,
    # 60秒以内であれば, キャッシュのDBから取得してくる. ということ.

print(get_employ_id("Mike")) # 1 と表示
