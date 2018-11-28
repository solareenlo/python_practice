"""This is a test program."""
d: dict = {'x': 100, 'y': 200}

print(d.items()) # dict_items([('x', 100), ('y', 200)]) と表示. .items()は辞書型をtupleのlist型として出力してくれる

for k, v in d.items(): # なので, 1つ1つのtupleの中身を分割代入して, keyをkへ, valueをvへ代入してる
    print(k, ':', v) # そして, 表示してる. x : 100 y : 200 と表示.
