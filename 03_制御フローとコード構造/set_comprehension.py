"""This is a test program."""
s = set()
for i in range(10):
    s.add(i)
print(s) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} と表記

# 上記4行を集合内包表記で書くと
s = {i for i in range(10)}
print(s) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} と表記



s = set()
for i in range(10):
    if i % 2 == 1:
        s.add(i)
print(s) # {1, 3, 5, 7, 9} と表記

# 上記5行を集合内包表記で書くと
s = {i for i in range(10) if i % 2 == 1}
print(s) # {1, 3, 5, 7, 9} と表記
