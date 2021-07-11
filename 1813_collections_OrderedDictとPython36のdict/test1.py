import collections

# Python 2.7では、普通に辞書を定義してもオーダー順ではない
# Python 3.6では、定義順になっているが、保証はされていない
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(d)

# 定義順が保証されていないので、保証したければcollections.OrderedDict()を使う
od = collections.OrderedDict(
    {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
)
print(od)
