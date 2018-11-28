"""This is a test program."""
count: int = 0
while count < 5:
    print(count, end='')
    count += 1
# 上のwhile文は 01234と表示される
print('')

count2: int = 0
while True:
    if count2 >= 5:
        break
    print(count2, end='')
    count2 += 1
# 上のwhile文は 01234と表示される
print('')

count3: int = 0
while True:
    if count3 >= 5:
        break
    if count3 == 2:
        count3 += 1
        continue # ループの最初に戻ってね(下の操作は無視してね). という意味
    print(count3, end='')
    count3 += 1
# 上のwhile文は 0134と表示される
print('')
