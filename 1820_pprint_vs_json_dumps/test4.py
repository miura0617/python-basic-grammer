import json
import pprint   # prety printの略

# リストの場合
l = ['apple', 'orange', 'banana', 'peach', 'mango']

l.insert(0, l[:])
print(l)

print('@@@@@')

pp = pprint.PrettyPrinter(
    indent=4, width=40, compact=True, depth=3
)
pp.pprint(l)

print('@@@@@')

# 辞書の場合
d = {'a': 'A', 'b': 'B', 'c': {'x': {'y': 'Y'}}}
pp = pprint.PrettyPrinter(
    indent=4, width=40
)
pp.pprint(d)

print('@@@@@')

print(json.dumps(l, indent=4))
print(json.dumps(d, indent=4))
