""" Pythonでmongodbを扱う
まず, mongodbを保存する翁ディレクトリを作成
$ makdir ./mongodb/db
$ mongod --dbpath ./mongodb/db で, mongodbを起動しながら,
$ python mongodb1.py と, 実行する.
"""
import datetime

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'data': datetime.datetime.utcnow()
}

stack2 = {
    'name': 'customer2',
    'pip': ['python', 'java', 'rust'],
    'info': {'os': 'ubuntu'},
    'data': datetime.datetime.utcnow()
}

db_stacks = db.stacks
# stack_id = db_stacks.insert_one(stack1).inserted_id
# 検索の仕方その1
# print(stack_id, type(stack_id))
# print(db_stacks.find_one({'_id': stack_id}))
# 検索の仕方その2
# from bson.objectid import ObjectId
# str_stack_id = '5c09f755f9faee2f9d240990' # IDをobject形式で渡してあげないと検索できない.
# print(db_stacks.find_one({'_id': ObjectId(str_stack_id)}))
# 検索の仕方その3
# print(db_stacks.find_one({'name': 'customer1'}))

# stack_id = db_stacks.insert_one(stack2).inserted_id
# print(stack_id, type(stack_id))

# for stack in db_stacks.find(): # 全部のデータを見るときはforで回してあげると良い.
#     print(stack)

# 時間で検索することもできる
# now = datetime.datetime.utcnow()
# for stack in db_stacks.find({'data': {'$lt': now}}): # $lt は, lessthanの意味で, nowよりも前の時間に適合するものをfindしてね.という意味.
    # print(stack)

# データの内容を変更するには,
db_stacks.find_one_and_update(
    {'name': 'customer1'}, {'$set': {'name': 'YYY'}})

# データを削除するときは,
db_stacks.delete_one({'name': 'YYY'})
for stack in db_stacks.find(): # 全部のデータを見るときはforで回してあげると良い.
    print(stack)
