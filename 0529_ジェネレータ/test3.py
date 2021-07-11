# ジェネレータはイテレーターの要素
# イテレーターは、反復処理で、リストなどをforで回す
# ジェネレータは、反復処理するときに一要素取り出して生成するというやり方をする

def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good morning'   # yeildは算出するという意味
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
c = counter()

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
print(next(g))   # イテレーターのエラー（greetingに4つ目はないので)