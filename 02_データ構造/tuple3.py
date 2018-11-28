"""This is a test program."""
# 回答者に3つの選択の中から答えを2つ選んでもらう状況で,
# 問題文を変更したくないので,
# 問題文はtuple(変更不可)で, 回答文をlist(変更可)で作成する

chose_from_two: tuple = ('A', 'B', 'C')
anser: list = []

anser.append('A')
anser.append('B')

print(chose_from_two)
print(anser)

# こんな時にtupleが使えます
