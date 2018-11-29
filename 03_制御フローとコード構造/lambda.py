"""This is a test program."""
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word), end=' ')
    print('')

# def sample_func(word):
#     return word.capitalize()
# 上をlambdaで短く表現すると下のようになる
sample_func = lambda word: word.capitalize() # Mon Tue Wed Thu Fri Sat Sun と表示
change_words(l, sample_func) # Mon Tue Wed Thu Fri Sat Sun と縦に表示

# 上2行は, より簡単に, 以下のように書ける.
change_words(l, lambda word: word.capitalize()) # Mon Tue Wed Thu Fri Sat Sun と表示
change_words(l, lambda word: word.lower()) # mon tue wed thu fri sat sun と表示
# lambdaは無名関数であり, 引数と戻り値を指定できる.
# ここでは, wordが引数. word.lower()が戻り値.
