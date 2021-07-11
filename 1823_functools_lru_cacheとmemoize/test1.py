

def long_func(n):
    r = 0
    for i in range(10000000):
        r += n * i
    return r

for i in range(10):
    print(long_func(i))

print('next run')
for i in range(10):
    print(long_func(i))
