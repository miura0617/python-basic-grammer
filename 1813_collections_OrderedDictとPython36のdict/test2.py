import collections

# Python 2.7では、普通に辞書を定義してもオーダー順ではない
# Python 3.6では、定義順になっているが、保証はされていない
# d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
d = {'apple': 4, 'banana': 3, 'pear': 1, 'orange': 2}       # 順番を変える
print(d)

# 定義順が保証されていないので、保証したければcollections.OrderedDict()を使う
od1 = collections.OrderedDict(
    {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
)
od2 = collections.OrderedDict(
    {'apple': 4, 'banana': 3, 'pear': 1, 'orange': 2}
)

print(od1)
print(d == od1)      # 順番を変えても、TRUE判定
print(d == od2)      # 順番を変えても、TRUE判定
print(od1 == od2)    # OrderedDict同士の比較時は、順番が違えば、FALSE判定
