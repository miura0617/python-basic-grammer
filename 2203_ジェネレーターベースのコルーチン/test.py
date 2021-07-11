def g_hello():
    yield 'hello 1'
    yield 'hello 2'
    yield 'hello 3'

for w in g_hello():
    print(w)

