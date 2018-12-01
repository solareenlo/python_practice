s = """\
AAA
BBB
CCC
DDD
"""

# with open('test.md', 'w') as f:
#     f.write(s)

with open('test.md', 'r') as f:
    print(f.read(), end='') # ファイル全部を一気に読み込み

with open('test.md', 'r') as f:
    while True:
        line = f.readline() # ファイル内容を1行ずつ読み込み
        print(line, end='')
        if not line:
            break

with open('test.md', 'r') as f:
    while True:
        chunk = 2
        line = f.read(chunk) # ファイル内容を2文字ずつ読み込み
        print(line)
        if not line:
            break
