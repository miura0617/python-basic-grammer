# repr    # representation 表示

print('s')
print(str('s'))
print(repr('s'))                # pythonオブジェクトを表示するような形になる

import datetime
d = datetime.datetime.now()
print(d)
print(str(d))
print(repr(d))                  # pythonオブジェクトを表示するような形になる

# reprをフォーマットを使って表示する方法
print('{!r} {} {!s}'.format('test', 'test1', 'test2'))

# クラスで表示
class Point(object):
    # pass
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Point<object>'

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)

p = Point(10, 200)
print('{0!r}'.format(p))        # Pyオブジェクト表示するときに, __repr__()を呼び出しており、クラス内で__repr__をオーバーライドできる（こちらはあまりオーバーライドしないことが多い）
print('{0}'.format(p))          # 文字列表示するときに, __str__()を呼び出しており、クラス内で__str__をオーバーライドできる
print('{0!s}'.format(p))        # 文字列表示するときに, __str__()を呼び出しており、クラス内で__str__をオーバーライドできる
