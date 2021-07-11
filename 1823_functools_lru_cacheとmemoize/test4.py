
# # キャッシュのような動作をしてくれる
# def memoize(f):
#     memo = {}
#     def _wrapper(n):
#         if n not in memo:
#             memo[n] = f(n)
#         return memo[n]
#     return _wrapper

# Python3.x系では、functoolsというキャッシュのような動きをするものが存在するので紹介
import functools

@functools.lru_cache()
def long_func(n):
    r = 0
    for i in range(10000000):
        r += n * i
    return r

for i in range(10):
    print(long_func(i))

print(long_func.cache_info())   # キャッシュに何回ヒットしたかなどの情報を表示できる
long_func.cache_clear()         # キャッシュクリアすると、next runはまた遅くなる

print('next run')
for i in range(10):
    print(long_func(i))

print(long_func.cache_info())   # キャッシュに何回ヒットしたかなどの情報を表示できる
