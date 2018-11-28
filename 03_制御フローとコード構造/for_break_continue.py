"""This is a test program."""
some_list: list = [1, 2, 3]

i: int = 0
while i < len(some_list):
    print(some_list[i]) # 1 2 3 と縦に表示
    i += 1

for i in some_list:
    print(i) # 1 2 3 と縦に表示

for s in 'abc':
    print(s) # a b c と縦に表示

for word in ['My', 'name', 'is', 'sola']:
    print(word) # My name is sola と縦に表示

for word in ['My', 'name', 'is', 'sola']:
    if word == 'name':
        break # Myだけ表示
    print(word)

for word in ['My', 'name', 'is', 'sola']:
    if word == 'name':
        continue # name表示が飛ばされて, My is solaと縦に表示
    print(word)
