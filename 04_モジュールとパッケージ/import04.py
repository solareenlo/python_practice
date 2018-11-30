# from package.talk import human
# from package.talk import animal
# 上2行をまとめると下の1行にすることもできるが,
# どんなモジュールが読み込まれたか分かりづらいので,
# オススメされていません.
# humanとanimalがあるディレクトリ内の__init__.pyに
# __all__ = ['animal', 'human'] を追記する
from package.talk import *

print(animal.sing())
print(animal.cry())

print(human.sing())
print(human.cry())
