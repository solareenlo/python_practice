s = """\
abc
def
ghi
jkl
"""

# with open('test.md', 'w') as f:
#     f.write(s)

with open('test.md', 'r') as f:
    print(f.tell()) # seek(読み込んでる場所) の番号を教えてくれる. この場合は0
    f.seek(5)
    print(f.tell()) # ここでは5が返ってくる
    print(f.read(1)) # 5+1 で6番目の文字eが返ってくる
    print(f.read(3)) # 6+3 で9番目の文字gが返ってくる
    print(f.tell()) # 9 が返ってくる
