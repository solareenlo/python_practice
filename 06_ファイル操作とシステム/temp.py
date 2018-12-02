import tempfile # 一時ファイルを使うための標準ライブラリ

with tempfile.TemporaryFile(mode='w+') as t: # 一時ファイル作成. これを抜けると一時ファイルは削除される.
    t.write('hello')
    t.seek(0)
    print(t.read()) # hello と表示

with tempfile.NamedTemporaryFile(delete=False) as t: # 一時ファイルは消えない
    print(t.name) # 一時ファイルの場所を表示
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(t.read()) # b'test\n' と表示

with tempfile.TemporaryDirectory() as td: # 一時ディレクトリ作成. 抜けると一時ディレクトリは削除される
    print(td) # 一時ディレクトリの場所を表示

temp_dir = tempfile.mkdtemp() # tempfileライブラリのmkdtemp()メソッドを使って, 一時ディレクトリを作成しているので, mkdtemp()を直接使うと, 一時ディレクトリが消えずに使える
print(temp_dir)
