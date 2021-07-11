import functools


# def f(x, y):
#     return x + y

def task(f):
    print('start task')
    print(f(10, 20))

# task(f)
task(lambda x, y: x + y)
