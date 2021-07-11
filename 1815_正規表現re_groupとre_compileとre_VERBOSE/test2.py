import re


s = ('arn:aws:cloudformation:us-east-2:123456789012:stack/'
     'mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786')

m = re.match(r'arn:aws:cloudformation:(?P<region>[\w-]+):(?P<account_id>[\d]+):stack/(?P<stack_name>[\w-]+)/[\w-]+', s)
print(m)
if m:
    print('go next')
    print(m.group())                # 省略せずにマッチオブジェクト内容を表示
    print(m.group('region'))        # ?Pで名前をつけた部分のみ抽出できる
    print(m.group('account_id'))        # ?Pで名前をつけた部分のみ抽出できる
    print(m.group('stack_name'))        # ?Pで名前をつけた部分のみ抽出できる

# else:
#     raise Exception('Error!)

print(m)                        # 省略されて表示される
