import collections


a = {'a': 'a', 'c': 'c', 'num': 0}
b = {'b': 'b', 'c': 'cc'}
c = {'b': 'bbb', 'c': 'ccc'}

# # updateメソッドにより、keyの値を上書きしている
# print(a)
# a.update(b)
# print(a)
# a.update(c)
# print(a)

# keyの値を上書き前後の値をもう一度戻って使いたいケースが発生したときに、collectionsのChainMapが有効
m = collections.ChainMap(a, b, c)
print(m)        # 読み込んだ状態を表示
print(m.maps)   # リスト化される
m.maps.reverse()
print(m.maps)
m.maps.insert(0, {'c': 'CCCCCCC'})  # ChainMapに新しい辞書を追加
print(m.maps)
del m.maps[0]
print(m.maps)
print(m['c'])
m['b'] = 'BBBBBB'   # 一番最初のkeyが'b'の値だけが変わる
print(m.maps)


