i = [1, 2, 3, 4, 5]
j = i
j[0] = 100        # j=iが参照渡しのため、i[0]も書き換えられる
print('j = ', j)
print('i = ', i)


x = [1, 2, 3, 4, 5]
y = x.copy()
# または
# y = x[:]
y[0] = 100
print('y = ', y)
print('x = ', x)
