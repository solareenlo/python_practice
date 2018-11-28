"""This is a test program."""
d: dict = {'x': 10, 'y': 20}

print(d.keys()) # dict_keys(['x', 'y']) と表示

print(d.values()) # dict_values([10, 20]) と表示

d2: dict = {'x': 100, 'j': 500}
d.update(d2) # dにd2の内容が上書きされる
print(d) # {'x': 100, 'y': 20, 'j': 500} と表示

print(d['x'], d.get('x')) # 100 100 と表示

print(d.pop('x')) # dの中からxを切り取る 100 と表示
print(d) # {'y': 20, 'j': 500} と表示

del d['y'] # yを削除
print(d) # {'j': 500} と表示

del d # dの存在自体を削除
# print(d) は, エラーになる

d: dict = {'x': 10, 'y': 20}
d.clear() # dの中身を全て削除 dは空のdictionaryとして残る
print(d) # {} と表示

d: dict = {'x': 10, 'y': 20}
print('x' in d) # dの中にaというkeyはありますか？ True と表示
print('j' in d) # dの中にjというkeyはありますか？ False と表示
