""" Python独自のDBであるDBMの練習
DBMはものすごく簡易的なDB
"""
import dbm

with dbm.open('cache', 'c') as db:
    # db['key1'] = 'value1'
    # db['key2'] = 'value2'
    db['key3'] = 1 # これはエラーになっちゃう.

with dbm.open('cache', 'r') as db:
    print(db.get('key1')) # b'value1' と表示.
