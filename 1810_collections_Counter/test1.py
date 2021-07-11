import collections


d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']

for word in l:
    if word not in d:   # wordが辞書dのkeyになかったら
        d[word] = 0
    d[word] += 1
print(d)

# collectionsを使って置き換え
d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d.setdefault(word, 0)
    d[word] += 1
print(d)

# collectionsのdefaultdictで置き換える
d = collections.defaultdict(int)    # int型で初期値0を設定したことになる
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d[word] += 1
print(d)



l = ['a', 'a', 'a', 'b', 'b', 'c']
c = collections.Counter()
for word in l:
    c[word] += 1
print(c)
print(c.most_common(1))     # 数が一番多いもの1つだけ表示
print(c.most_common(2))     # 数が一番多い、二番目に多いものを表示
print(c.most_common(3))
print(c.values())           # values()も使える
print(sum(c.values()))      # 更にsum()を使ってtotalを求められる


import re               # レギュラー・エクスプレッションの略

with open('test1.py', 'r') as f:
    words = re.findall(r'\w+', f.read().lower())
    print(words)
    print(collections.Counter(words).most_common(20))   # ファイルを読み取って、最も使われている文字列を探すこともできる
