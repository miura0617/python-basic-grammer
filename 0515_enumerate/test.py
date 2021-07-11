for fruit in ['apple', 'banana', 'orange']:
    print(fruit)

# 上記にインデックスも追加したいとき
print('###########################')
i=0
for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)
    i += 1

# enumerate関数で簡単に書ける
print('###########################')
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)
