"""This is a test program."""
t = (1, 2, 3)
t2 = (4, 5, 6)

r = []
for i in t:
    r.append(i)
print(r) # [1, 2, 3] と表示
# 上記4行をlist内包表記を使うと
r = [i for i in t]
print(r) # [1, 2, 3] と表示

r = []
for i in t:
    if i % 2 == 1:
        r.append(i)
print(r) # [1, 3] と表示
# 上記5行をlist内包表記を用いると
r = [i for i in t if i % 2 == 1]
print(r) # [1, 3] と表示

r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r) # [4, 5, 6, 8, 10, 12, 12, 15, 18] と表示
# 上記5行をlist内包表記で書くと
r = [i * j for i in t for j in t2] # [4, 5, 6, 8, 10, 12, 12, 15, 18] と表示
print(r)
