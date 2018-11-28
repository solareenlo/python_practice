"""This is a test program."""
days: list = ['Mon', 'Tue', 'Wen']
fruits: list = ['apple', 'banana', 'orange']
drinks: list = ['coffee', 'tea', 'milk']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i]) # 3つのlistの中身を並べて表示する

for a, b, c in zip(days, fruits, drinks): # 3つのlistの中身をaとbとcにそれぞれ代入する
    print(a, b, c) # そして, それぞれを並べて表示する
