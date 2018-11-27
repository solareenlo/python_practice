"""This is a test program."""
s: str = 'hello'
print(s)
print('hello') # ''で囲ってもok
print("hello") # ""で囲ってもok
print("I don't know") # ""の中では'も出力される
# print('I don't know') ''の中では'は出力されない
print('I don\'t know') # ''の中で, 'を出力するには\'とする
print('say "I don\'t know"') # ''の中では""は使える
print("say \"I don't know\"") # ""の中で""を使うときは\"とする

print('hello.\nHow are you?')
print(r'C:\name\name') # ''の中身をそのまま出力するときは''の前にrawを意味するrを入れる

print("""\
line1
line2
lien3\
""")

print('Hi.' * 3) # 文字列を連続して３回表示

print('Py'+'thon')
print('Py''thon') # 長い文字列を見易くする時に使います

s: str = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
          'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

s2: str = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'\
          'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
print(s2)
