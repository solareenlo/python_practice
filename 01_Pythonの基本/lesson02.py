"""This is a test program."""
# 普通に表示
print('Hi', 'Mike')

# 区切りを,にする
print('Hi', 'Mike', sep=',')

# 文末の最後を\nにする（デフォルトでは\nになってます）
print('Hi', 'Mike', sep=',', end='\n')
print('Hi', 'Mike', sep=',', end='\n')

# 文末の最後に何も入れない
print('Hi', 'Mike', sep=',', end='')
print('Hi', 'Mike', sep=',', end='')

print('')

# 文末の最後にピリオドを入れて, 改行する
print('Hi', 'Mike', sep=',', end='.\n')
