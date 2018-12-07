"""
hbaseはワイドcolum型のDB.
$ brew install hbase で, hbaseをインストール
$ start-hbase.sh で, hbaseを起動
$ hbase thrift start で, thriftを起動
$ hbase shell で, シェルに入る
$ pip install happybase で, Pyhotonでhbaseを扱うためのライブラリーをインストール
$ stop-hbase.sh で, hbaseを停止
"""
import happybase
connection = happybase.Connection('localhost')
connection.open()

connection.create_table(b'sns', {'blog': dict()})

table = connection.table(b'sns')

table.put(
    b'user1', {
        b'blog:bitcoin': b'user1 about bitcoin',
        b'blog:soccor': b'user1 about soccer'
    }
)

table.put(
    b'user2', {
        b'blog:soccor': b'user2 about soccer'
    }
)

print(list(table.scan())) # データを全部表示
print()
print(list(table.scan(row_prefix=b'user1'))) # user1に関するデータを表示
print()
print(list(table.scan(columns=[b'blog:soccor']))) # blog:soccorに関するデータを表示

connection.disable_table(b'sns')
connection.delete_table(b'sns')
