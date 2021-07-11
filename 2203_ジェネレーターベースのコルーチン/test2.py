def g_hello():
    yield 'hello 1'
    yield 'hello 2'
    yield 'hello 3'

g = g_hello()
print(next(g))
print(next(g))
print(next(g))
print(next(g))  # イテレーターエラー

