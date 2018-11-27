"""This is a test program."""
s: str = 'My name is sola. Hi sola.'
print(s)
is_start: bool = s.startswith('My')
print(is_start)
is_start: bool = s.startswith('X')
print(is_start)

print(s.find('sola')) # solaという文字列は前から何番目にありますか？
print(s.rfind('sola')) # 後ろのsolaという文字列は前から番目にありますか？
print(s.count('sola')) # solaという文字列は何個ありますか？
print(s.capitalize()) # 最初の1文字だけ大文字にして, 後の文字は小文字にする
print(s.title()) # 各文字の1文字目を大文字にする
print(s.upper()) # 全ての文字を大文字にする
print(s.lower()) # 全ての文字を小文字にする
print(s.replace('sola', 'Taro')) # solaをTaroに変換
