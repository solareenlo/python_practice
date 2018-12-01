s = """\
abc
def
ghi
"""

with open('test.md', 'w+') as f: # 'w+'は書き込んだ後に読み込めますよ.という意味
    f.write(s)
    f.seek(0) # seekを一番初めに戻してあげて, 読み込みを一番初めからできるようにしてあげてる.
    print(f.read()) # abc def ghi と縦に表示

with open('test.md', 'r+') as f: # 'r+'は読み込んだ後に書き込めるようにしてくれる.
    print(f.read()) # abc def ghi と縦に表示
    f.write('test\n')
    f.seek(0)
    print(f.read()) # abc def ghi test と縦に表示
