"""This is a test program."""
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y
print(d) # {'mon': 'coffee', 'tue': 'milk', 'wed': 'water'} と表示

# 上記4行を辞書内包表記で書くと
d = {x: y for x, y in zip(w, f)}
print(d) # {'mon': 'coffee', 'tue': 'milk', 'wed': 'water'} と表示
