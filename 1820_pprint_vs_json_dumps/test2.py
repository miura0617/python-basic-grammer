import json
import pprint   # prety printの略

l = ['apple', 'orange', 'banana', 'peach', 'mango']

l.insert(0, l[:])
print(l)

print('@@@@@')

pp = pprint.PrettyPrinter(
    indent=4, width=40, compact=True
)
pp.pprint(l)
