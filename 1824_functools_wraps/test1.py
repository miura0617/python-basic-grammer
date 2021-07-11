import functools


def d(f):
    def w():
        print('decorator')
        return f()
    return w


@d
def example():
    print('example')

example()