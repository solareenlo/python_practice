"""This is a test program."""
x: int = 0

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

a: int = 5
b: int = 10

# Pythonではインデントでif分の中身がどこからどこまでかを認識している
# Pythonのインデントは基本スペース4つ
if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')
