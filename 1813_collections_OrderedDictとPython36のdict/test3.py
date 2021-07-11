import collections

# Python 2.7では、普通に辞書を定義してもオーダー順ではない
# Python 3.6では、定義順になっているが、保証はされていない
# d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
d = {'apple': 4, 'banana': 3, 'pear': 1, 'orange': 2}       # 順番を変える

# dをもとにOrderedDictを作る
od = collections.OrderedDict(
    sorted(d.items(), key=lambda t: t[0])       # keyの値をもとにソート
    # sorted(d.items(), key=lambda t: t[1])       # valueの値をもとにソート
)
print(od)
od['cc'] = 100      # 追加されたものは、最後に入る
print(od)
# 再度OrderedDictに入れると、('cc', 100)もソートされる
od = collections.OrderedDict(
    sorted(od.items(), key=lambda t: t[0])       # keyの値をもとにソート
)
print(od)
