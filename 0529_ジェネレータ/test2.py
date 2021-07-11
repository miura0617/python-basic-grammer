# ジェネレータはイテレーターの要素
# イテレーターは、反復処理で、リストなどをforで回す
# ジェネレータは、反復処理するときに一要素取り出して生成するというやり方をする

l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print('#####################')

def greeting():
    yield 'Good morning'   # yeildは算出するという意味
    yield 'Good afternoon'
    yield 'Good night'

#for g in greeting():
#    print(g)

g = greeting()
print(next(g))
print('@@@@@@@@@@@')
print(next(g))
print('@@@@@@@@@@@')
print(next(g))
