"""This is a test program."""
a: int = 2
b: int = 1

# a が b と等しい
print(a == b)

# a が b と異なる
print(a != b)

# a が b よりも小さい
print(a < b)

# a が b よりも大きい
print(a > b)

# a が b 以下である
print(a <= b)

# a が b 以上である
print(a >= b)

# a も b も真であれば真
print(a > 0 and b > 0)

# 上と下は同じこと
if a > 0:
    if b > 0:
        print(True)

# a または b が真であれば真
print(a > 0 or b > 0)
# 上と下は同じこと
if a > 0:
    print(True)
elif b > 0:
    print(True)
