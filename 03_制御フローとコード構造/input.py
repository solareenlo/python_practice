"""This is a test program."""
while True:
    print('Please input integer')
    word: str = input('Enter: ') # コンソールから入力された文字列をwordに格納する.
    num: int = int(word) # 文字列をint型にして, numに格納する
    if num == 100:
        break
    print('next')
