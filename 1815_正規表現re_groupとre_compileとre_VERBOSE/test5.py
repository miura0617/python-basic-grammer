import re

# re.VERBOSEで長い正規表現を可読性よくする
RE_STACK_ID = re.compile(r"""
     arn:aws:cloudformation:
     (?P<region>[\w-]+):                # region
     (?P<account_id>[\d]+)              # account_id
     :stack/
     (?P<stack_name>[\w-]+)/            # stack_name
     [\w-]+""", re.VERBOSE)

s1 = ('arn:aws:cloudformation:us-east-2:123456789012:stack/'
     'mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786')
s2 = ('arn:aws:cloudformation:us-east-1:888456789012:stack/'
     'mystack-mynestedstack-sggfrhxhugar/f449b250-b969-11e0-a185-5081d0136786')

for s in [s1, s2]:

     # m = re.match(r'arn:aws:cloudformation:(?P<region>[\w-]+):(?P<account_id>[\d]+):stack/(?P<stack_name>[\w-]+)/[\w-]+', s)
     m = RE_STACK_ID.match(s)           # 同じmatch処理を繰り返すのは処理時間が長いので、このようにre.compileを使って書き換えられる
     if m:
        print('go next')
        print(m.group())                # 省略せずにマッチオブジェクト内容を表示
        print(m.group('region'))        # ?Pで名前をつけた部分のみ抽出できる
        print(m.group('account_id'))        # ?Pで名前をつけた部分のみ抽出できる
        print(m.group('stack_name'))        # ?Pで名前をつけた部分のみ抽出できる


