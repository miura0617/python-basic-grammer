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

# int意外にも, set(タプル、集合)を使える
d = collections.defaultdict(set)
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
for k, v in s:
    d[k].add(v)
print(d)                # set(タプル、集合)で表される
