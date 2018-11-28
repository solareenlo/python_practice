"""This is a test program."""
d: dict = {'x': 10, 'y': 20}
print(d) # {'x': 10, 'y': 20} と出力
print(d['x'], d['y']) # 10 20 と出力

d['x'] = 100 # 既存のkeyのvalueの値を変更
print(d) # {'x': 100, 'y': 20} と出力

d['z'] = 30 # 新たなkeyとvalueを追加
print(d) # {'x': 10, 'y': 20, 'z': 30} と出力

d[1] = 999 # keyには数値もok
print(d) # {'x': 100, 'y': 20, 'z': 30, 1: 999}と出力

print(dict(a=10, b=20)) # {'a': 10, 'b': 20} と出力

print(dict([('a', 10), ('b', 20)])) # {'a': 10, 'b': 20} と出力
