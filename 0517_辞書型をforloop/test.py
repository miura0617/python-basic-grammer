d = {'x': 100, 'y': 200}

# d.items()の中身
# リスト内[]にタプルが2つ
print(d.items())

# タプルのアンパッキングが行われ、k, vにkey, valueが代入される
for k, v in d.items():
    print(k, ':', v)
