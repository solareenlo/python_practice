"""
グラフ型DBのneo4jの練習
うまくホストと繋がらないが, こんな感じです.
"""
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

# DB内を削除してくれる関数
def clear_db(tx):
    tx.run('MATCH (n) DETACH DELETE n')

# データを追加する関数
def add_friend(tx, name, friend_name=None):
    if not friend_name:
        return tx.run('CREATE (p:Person {name: %name}) RETURN p', name=name)
    return tx.run('MATCH (p:Person {name: $name})'
                  'CREATE (p)-[:FRIEND]->(:Person {name: $friend_name})',
                  name=name, friend_name=friend_name)

# データを表示する
def print_friend(tx, name):
    for record in tx.run('MATCH (p {name: $name})-[:FRIEND]->(yourFriends)'
                         'RETURN p, yourFriends', name=name):
        print(record)

with driver.session() as session:
    # DB内データを削除する関数を実行する
    session.write_transaction(clear_db)
    # データを追加する関数を実行する
    session.write_transaction(add_friend, 'Taro')
    for f in ['Mike', 'Nancy']:
        session.write_transaction(add_friend, 'Taro', f)
    # データを表示する関数を実行する
    session.read_transaction(print_friend, 'Taro')
