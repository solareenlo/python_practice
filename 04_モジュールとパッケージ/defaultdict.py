# Pythonにも標準ライブラリがたくさんある.
# その中のdefaultdictを試してみます.
# 文字列の中の文字の出現回数を数えてみます.

s = 'ksjdflkhasklfalkshfkahsdkjhfakjdhk'

# 方法その1
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

# 方法その2 (少し短く書ける)
d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

# 方法その3 (さらに短く書ける)
from collections import defaultdict # 標準ライブライであるcollectionsの中のdefaultdictを呼び出してる
d = defaultdict(int) # dをdefaultdice(int)で, int型でdictionary型で初期化
for c in s:
    d[c] += 1
print(d)
