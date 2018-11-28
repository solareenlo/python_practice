"""This is a test program."""
my_friends: set = {'A', 'B', 'C'}
A_friends: set = {'B', 'D'}
print(my_friends & A_friends) # {'B'} と表示. 共通の友達を見つけれる

f: list = ['apple', 'banana', 'apple', 'banana']
kind: set = set(f) # listをsetに型変換することで, 種類を摘出できる
print(kind)
