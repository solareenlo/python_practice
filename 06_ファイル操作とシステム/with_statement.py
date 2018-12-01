with open('test.md', 'w') as f: # with を用いることで, f.close() を省略できる. with で, インデント以下を実行してくれる.
    f.write('Test\n')
