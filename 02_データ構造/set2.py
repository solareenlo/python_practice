"""This is a test program."""
s: set = {1, 2, 3}
# s[0] はエラーになる. setに順番はないので.

s.add(4) # 4を追加
print(s) # {1, 2, 3, 4} と表示
s.add(4) # 4を追加するけど, もう先に4があるので変化なし. sは集合型なので.
print(s) # {1, 2, 3, 4} と表示

s.remove(4) # 4を削除
print(s) # {1, 2, 3} と表示

s.clear()
print(s) # set{} と表示
