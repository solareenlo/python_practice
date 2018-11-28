"""This is a test program."""
for fruit in ['apple', 'banana', 'orage']:
    if fruit == 'banana':
        print('stop eatting') # breakでfor文を抜ければstop eattingを表示
        break
    print(fruit)
else:
    print('I ate all!') # breakでfor文を抜けなければI ate all!を表示
