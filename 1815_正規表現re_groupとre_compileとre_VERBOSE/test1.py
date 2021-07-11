import re


s = ('arn:aws:cloudformation:us-east-2:123456789012:stack/'
     'mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786')

m = re.match(r'arn:aws:cloudformation:[\w-]+:[\d]+:stack/[\w-]+/[\w-]+', s)
print(m)
if m:
    print('go next')
    print(m.group())            # 省略せずにマッチオブジェクト内容を表示
# else:
#     raise Exception('Error!)

print(m)                        # 省略されて表示される
