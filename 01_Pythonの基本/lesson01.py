# Pythonでは変数の型宣言をしなくても良い
# Pythonでは文末に;が必要ない
"""This is a test program."""
print('hello world')

num: int = 1
name: str = '1'
num2 = 2
name2 = 'test'

print(num, type(num))
print(name, type(name))
print(num2, type(num2))
print(name2, type(name2))

new_num: int = int(name)

print(new_num, type(new_num))
