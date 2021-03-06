
# キャッシュのような動作をしてくれる
def memoize(f):
    memo = {}
    def _wrapper(n):
        if n not in memo:
            memo[n] = f(n)
        return memo[n]
    return _wrapper

@memoize                # デコレーターで指定
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
