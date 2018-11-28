"""This is a test program."""
num_list: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num_list:
    print(i, end='') # 0123456789 と表示
print('')

for i in range(10): # 0から9までの10回for文が回る
    print(i, end='') # 0123456789 と表示
print('')

for i in range(2, 10): # 2から9までの8回for文が回る
    print(i, end='') # 23456789 と表示
print('')

for i in range(2, 10, 3): # 2から9までで3飛ばしで3回for文が回る
    print(i, end='') # 258 と表示
print('')
