import functools


def d(f):
    @functools.wraps(f)             # これがないと、help関数で w()のdocstringが返される
    def w():
        """ Wrapper docstring """
        print('decorator')
        return f()
    return w


@d
def example():
    """ Example docstring """
    print('example')

# example()

# print(example.__doc__)
help(example)
