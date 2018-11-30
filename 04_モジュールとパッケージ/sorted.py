import builtins
builtins.print() # print関数はbuiltinsの中にあります

# 色々な初めからある組み込み関数がありますが,
# 今回はsorted()関数を試してみます.

ranking = {
    'A': 100,
    'B': 70,
    'C': 90
    }

# rankding.get('A') Aのvalueを取ってきてる

print(sorted(ranking)) # ['A', 'B', 'C'] と表示
print(sorted(ranking, key=ranking.get)) # ['B', 'C', 'A'](昇順) と表示
print(sorted(ranking, key=ranking.get, reverse=True)) # ['A', 'C', 'B'](降順) と表示
