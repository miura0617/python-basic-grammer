import functools


# def f(x, y):
#     return x + y

# クロージャーを使うと、f(10, 20)の値を指定するところを、外に出せる
def task(f):
    print('start task')
    print(f())

def outer(x, y):
    def inner():
        return x + y
    return inner

f = outer(10, 20)
task(f)
# task(lambda x, y: x + y)
