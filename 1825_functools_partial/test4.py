import functools


def f(x, y):
    return x + y

# クロージャーを使わなくても、partialを使って書ける
def task(f):
    print('start task')
    print(f())

# def outer(x, y):
#     def inner():
#         return x + y
#     return inner

# f = outer(10, 20)
p = functools.partial(f, 10, 20)
task(p)
# task(lambda x, y: x + y)
