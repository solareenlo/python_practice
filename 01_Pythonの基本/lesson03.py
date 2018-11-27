"""This is a test program."""
import math

print(2 + 2)
print(5 - 2)
print(5 * 6)
print(50 - 6 * 5)
print((50 - 6) * 5)
print(8 / 5)
print(type(1), type(1.6))
print(0.6, .6) # .6も0.6と表示される
print(17 / 3)
print(17 // 3) # 商だけ表示する
print(17 % 3) # 余りを表示する
print(5 * 5)
print(5 ** 2) # 5^2のこと

pie: float = 3.14159265
print(round(pie, 2)) # 小数点第２まで表示

result: float = math.sqrt(25)
print(result)

y: float = math.log2(100)
print(y)

# print(help(math)) で, mathのhelpが出ます
