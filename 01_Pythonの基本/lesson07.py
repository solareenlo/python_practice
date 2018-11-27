"""This is a test program."""
print('a is {}'.format('a')) # {}の中身をaにする

print('a is {}'.format('test')) # {}の中身をtestにする

print('a is {} {} {}'.format(1, 2, 3)) # {} {} {} の中身をそれぞれ1 2 3にする

print('a is {0} {1} {2}'.format(1, 2, 3)) # 上と同じこと

print('a is {2} {1} {0}'.format(1, 3, 5)) # {}のインデックスを指定して代入できる

print('My name is {} {}'.format('sola', 'taro')) # My name si sola taro と出力される

print('My name is {name} {family}. Watashi ha {family} {name} desu.'
      .format(name='sola', family='taro')) # インデックスに名前を付けてそれぞれに代入できる

print(str(1)) # 1の型を文字列へ
print(str(3.14)) # 3.14の型を文字列へ
print(str(True)) # Trueの型を文字列へ
