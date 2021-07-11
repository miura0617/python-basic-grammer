import collections


# p = (10, 20)
# print(p[0])
# # p[0] = 100      # タプルなので、書き換え不可

# class Point(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y 
# p = Point(10, 20)
# print(p.x)

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(10, y=20)
print(p.x)
# p.x = 100           # タプルのように書き込み不可になっている


p1 = Point._make([100, 200])
print(p1)
print(p1._asdict())

p1._replace(x=500)
print(p1)               # ここではxは変わらない
p2 = p1._replace(x=500) # 新たに作る時にp1をベースにリプレイスするときは反映される
print(p2)

class SumPoint(collections.namedtuple('Point', ['x', 'y'])):
    @property
    def total(self):
        return self.x + self.y

p3 = SumPoint(2, 3)
print(p3.x, p3.y, p3.total)
