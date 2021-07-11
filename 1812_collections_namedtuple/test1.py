import collections


p = (10, 20)
print(p[0])
# p[0] = 100      # タプルなので、書き換え不可

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
p = Point(10, 20)
print(p.x)
