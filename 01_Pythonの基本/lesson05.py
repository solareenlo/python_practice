"""This is a test program."""
word: str = 'python'
print(word[0]) # 1番目の文字を出力
print(word[1]) # 2番目の文字を出力
print(word[-1]) # 最後の文字を出力
print(word[0:2]) # 1番目から2番目まで出力
print(word[2:3]) # 3番目から3番目まで出力
print(word[:2]) # 1番目から2番目まで出力
print(word[2:]) # 2番目から最後まで出力

# word[0] = 'j' これはできないので, 1文字目を変えたときは,
word: str = 'j' + word[1:]
print(word)

print(word[:]) # 全部表示

n: int = len(word) # 文字列の長さを返してくれる
print(n)
