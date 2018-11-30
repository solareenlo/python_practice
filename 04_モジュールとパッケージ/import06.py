# importするモジュールの書き方の順番は,
# 標準ライブラリ -> サードパーティー製 -> 自分たちのチームで使用するライブラリ -> 自分専用のライブライ(ローカルなライブラリ)
# の順番に書いて, 間を1行空ける
import collections
import os
import sys

import termcolor

import package

import config

print(collections.__file__) # collectionsのファイルパスを表示
print(termcolor.__file__) # termcolorのファイルパスを表示
print(package.__file__) # packageのファイルパスを表示

print(sys.path) # Pythonが読み込むライブラリのパスと順番を表示. 一番初めにローカル(自分専用のライブリ)を読み込むので, 名前をつけるときは気をつける.
