f = open('test.md', 'w') # 'w' は上書き, 'a' は追加
f.write('Test\n') # test.md に, Test と書き込み
print('My name is sola.', file=f) # test.md に, My name is sola. と書き込み
print('My', 'name', 'is', 'sola', sep='#', end='!\n', file=f) # test.md に My#name#is#sola! と書き込み
f.close()
