""" Pythonのデータをそのままの形式で保存できるpickleの使い方 """
import pickle

class T(object):
    def __init__(self, name):
        self.name = name

data = {
    'a': [1, 2, 3],
    'b': ('test', 'test2'),
    'c': {'key': 'value'},
    'd': T('test3')
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f) # data をそのままの形式で, data.pickleに保存する

with open('data.pickle', 'rb') as f:
    data_loaded = pickle.load(f)
    print(data_loaded) # {'a': [1, 2, 3], 'b': ('test', 'test2'), 'c': {'key': 'value'}, 'd': <__main__.T object at 0x10a41b3c8>} と表示
    print(type(data_loaded['a'])) # <class 'list'> と表示
    print(type(data_loaded['b'])) # <class 'tuple'> と表示
    print(type(data_loaded['c'])) # <class 'dict'> と表示
    print(type(data_loaded['d'])) # <class '__main__.T'> と表示
